STATIC = {
    'brand': str,
    'zone': str,
    'register_member_amount': int,
    'rma_compared_with_ystd': float,
    'consumed_member_amount': int,
    'consumed_member_amount_proportion': float,
    'cma_compared_with_ystd': float,
    'unconsumed_member_amount': int,
    'unconsumed_member_amount_proportion': float
}

NEW_OLD = {
    'brand': str,
    'zone': str,
    'new_member_amount': int,
    'new_member_amount_proportion': float,
    'old_member_amount': int,
    'old_member_amount_proportion': float
}

LEVEL = {
    'brand': str,
    'zone': str,
    'member_level_type': str,
    'member_level_amount': int,
    'member_level_amount_proportion': float
}

REMAIN = {
    'brand': str,
    'zone': str,
    'remain_member_amount': int,
    'remain_member_amount_proportion': float,
    'lost_member_amount': int,
    'lost_member_amount_proportion': float
}

ACTIVE = {
    'brand': str,
    'zone': str,
    'active_member_amount': int,
    'active_member_amount_proportion': float,
    'silent_member_amount': int,
    'silent_member_amount_proportion': float,
    'sleep_member_amount': int,
    'sleep_member_amount_proportion': float,
    'pre_lost_member_amount': int,
    'pre_lost_member_amount_proportion': float
}