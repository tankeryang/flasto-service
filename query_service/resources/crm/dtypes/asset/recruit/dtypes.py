STATIC = {
    'brand': str,
    'zone': list,
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
    'zone': list,
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
    'zone': list,
    'register_member_amount': int,
    'rma_compared_with_lyst': float,
    'consumed_member_amount': int,
    'consumed_member_amount_proportion': float,
    'cma_compared_with_lyst': float,
    'unconsumed_member_amount': int,
    'unconsumed_member_amount_proportion': float,
    'uma_compared_with_lyst': float,
    'year_month': str
}

CONSUMED_DAILY = {
    'brand': str,
    'zone': list,
    'member_recruit_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'date': str
}

CONSUMED_MONTHLY = {
    'brand': str,
    'zone': list,
    'member_recruit_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'year_month': str
}

UNCONSUMED_DAILY = {
    'brand': str,
    'zone': list,
    'member_register_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'date': str
}

UNCONSUMED_MONTHLY = {
    'brand': str,
    'zone': list,
    'member_register_type': str,
    'member_amount': int,
    'member_amount_proportion': float,
    'year_month': str
}