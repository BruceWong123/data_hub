def get_is_on_lane(lane_ids, train_seq):
    on_lane_count = 0
    for i in range(min(train_seq, len(lane_ids))):
        lane_id = lane_ids[i]
        if lane_id != -1:
            on_lane_count += 1
    if on_lane_count > int(train_seq / 2):
        return True
    else:
        return False


def load_is_on_lane(lane_ids):
    # todo(jiamiao): move this to config
    train_seq = 20
    return get_is_on_lane(lane_ids, train_seq)