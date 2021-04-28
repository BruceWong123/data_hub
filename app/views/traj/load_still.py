import math


def get_speed(points, train_seq):
    time_interval = min(len(points), train_seq) * 0.1
    distance = math.sqrt((points[min(len(points), train_seq) - 1][0] - points[0][0]) ** 2 +
                         (points[min(len(points), train_seq) - 1][1] - points[0][1]) ** 2)
    speed = distance / time_interval
    return speed


def load_is_still(points):
    # todo(jiamiao): move this to config
    speed_thresh = 0.2
    train_seq = 20
    speed = get_speed(points, train_seq)
    if speed < speed_thresh:
        return True
    else:
        return False
