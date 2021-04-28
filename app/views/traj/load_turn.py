import math

from app.views.traj.data_utils import get_angle_diff


def get_angle(points):
    angle_1 = math.atan2(points[10][1] - points[0]
                         [1], points[10][0] - points[0][0])
    angle_2 = math.atan2(points[-1][1] - points[-10]
                         [1], points[-1][0] - points[-10][0])
    angle_diff = abs(get_angle_diff(angle_1, angle_2))

    distance_1 = math.sqrt((points[10][1] - points[0][1])**2 +
                           (points[10][0] - points[0][0])**2)
    distance_2 = math.sqrt((points[-1][1] - points[-10][1])**2 +
                           (points[-1][0] - points[-10][0])**2)

    if distance_1 < 1.0 or distance_2 < 1.0:
        return 0.0

    return angle_diff


def load_turn(points):
    # todo(jiamiao): move this to config
    turn_thresh = 0.15
    angle = get_angle(points)
    if angle < turn_thresh:
        return False
    else:
        return True
