def get_is_lane_change(lane_ids, begin_idx, end_idx, hdmap):
    if begin_idx >= len(lane_ids):
        return False
    begin_idx = max(begin_idx, 0)
    end_idx = min(end_idx, len(lane_ids))

    for i in range(begin_idx, end_idx-1):
        if lane_ids[i] == -1:
            return False
        lane = hdmap.get_lane_by_id(lane_ids[i])
        if lane == None:
            print("fail to find lane with lane_id: ", lane_ids[i])
            continue
        successor_ids = lane.successor_id
        predecessor_ids = lane.predecessor_id
        overlaps = lane.overlaps
        successor_ids.append(lane_ids[i])
        successor_ids.extend(predecessor_ids)
        for overlap in overlaps:    
            successor_ids.append(overlap.id)

        if lane_ids[i+1] not in successor_ids:
            return True
    return False


def load_is_lane_change(lane_ids, hdmap):
    # todo(jiamiao): move this to config
    begin_idx = 20
    end_idx = 50
    return get_is_lane_change(lane_ids, begin_idx, end_idx, hdmap)