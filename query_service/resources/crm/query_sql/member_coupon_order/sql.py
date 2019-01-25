ALL = """
    SELECT
        member_no,
        member_name,
        member_mobile,
        member_manage_store_code,
        member_manage_store_name,
        coupon_no,
        CASE coupon_status
            WHEN '7' THEN '有效'
            WHEN '-2' THEN '取消'
            WHEN '0' THEN '未生效'
            WHEN '11' THEN '已使用'
            WHEN '-1' THEN '已过期'
            WHEN '15' THEN '已禁用'
        ELSE NULL END AS coupon_status,
        coupon_batch_time,
        coupon_start_time,
        coupon_end_time,
        coupon_template_no,
        coupon_template_name,
        coupon_type,
        coupon_type_detail,
        coupon_denomination,
        coupon_used_time,
        coupon_used_order_no,
        order_store_code,
        order_store_name,
        CAST(COALESCE(order_retail_amount, 0) AS DECIMAL(18, 2)) AS order_retail_amount,
        CAST(COALESCE(order_fact_amount, 0) AS DECIMAL(18, 2)) AS order_fact_amount,
        CAST(COALESCE(order_fact_amount_include_coupon, 0) AS DECIMAL(18, 2)) AS order_fact_amount_include_coupon,
        CAST(COALESCE(order_discount, 0) AS DECIMAL(18, 2)) AS order_discount,
        CAST(COALESCE(order_item_quantity, 0) AS INTEGER) AS order_item_quantity
    FROM ads_crm.member_coupon_order_info_detail
    WHERE flag = 1
    {condition_sql}
"""

COUPON_DEMONINATION_SUM = """
    SELECT
        outer_order_no,
        coupon_denomination_sum
    FROM cdm_crm.order_coupon_info_detail
    WHERE coupon_category = 'Cash' AND outer_order_no IN ({outer_order_no})
"""