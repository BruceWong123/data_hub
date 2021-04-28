import math
import numpy as np
epsilon = 1e-5


def add_lane_points(pt1, pt2, idx, index, lane_points, lane_info):
    dis = np.sqrt(np.sum((pt1 - pt2) ** 2))
    num = int(dis) >> 3
    n = max(1, num)
    for i in range(n):
        ratio = (i + 0.5) / n
        x = pt1[0] + (pt2[0] - pt1[0]) * ratio
        y = pt1[1] + (pt2[1] - pt1[1]) * ratio
        lane_points.append((x, y))
        lane_info.append((idx, index))


class Point(np.ndarray):
    """docstring for Point"""
    def __new__(cls, x, y):
        obj = np.asarray((x, y), dtype=float).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return

    @classmethod
    def init_from_other_type(cls, point):
        if isinstance(point, list) or isinstance(point, np.ndarray):
            if len(np.array(point).shape) == 2:
                pt = cls(point[0, 0], point[0, 1])
            else:
                pt = cls(point[0], point[1])
        else:
            pt = cls(point.x, point.y)
        return pt

    def norm(self):
        return np.linalg.norm(self)

    def square_distance_to(self, other):
        return np.linalg.norm(self - other) ** 2

    def distance_to(self, other):
        return np.linalg.norm(self - other)

    def inner_product(self, pt):
        return np.dot(self, pt)

    def cross_product(self, pt):
        return np.cross(self, pt)


class Line(object):
    __slots__ = ['s_pt', 'e_pt', 'delta_pt', 'length', 'unit_v']

    def __init__(self, start_pt, end_pt):
        if not isinstance(start_pt, Point):
            raise ValueError()

        if not isinstance(end_pt, Point):
            raise ValueError()

        self.s_pt = start_pt
        self.e_pt = end_pt
        self.delta_pt = self.e_pt - self.s_pt
        self.length = (end_pt - start_pt).norm()
        if self.length < epsilon:
            self.unit_v = Point(0., 0.)
        else:
            self.unit_v = self.delta_pt * (1. / self.length)

    @classmethod
    def init_from_pb(cls, start_pt, end_pt):
        s = Point.init_from_other_type(start_pt)
        e = Point.init_from_other_type(end_pt)
        return cls(s, e)

    def combo_inner_product(self, pt, heading):
        inner_pro = self.unit_v[0] * heading[0] + self.unit_v[1] * heading[1]
        return self.get_mini_square_distance(pt) / ((1.2 + inner_pro) * (1.2 + inner_pro))

    def get_mini_square_distance(self, pt):
        if not isinstance(pt, Point):
            pt = Point.init_from_other_type(pt)
        if self.length < epsilon:
            return pt.square_distance_to(self.s_pt)

        p_to_s = pt - self.s_pt
        inner_pro = self.unit_v.inner_product(p_to_s)
        if inner_pro <= 0:
            return p_to_s.norm() ** 2
        if inner_pro >= self.length:
            return pt.square_distance_to(self.e_pt)

        return p_to_s.cross_product(self.unit_v) ** 2

    def get_sl(self, point):
        if not isinstance(point, Point):
            point = Point.init_from_other_type(point)
        if self.length < epsilon:
            return [0., point.distance_to(self.s_pt)]

        p_to_s = point - self.s_pt
        inner_pro = self.unit_v.inner_product(p_to_s)
        cross_pro = self.unit_v.cross_product(p_to_s)
        if inner_pro <= 0:
            s = 0.
            l = math.copysign(p_to_s.norm(), cross_pro)
            return [s, l]
        if inner_pro >= self.length:
            s = self.length
            l = math.copysign(point.distance_to(self.e_pt), cross_pro)
            return [s, l]
        return [inner_pro, cross_pro]

    def get_nearest_point_on_line(self, point):
        if not isinstance(point, Point):
            point = Point.init_from_other_type(point)
        if self.length < epsilon:
            distance = point.distance_to(self.s_pt)
            return self.s_pt, distance
        p_to_s = point - self.s_pt
        inner_pro = self.unit_v.inner_product(p_to_s)
        if inner_pro <= 0:
            # nearest = Point.init_from_other_type(self.s_pt)
            distance = p_to_s.norm()
            return self.s_pt, distance
        if inner_pro >= self.length:
            distance = self.e_pt.distance_to(point)
            return self.e_pt, distance
        nearest = Point.init_from_other_type(self.s_pt + self.unit_v * inner_pro)
        distance = np.abs(p_to_s.cross_product(self.unit_v))
        return nearest, distance


if __name__ == "__main__":
    a = []
    b = []
    add_lane_points(np.array([10, 20]), np.array([20, 30]), 10, 20, a, b)
    print(a, b)