MONTHLY_SALES = """
    SELECT
        brand_code,
        brand_name,
        channel_type,
        mr_member_type AS member_type,
        CASE kpi
            WHEN 'order_fact_amount_with_coupon' THEN '消费金额'
            WHEN 'member_quantity' THEN '会员人数'
            WHEN 'order_quantity' THEN '单数'
            WHEN 'order_item_quantity' THEN '件数'
            WHEN 'order_amount' THEN '吊牌价'
            WHEN 'apt' THEN 'APT'
            WHEN 'upt' THEN 'UPT'
            WHEN 'apu' THEN '件单价'
            WHEN 'order_discount' THEN '折扣'
        ELSE NULL END AS kpi,
        CASE kpi
            WHEN 'order_fact_amount_with_coupon' THEN 1
            WHEN 'member_quantity' THEN 2
            WHEN 'order_quantity' THEN 3
            WHEN 'order_item_quantity' THEN 4
            WHEN 'order_amount' THEN 5
            WHEN 'apt' THEN 6
            WHEN 'upt' THEN 7
            WHEN 'apu' THEN 8
            WHEN 'order_discount' THEN 9
        ELSE NULL END AS kpi_num,
        mtd,
        mtd_tg,
        mtd_tg_rc,
        mtd_ly,
        mtd_ly_cp,
        mtd_lm,
        mtd_lm_cp,
        qtd,
        qtd_tg,
        qtd_tg_rc,
        qtd_ly,
        qtd_ly_cp,
        ytd,
        ytd_tg,
        ytd_tg_rc,
        ytd_ly,
        ytd_ly_cp,
        year_month AS report_time
    FROM ads_crm.monthly_report_sales
    WHERE brand_code IN ({brand_codes})
        AND channel_type IN ({channel_types})
        AND mr_member_type IN ({mr_member_types})
        AND year_month = '{year_month}'
"""

MONTHLY_ASSET = """
    WITH i AS (
        SELECT
            brand_code,
            brand_name,
            member_manage_channel_type                                 AS channel_type,
            member_no,
            CAST(SUM(order_fact_amount_with_coupon) AS DECIMAL(38, 2)) AS consumed_amount
        FROM dws_crm.order_info
        WHERE is_member = 1 AND order_deal_year_month <= '{year_month}'
        GROUP BY brand_code, brand_name, member_manage_channel_type, member_no
    ), j AS (
        SELECT
            mi.brand_code,
            mi.brand_name,
            mi.channel_type,
            mi.member_no,
            CASE
                WHEN mi.member_first_order_time IS NULL OR i.consumed_amount <= 0 THEN -1
                WHEN i.consumed_amount > 0 THEN 1
            ELSE NULL END AS is_consumed
        FROM dwd_crm.member_info mi
        LEFT JOIN i ON mi.brand_code = i.brand_code
            AND mi.brand_name = i.brand_name
            AND mi.channel_type = i.channel_type
            AND mi.member_no = i.member_no
    ), k AS (
        SELECT
            brand_code,
            brand_name,
            channel_type,
            CAST(SUM(IF(is_consumed = 1, is_consumed, 0)) AS INTEGER)    AS consumed_member_quantity,
            CAST(SUM(IF(is_consumed = -1, - is_consumed, 0)) AS INTEGER) AS unconsumed_member_quantity,
            COUNT(member_no)                                             AS member_quantity
        FROM j
        GROUP BY brand_code, brand_name, channel_type
    ), t AS (
        SELECT
            brand_code,
            brand_name,
            channel_type,
            ARRAY[
                'consumed_member_quantity',
                'unconsumed_member_quantity',
                'member_quantity'
            ] AS kpi_key,
            ARRAY[
                consumed_member_quantity,
                unconsumed_member_quantity,
                member_quantity
            ] AS kpi_value,
            CAST(SUBSTR('{year_month}', 1, 4) AS INTEGER) AS year,
            CAST(SUBSTR('{year_month}', 6, 2) AS INTEGER) AS month
        FROM k
    ), sb AS (
        SELECT
            brand_code,
            brand_name,
            channel_type,
            CASE member_type
                WHEN 'unconsumed_member_quantity' THEN CONCAT(channel_type, '注册会员')
                WHEN 'consumed_member_quantity' THEN CONCAT(channel_type, '有消费会员')
                WHEN 'member_quantity' THEN '整体会员'
            ELSE NULL END AS member_type,
            member_quantity,
            year,
            month
        FROM t
        CROSS JOIN UNNEST(kpi_key, kpi_value) AS tt (member_type, member_quantity)
    )
    SELECT
        brand_code,
        brand_name,
        channel_type,
        member_type,
        member_quantity,
        year,
        month
    FROM sb
    WHERE brand_code IN ({brand_codes})
        AND channel_type IN ({channel_types})
        AND member_type IN ({member_types})
"""
