ALL = {
    'member_no': str,
    'member_name': str,
    'member_mobile': str,
    'member_manage_store_code': str,
    'member_manage_store_name': str,
    'coupon_no': str,
    'coupon_status': str,
    'coupon_batch_time': str,
    'coupon_start_time': str,
    'coupon_end_time': str,
    'coupon_template_no': str,
    'coupon_template_name': str,
    'coupon_type': str,
    'coupon_type_detail': str,
    'coupon_denomination': float,
    'coupon_used_time': str,
    'coupon_used_order_no': str,
    'order_store_code': str,
    'order_store_name': str,
    'order_retail_amount': float,
    'order_fact_amount': float,
    'order_fact_amount_include_coupon': float,
    'order_discount': float,
    'order_item_quantity': int
}

COUPON_DENOMINATION_SUM = {
    'outer_order_no': list,
    'coupon_denomination_sum': float
}