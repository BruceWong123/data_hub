from app.views.traj.load_still import load_is_still
from app.views.traj.load_turn import load_turn
from app.views.traj.load_on_crosswalk import load_is_on_crosswalk
from app.views.traj.load_on_lane import load_is_on_lane
from app.views.traj.load_in_junction import load_is_in_junction
from app.views.traj.load_lane_change import load_is_lane_change
from app.views.deeproute_perception_obstacle_pb2 import PerceptionObstacle


def handle_pedestrain_attribute(obj_id, document_context, points, hdmap):
    if load_is_on_crosswalk(points, hdmap):
        document_context['on_crosswalk'].append(obj_id)


def handle_bicycle_attribute(obj_id, document_context, points, lane_ids, hdmap):
    if load_is_on_crosswalk(points, hdmap):
        document_context['on_crosswalk'].append(obj_id)
    if load_is_on_lane(lane_ids):
        document_context['on_lane'].append(obj_id)
    if load_is_lane_change(lane_ids, hdmap):
        document_context['lane_change'].append(obj_id)


def handle_vehicle_attribute(obj_id, document_context, lane_ids, hdmap):
    if load_is_on_lane(lane_ids):
        document_context['on_lane'].append(obj_id)
    if load_is_lane_change(lane_ids, hdmap):
        document_context['lane_change'].append(obj_id)
    if load_is_in_junction(lane_ids, hdmap):
        document_context['in_junction'].append(obj_id)


def handle_truck_attribute(obj_id, document_context, lane_ids, hdmap):
    handle_vehicle_attribute(obj_id, document_context, lane_ids, hdmap)


def handle_attribute(obj_type, obj_id, document_context, points, lane_ids, hdmap):
    """ An abstract function to handle perception obstacle's attributes

    Args::
        obj_type (PerceptionObstacle.Type._enum_type): the enumerate type of perception object
        obj_id (int): the identity of perception object
        document_context (dict): mongo document in a frame
        points (list): the points belong to a trajectory
        lane_ids (list): the lane ids covered by a trajectory
        hdmap (HDMap): a hdmap object
    """

    # print("points ", points)
    # print("lane ids: ", lane_ids)
    if load_is_still(points):
        document_context['is_still'].append(obj_id)
    if load_turn(points):
        document_context['turn'].append(obj_id)
    if obj_type == PerceptionObstacle.PEDESTRIAN:
        handle_pedestrain_attribute(obj_id, document_context, points, hdmap)
    elif obj_type == PerceptionObstacle.BICYCLE:
        handle_bicycle_attribute(
            obj_id, document_context, points, lane_ids, hdmap)
    elif obj_type == PerceptionObstacle.VEHICLE:
        handle_vehicle_attribute(obj_id, document_context, lane_ids, hdmap)
    elif obj_type == PerceptionObstacle.TRUCK:
        handle_vehicle_attribute(obj_id, document_context, lane_ids, hdmap)
    else:
        print("finish handle")
        return
