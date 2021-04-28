import math
import numpy as np


def check_dr_data_continous(trajectory):
    timestamp_list = []
    for point in trajectory:
        timestamp_list.append(point[0])
    for i in range(1, len(timestamp_list)):
        pre = timestamp_list[i-1]
        cur = timestamp_list[i]
        if cur - pre != 100000:
            return False
    return True


def get_angle_diff(angle_1, angle_2):
    angle = angle_2 - angle_1
    angle = angle + math.pi

    while angle >= 0:
        angle -= math.pi * 2
    while angle < 0:
        angle += math.pi * 2
    return angle - math.pi
    

def trajectory_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] < target:
            low = mid + 1
        elif arr[mid][0] > target:
            high = mid - 1
        else:
            return mid
    return -1


def points_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.sqrt(np.sum((point1 - point2)**2))


def point2seg_distance(seg_point1, seg_point2, point):
    seg_point1 = np.array(seg_point1)
    seg_point2 = np.array(seg_point2)
    point = np.array(point)

    distance = points_distance(seg_point1, seg_point2)

    if distance < 1e-6:
        return points_distance(seg_point1, point)
    else:
        cross_val = np.cross((seg_point2-seg_point1), (point-seg_point1))
        lateral = abs(cross_val/distance)
        sign = (seg_point2-seg_point1).dot((point-seg_point1)) * (seg_point1-seg_point2).dot((point-seg_point2))
        if sign < 0 and sign < -0.01:
            lateral = 1e9
        return lateral


def point2line_distance(point, line):
    point1 = np.array(line[0])
    point2 = np.array(line[1])
    point = np.array(point)

    line_distance = points_distance(point1, point2)
    if line_distance < 1e-6:
        return points_distance(point1, point)

    cross_val = np.cross((point2 - point1), (point - point1))
    lateral = abs(cross_val / line_distance)
    return lateral


def is_point_in_polygon(polygon, point):
    if len(polygon) < 3:
        return False

    covered = False
    j = 0
    i = j + 1
    while i < len(polygon):
        point_i = polygon[i]
        point_j = polygon[j]
        if ((point_i[1] > point[1]) != (point_j[1] > point[1])) and \
                (point[0] < (point_j[0] - point_i[0]) * (point[1] - point_i[1])
                 / (point_j[1] - point_i[1]) + point_i[0]):
            covered = not covered
        i += 1
        j += 1
    return covered