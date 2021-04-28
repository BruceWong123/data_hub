from app.views.traj.data_utils import is_point_in_polygon


def get_is_on_crosswalk(points, hdmap):
    start_idx = 0
    middle_idx = int(len(points) / 2)
    end_idx = len(points)

    flag, crosswalk_id = hdmap.get_nearest_crosswalk(points[middle_idx])
    if not flag:
        return False
    crosswalk = hdmap.get_cross_walk_by_id(crosswalk_id)
    crosswalk_points = crosswalk.polygon.point
    polygon = []
    for point in crosswalk_points:
        polygon.append([point.x, point.y])
    return is_point_in_polygon(polygon[:-1], points[start_idx]) or \
        is_point_in_polygon(polygon[:-1], points[middle_idx]) or \
        is_point_in_polygon(polygon[:-1], points[end_idx-1])


def load_is_on_crosswalk(points, hdmap):
    # todo(jiamiao): move this to config
    return get_is_on_crosswalk(points, hdmap)
