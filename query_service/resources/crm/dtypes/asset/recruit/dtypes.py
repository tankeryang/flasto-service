STATIC = {
    'brand': str,
    'zone': str,
    'register_member_amount': int,
    'rma_compared_with_lyst': float,
    'consumed_member_amount': int,
    'consumed_member_amount_proportion': float,
    'cma_compared_with_lyst': float,
    'unconsumed_member_amount': int,
    'unconsumed_member_amount_proportion': float,
    'uma_compared_with_lyst': float
}

DAILY = {
    'brand': str,
    'zone': str,
    'register_member_amount': int,
    'rma_compared_with_lyst': float,
    'consumed_member_amount': int,
    'consumed_member_amount_proportion': float,
    'cma_compared_with_lyst': float,
    'unconsumed_member_amount': int,
    'unconsumed_member_amount_proportion': float,
    'uma_compared_with_lyst': float,
    'date': str
}

MONTHLY = {
    'brand': str,
    'zone': str,
    'register_member_amount': int,
    'rma_compared_with_lyst': float,
    'consumed_member_amount': int,
    'consumed_member_amount_proportion': float,
    'cma_compared_with_lyst': float,
    'unconsumed_member_amount': int,
    'unconsumed_member_amount_proportion': float,
    'uma_compared_with_lyst': float,
    'year': str,
    'month': str
}

CONSUMED_DAILY = {
    'brand': str,
    'zone': str,
    'member_recruit_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'date': str
}

UNCONSUMED_DAILY = {
    'brand': str,
    'zone': str,
    'member_register_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'date': str
}