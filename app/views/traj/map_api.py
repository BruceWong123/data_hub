import os
import sys
import math
import time
import logging
import numpy as np
from functools import partial, wraps
import google.protobuf.text_format as text

import map_pb2 as map_pb2
from app.views.traj.kdtree import KDTreeAdaptor
from app.views.traj.map_utils import add_lane_points, Point, Line


def read_info_by_proto(filename, proto_format):
    if filename.split(".")[-1] == "bin":
        with open(filename, "rb") as f:
            proto_info = proto_format.FromString(f.read())
    elif filename.split(".")[-1] == "cfg" or filename.split(".")[-1] == "txt":
        with open(filename, "r") as f:
            proto_info = text.Parse(f.read(), proto_format)
    else:
        raise ValueError("unknown format!")
    return proto_info


def check_input_point_type(func):
    @wraps(func)
    def wrapper(self, point, *args, **kwargs):
        if isinstance(point, Point):
            point = np.array([[point[0], point[1]]])
        elif isinstance(point, np.ndarray):
            if len(point.shape) == 2:
                point = np.array([point])
            elif len(point.shape) == 1:
                point = np.array([[point[0], point[1]]])
            else:
                raise ValueError("only support Point and np.ndarray type")
        elif isinstance(point, list):
            point = np.array([[point[0], point[1]]])
        elif isinstance(point, tuple):
            point = np.array([[point[0], point[1]]])
        return func(self, point, *args, **kwargs)
    return wrapper


def clock(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        end = time.time()
        name = func.__name__
        if self.time_test:
            print('[Elapsed time: {}s] ->{}'.format(end - start, name))
        return result
    return wrapper


class HDMap(object):
    def __init__(self, file_name=None) -> None:
        if file_name is not None:
            self.filename = file_name
        else:
            self.filename = os.path.dirname(os.path.realpath(__file__)) \
                + "/../../test_data/baoan_p3_new.bin"
            logging.log(logging.WARNING, "use default map in the test_data")

        self.proto_map = read_info_by_proto(self.filename, map_pb2.Map())

        self.time_test = False
        self.lane_points = []
        self.lane_info = []
        self.kdtree = KDTreeAdaptor()

        self.init_map_structure()
        self.map_items = {}
        self.map_items['LANE'] = self.__lanes_table
        self.map_items['JUNCTION'] = self.__junctions_table
        self.map_items['STOP_LINE'] = self.__stop_lines_table
        self.map_items['CROSS_WALK'] = self.__crosswalks_table
        self.map_items['LANE_BOUNDARY'] = self.__lane_boundaries_table
        self.all_kdtrees = self.init_kdtrees()

    def __str__(self):
        print(self.proto_map)
        return "hdmap"

    def init_map_structure(self):
        # note heryms
        # in python we use __variable_name to define private members
        self.__clear_areas_table = {
            clear_zone.id: clear_zone for clear_zone in self.proto_map.clear_area}
        self.__crosswalks_table = {
            cross_walk.id: cross_walk for cross_walk in self.proto_map.crosswalk}
        self.__junctions_table = {
            junction.id: junction for junction in self.proto_map.junction}
        self.__lane_boundaries_table = {lane_boundary.id: lane_boundary for lane_boundary in
                                        self.proto_map.lane_boundaries}
        self.__lanes_table = {lane.id: lane for lane in self.proto_map.lane}
        self.__stop_lines_table = {
            stop_line.id: stop_line for stop_line in self.proto_map.stop_lines}
        self.__stop_signs_table = {
            stop_sign.id: stop_sign for stop_sign in self.proto_map.stop_sign}
        self.__traffic_lights_table = {traffic_light.id: traffic_light for traffic_light in
                                       self.proto_map.traffic_lights}
        self.centerline_s_dict = dict()

        for lane_id in self.__lanes_table.keys():
            lane = self.__lanes_table[lane_id]
            recalculate_centerline_s = len(
                lane.centerline.point) != len(lane.centerline_s)

            if recalculate_centerline_s:
                centerline_s = list()
                centerline_s.append(0.)
                s = 0.
                for point, point_next in list(zip(lane.centerline.point, lane.centerline.point[1:])):
                    pt1 = np.array([point.x, point.y])
                    pt2 = np.array([point_next.x, point_next.y])
                    dis = np.sqrt(np.sum((pt1 - pt2) ** 2))
                    s += dis
                    centerline_s.append(s)

                self.centerline_s_dict[lane_id] = centerline_s
            else:
                self.centerline_s_dict[lane_id] = list(lane.centerline_s)
            index = 0
            for point, point_next in zip(lane.centerline.point, lane.centerline.point[1:]):
                pt1 = np.array([point.x, point.y])
                pt2 = np.array([point_next.x, point_next.y])
                add_lane_points(pt1, pt2, lane_id, index,
                                self.lane_points, self.lane_info)
                index += 1
        self.kdtree.construct_kdtree(self.lane_points, self.lane_info)

    def init_kdtrees(self):
        kdtrees = {}
        for item_type, items in self.map_items.items():
            all_points = []
            point_info = []
            cur_tree = KDTreeAdaptor()
            for item_id in items.keys():
                item = items[item_id]
                if item_type == 'LANE':
                    points = item.centerline.point
                elif item_type == 'LANE_BOUNDARY':
                    points = item.boundary.point
                elif item_type == 'STOP_LINE':
                    points = item.stop_line.point
                elif item_type == 'CROSS_WALK':
                    points = item.polygon.point
                elif item_type == 'JUNCTION':
                    points = item.polygon.point
                else:
                    print("Error: unsupport map item type!")
                    sys.exit(-1)
                points = np.array([[pt.x, pt.y] for pt in points])
                mean_pt = points.mean(axis=0)
                all_points.append((mean_pt[0], mean_pt[1]))
                point_info.append(item)
            cur_tree.construct_kdtree(all_points, point_info)
            kdtrees[item_type] = cur_tree
        return kdtrees

    def clear(self):
        self.__clear_areas_table.clear()
        self.__crosswalks_table.clear()
        self.__junctions_table.clear()
        self.__lane_boundaries_table.clear()
        self.__lanes_table.clear()
        self.__stop_lines_table.clear()
        self.__stop_signs_table.clear()
        self.__traffic_lights_table.clear()
        self.centerline_s_dict.clear()

    @property
    def clear_zones(self):
        return self.__clear_areas_table

    @property
    def cross_walks(self):
        return self.__crosswalks_table

    @property
    def junctions(self):
        return self.__junctions_table

    @property
    def lane_boundaries(self):
        return self.__lane_boundaries_table

    @property
    def lanes(self):
        return self.__lanes_table

    @property
    def stop_lines(self):
        return self.__stop_lines_table

    @property
    def stop_signs(self):
        return self.__stop_signs_table

    @property
    def traffic_lights(self):
        return self.__traffic_lights_table

    def get_clear_zone_by_id(self, id):
        return self.__clear_areas_table.get(id)

    def get_cross_walk_by_id(self, id):
        return self.__crosswalks_table.get(id)

    def get_junction_by_id(self, id):
        return self.__junctions_table.get(id)

    def get_lane_boundary_by_id(self, id):
        return self.__lane_boundaries_table.get(id)

    def get_lane_by_id(self, id):
        return self.__lanes_table.get(id)

    def get_stop_line_by_id(self, id):
        return self.__stop_lines_table.get(id)

    def get_stop_sign_by_id(self, id):
        return self.__stop_signs_table.get(id)

    def get_traffic_light_by_id(self, id):
        return self.__traffic_lights_table.get(id)

    def find_line(self, output, **data):
        lane_id, index = output[0]
        lane_line = self.__lanes_table[lane_id].centerline
        line = Line.init_from_pb(
            lane_line.point[index], lane_line.point[index + 1])
        name = data['func_name']
        data.pop('func_name')
        squared_distance = line.__getattribute__(name)(**data)
        return squared_distance

    def get_accumulate_distance(self, lane_id, n):
        lane = self.get_lane_by_id(lane_id)
        if lane is None:
            return 0
        lane_line = self.__lanes_table[lane_id].centerline
        l = 0.
        points_slice = min(n, len(lane_line.point) - 1) + 1
        for point, point_next in zip(lane_line.point[:points_slice], lane_line.point[1:points_slice]):
            l += Point.init_from_other_type(point).distance_to(
                Point.init_from_other_type(point_next))
        return l

    @clock
    @check_input_point_type
    def get_nearest_lane(self, point):
        output = self.kdtree.query_with_k(point, k=4)
        if len(output[0]) <= 0:
            return False, [], None

        fix_data = {"pt": point,
                    "func_name": "get_mini_square_distance"
                    }
        pfunc = partial(self.find_line, **fix_data)
        distance_list = map(pfunc, output[0])
        min_pack = np.argmin(distance_list)
        min_id, min_index = output[0][min_pack][0]
        lane_line = self.__lanes_table[min_id].centerline
        line = Line.init_from_pb(
            lane_line.point[min_index], lane_line.point[min_index + 1])
        s, l = line.get_sl(point)
        s = self.get_accumulate_distance(min_id, min_index) + s
        return True, [s, l], min_id

    @clock
    @check_input_point_type
    def get_nearest_crosswalk(self, point):
        min_distance = sys.float_info.max
        flag = False
        min_crosswalk_id = -1
        point = Point.init_from_other_type(point)
        for crosswalk_id in self.__crosswalks_table.keys():
            center_point = [0., 0.]
            count = 0.
            for croswalk_point in self.__crosswalks_table[crosswalk_id].polygon.point:
                center_point[0] += croswalk_point.x
                center_point[1] += croswalk_point.y
                count += 1.
            center_point[0] = center_point[0] / count
            center_point[1] = center_point[1] / count
            center_point = Point.init_from_other_type(center_point)
            square_distance = center_point.square_distance_to(point)
            if square_distance < min_distance:
                min_distance = square_distance
                min_crosswalk_id = crosswalk_id
                flag = True
        return flag, min_crosswalk_id

    @clock
    @check_input_point_type
    def get_rough_lane_left_width(self, id, s):
        lane = self.get_lane_by_id(id)
        if lane is None:
            return False, 100000.0
        has_found, lane_point = self.get_point_and_lane_heading_by_s(id, s)
        if not has_found:
            return False, 100000.0

        if lane.left_boundary_id == 0:
            return False, 100000.0
        left_lane_id = lane.left_boundary_id
        left_boundary = self.get_lane_boundary_by_id(left_lane_id)
        if left_boundary is None:
            return False, 100000.0
        left_boundary_points = left_boundary.boundary.point
        min_square_distance = 100000
        min_index = -1
        for idx, boundary_point in enumerate(left_boundary_points):
            p = Point.init_from_other_type(boundary_point)
            square_distance = p.square_distance_to(lane_point)
            if square_distance < min_square_distance:
                min_square_distance = square_distance
                min_index = idx
        if min_index == -1:
            return False, 100000.0

        if min_index == 0 and len(left_boundary_points) == 1:
            return True, math.sqrt(min_square_distance)

        flag = False
        square_left_width = 100000.0
        if min_index != 0:
            line = Line.init_from_pb(
                left_boundary_points[min_index], left_boundary_points[min_index-1])
            square_left_width = line.get_mini_square_distance(lane_point)
            flag = True
        if min_index < len(left_boundary_points)-1:
            line = Line.init_from_pb(
                left_boundary_points[min_index], left_boundary_points[min_index+1])
            square_distance = line.get_mini_square_distance(lane_point)
            if (flag and square_distance < square_left_width) or (not flag):
                square_left_width = square_distance
            flag = True
        return flag, math.sqrt(square_left_width)

    @clock
    @check_input_point_type
    def get_rough_lane_right_width(self, id, s):
        lane = self.get_lane_by_id(id)
        if lane is None:
            return False, 100000.0
        has_found, lane_point = self.get_point_and_lane_heading_by_s(id, s)
        if not has_found:
            return False, 100000.0

        if lane.right_boundary_id == 0:
            return False, 100000.0
        right_lane_id = lane.right_boundary_id
        right_boundary = self.get_lane_boundary_by_id(right_lane_id)
        if right_boundary is None:
            return False, 100000.0
        right_boundary_points = right_boundary.boundary.point
        min_square_distance = 100000
        min_index = -1
        for idx, boundary_point in enumerate(right_boundary_points):
            p = Point.init_from_other_type(boundary_point)
            square_distance = p.square_distance_to(lane_point)
            if square_distance < min_square_distance:
                min_square_distance = square_distance
                min_index = idx
        if min_index == -1:
            return False, 100000.0

        if min_index == 0 and len(right_boundary_points) == 1:
            return True, math.sqrt(min_square_distance)

        flag = False
        square_right_width = 100000.0
        if min_index != 0:
            line = Line.init_from_pb(
                right_boundary_points[min_index], right_boundary_points[min_index - 1])
            square_right_width = line.get_mini_square_distance(lane_point)
            flag = True
        if min_index < len(right_boundary_points) - 1:
            line = Line.init_from_pb(
                right_boundary_points[min_index], right_boundary_points[min_index + 1])
            square_distance = line.get_mini_square_distance(lane_point)
            if (flag and square_distance < square_right_width) or (not flag):
                square_right_width = square_distance
            flag = True
        return flag, math.sqrt(square_right_width)

    @clock
    @check_input_point_type
    def get_nearest_lane_with_heading(self, point, heading):
        output = self.kdtree.query_with_k(point, k=4)
        if len(output[0]) <= 0:
            return False, [], None

        heading_vec = Point(np.cos(heading), np.sin(heading))

        fix_data = {"pt": point,
                    "func_name": "combo_inner_product",
                    "heading": heading_vec}
        pfunc = partial(self.find_line, **fix_data)
        distance_list = list(map(pfunc, output[0]))
        min_pack = distance_list.index(min(distance_list))
        min_id, min_index = output[0][min_pack][0]

        lane_line = self.__lanes_table[min_id].centerline
        line = Line.init_from_pb(
            lane_line.point[min_index], lane_line.point[min_index + 1])
        s, l = line.get_sl(point)
        s = self.get_accumulate_distance(min_id, min_index) + s
        return True, [s, l], min_id

    @clock
    @check_input_point_type
    def get_nearest_point(self, point):
        output = self.kdtree.query_with_k(point, k=4)
        if len(output[0]) <= 0:
            return []

        fix_data = {"pt": point,
                    "func_name": "get_mini_square_distance"}
        pfunc = partial(self.find_line, **fix_data)
        distance_list = map(pfunc, output[0])
        min_pack = np.argmin(distance_list)
        min_id, min_index = output[0][min_pack][0]
        lane_line = self.__lanes_table[min_id].centerline
        line = Line.init_from_pb(
            lane_line.point[min_index], lane_line.point[min_index + 1])
        nearest_point, _ = line.get_nearest_point_on_line(point)
        return nearest_point

    @clock
    @check_input_point_type
    def get_nearest_point_with_index(self, point, min_index):
        lane_id, index = self.lane_info[min_index]
        lane_line = self.__lanes_table[lane_id].centerline
        line = Line.init_from_pb(
            lane_line.point[index], lane_line.point[index + 1])
        nearest, _ = line.get_nearest_point_on_line(point)
        return nearest

    @clock
    def get_point_and_lane_heading_by_s(self, id, s):
        lane = self.get_lane_by_id(id)
        if lane is None:
            return False, None
        if lane.centerline is None or len(lane.centerline.point) < 1:
            return False, None
        if s <= self.centerline_s_dict[id][0]:
            return True, Point.init_from_other_type(lane.centerline.point[0])
        if s >= self.centerline_s_dict[id][-1]:
            return True, Point.init_from_other_type(lane.centerline.point[-1])

        index = np.array(self.centerline_s_dict[id]).searchsorted(s)
        delta_s = self.centerline_s_dict[id][index] - s
        if delta_s < 1e-10:
            return True, Point.init_from_other_type(lane.centerline.point[index])

        p2 = Point.init_from_other_type(lane.centerline.point[index])
        p1 = Point.init_from_other_type(lane.centerline.point[index - 1])
        unit_directions_ = Line(p1, p2).unit_v

        smooth_point = p2 - unit_directions_ * delta_s

        return True, smooth_point

    @clock
    def get_forward_signals_on_lane(self, lane_id, current_s):
        lane = self.get_lane_by_id(lane_id)
        if lane is None:
            return False, None
        if lane.overlaps is None or len(lane.overlaps) <= 0:
            return False, None
        for i in range(len(lane.overlaps)):
            overlap = lane.overlaps[i]

            stop_line = self.get_stop_line_by_id(overlap.id)
            if stop_line is None or stop_line.traffic_light_id is None or len(stop_line.traffic_light_id) <= 0:
                continue
            stop_line_s = overlap.s_begin
            if current_s < stop_line_s and len(stop_line.traffic_light_id) > 0:
                result = list(stop_line.traffic_light_id)
                return True, result

        return False, None

    @clock
    def find_right_most_successor(self, lane_id):
        lane = self.get_lane_by_id(lane_id)
        if lane is None:
            return False, None
        if lane.successor_id is None or len(lane.successor_id) <= 0:
            return False, None

        successor_endpoints = []
        c_lane_center = lane.centerline
        current_lane_end_point = Point.init_from_other_type(
            c_lane_center.point[-1])
        for i in range(len(lane.successor_id)):
            next_curve = self.get_lane_by_id(lane.successor_id[i])
            if next_curve is None:
                continue
            next_curve_center = next_curve.centerline
            end_point = Point.init_from_other_type(next_curve_center.point[-1])

            successor_endpoints.append(end_point)
            successor_endpoints[i] = successor_endpoints[i] - \
                current_lane_end_point
        rightmost_index = 0
        if len(successor_endpoints) > 1:
            for j in range(1, len(successor_endpoints)):
                if successor_endpoints[j].cross_product(successor_endpoints[rightmost_index]) > 0:
                    rightmost_index = j

        successor_id = lane.successor_id[rightmost_index]
        return True, successor_id

    # @clock
    def get_visible_traffic_lights(self, point, heading):
        max_range = 150
        result = []
        can_get, lane_id, sl = self.get_nearest_lane_with_heading(
            point, heading)
        if not can_get:
            return result
        while not self.get_forward_signals_on_lane(lane_id, sl[0])[0]:
            sl[0] = 0
            center_line = self.get_lane_by_id(lane_id).centerline
            end_point = Point.init_from_other_type(center_line.point[-1])
            if point.distance_to(end_point) > max_range:
                break
            can_find, successor_id = self.find_right_most_successor(lane_id)
            if not can_find:
                break
            lane_id = successor_id
        return self.get_forward_signals_on_lane(lane_id, sl[0])[1]

    def get_forward_lane_id_by_distance(self, lane_id_set, lane, distance):
        if lane is None:
            return lane_id_set
        if distance >= 0:
            successor_id = lane.successor_id
            if successor_id != []:
                for sid in successor_id:
                    lane_id_set.add(sid)
                    succlane = self.get_lane_by_id(sid)
                    if succlane is not None:
                        succdis = distance
                        succdis -= succlane.centerline_s[-1]
                        lane_id_set = self.get_forward_lane_id_by_distance(
                            lane_id_set, succlane, succdis)
        return lane_id_set

    def get_backward_lane_id_by_distance(self, lane_id_set, lane, distance):
        if lane is None:
            return lane_id_set
        if distance <= 0:
            predecessor_id = lane.predecessor_id
            if predecessor_id != []:
                for pid in predecessor_id:
                    lane_id_set.add(pid)
                    prelane = self.get_lane_by_id(pid)
                    if prelane is not None:
                        predis = distance
                        predis += prelane.centerline_s[-1]
                        lane_id_set = self.get_backward_lane_id_by_distance(
                            lane_id_set, prelane, predis)
        return lane_id_set

    @clock
    @check_input_point_type
    def kdtree_search(self, point, k, item_type='LANE'):
        res_tupe = self.all_kdtrees[item_type].query_with_k(point, int(k))
        return res_tupe[-1]
