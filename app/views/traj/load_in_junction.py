from app.views.map_overlap_pb2 import Overlap


def get_is_in_junction(lane_ids, hdmap):
    start_idx = 0
    middle_idx = int(len(lane_ids) / 2)
    end_idx = len(lane_ids)
    idxes = [start_idx, middle_idx, end_idx-1]

    for idx in idxes:
        lane_id = lane_ids[idx]
        if lane_id == -1:
            continue
        lane = hdmap.get_lane_by_id(lane_id)
        if lane == None:
            continue
        overlaps = lane.overlaps
        for overlap in overlaps:
            if overlap.type == Overlap.JUNCTION:
                return True
    return False


def load_is_in_junction(lane_ids, hdmap):
    # todo(jiamiao): move this to config
    return get_is_in_junction(lane_ids, hdmap)
