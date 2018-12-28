# TODO: 日报改多品牌，member_type 字段需要调整

DAILY = """
    WITH cmail AS (
        SELECT DISTINCT {zone_index}, dr_member_type
        FROM cdm_crm.member_analyse_index_label
    ), sm AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(sum(coid.order_fact_amount_include_coupon) AS DECIMAL(18, 4)) AS sa,
        cast(sum(coid.order_amount) AS DECIMAL(18, 4))                     AS ra,
        cast(sum(coid.order_type_num) AS DECIMAL(18, 4))                   AS oa,
        cast(sum(coid.order_item_quantity) AS DECIMAL(18, 4))              AS siq,
        cast(count(distinct coid.member_no) AS DECIMAL(18, 4))             AS ma
        FROM cdm_crm.order_info_detail coid
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), sm_tt AS (
        SELECT coid.{zone},
        cast(sum(coid.order_fact_amount_include_coupon) AS DECIMAL(18, 4)) AS sa
        FROM cdm_crm.order_info_detail coid
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}
    ), sm_mb_tt AS (
        SELECT coid.{zone},
        cast(sum(coid.order_fact_amount_include_coupon) AS DECIMAL(18, 4)) AS sa
        FROM cdm_crm.order_info_detail coid
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.dr_member_type != '非会员'
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}
    ), lyst AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(sum(coid.order_fact_amount_include_coupon) AS DECIMAL(18, 4)) AS sa
        FROM cdm_crm.order_info_detail coid
        WHERE date(coid.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(coid.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), lmr AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(count(distinct coid.member_no) AS DECIMAL(18, 4)) AS ma
        FROM cdm_crm.order_info_detail coid
        WHERE coid.dr_member_type IN ('普通会员', 'VIP会员')
        AND date(coid.order_deal_time) <= date(date('{start_date}') - interval '1' day)
        AND date(coid.order_deal_time) >= date(date('{start_date}') - interval '12' month)
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), new_vip AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(count(distinct coid.member_no) AS DECIMAL(18, 4)) AS ma
        FROM cdm_crm.order_info_detail coid
        WHERE coid.dr_member_type = '新会员'
        AND date(coid.member_register_time) = date(coid.order_deal_time)
        AND coid.last_grade_change_time IS NOT NULL
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), new_normal AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(count(distinct coid.member_no) AS DECIMAL(18, 4)) AS ma
        FROM cdm_crm.order_info_detail coid
        WHERE coid.dr_member_type = '新会员'
        AND coid.last_grade_change_time IS NULL
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), ugm AS (
        SELECT coid.{zone}, coid.dr_member_type,
        cast(count(distinct coid.member_no) AS DECIMAL(18, 4)) AS ma
        FROM cdm_crm.order_info_detail coid
        WHERE coid.dr_member_type IN ('新会员', '普通会员')
        AND date(coid.last_grade_change_time) = date(coid.order_deal_time)
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}, coid.dr_member_type
    ), stm AS (
        SELECT coid.{zone},
        cast(count(distinct coid.store_code) AS DECIMAL(18, 4)) AS sa
        FROM cdm_crm.order_info_detail coid
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '2'
        AND coid.channel_type = '自营'
        GROUP BY coid.{zone}
    )
    SELECT DISTINCT
        {cmail_sales_area} AS sales_area,
        CASE {cmail_sales_area}
            WHEN '东北' THEN 1
            WHEN '华北' THEN 2
            WHEN '华东' THEN 3
            WHEN '华南' THEN 4
            WHEN '华中' THEN 5
            WHEN '西北' THEN 6
        ELSE NULL END AS sales_area_num,
        {cmail_city} AS city,
        {cmail_store_code} AS store_code,
        cmail.dr_member_type AS member_type,
        CASE cmail.dr_member_type
            WHEN '新会员' THEN 1
            WHEN '普通会员' THEN 2
            WHEN 'VIP会员' THEN 3
        ELSE NULL END AS member_type_num,
        cast(COALESCE(sm.sa, 0) AS DECIMAL(18, 2)) AS sales_amount,
        cast(COALESCE(TRY(sm.sa / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion,
        cast(COALESCE(TRY(sm_mb_tt.sa / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion_total,
        cast(COALESCE(lyst.sa, 0) AS DECIMAL(18, 2)) AS last_year_same_time_sales_amount,
        cast(COALESCE(TRY((sm.sa - lyst.sa) / lyst.sa), 0) AS DECIMAL(18, 4)) AS like_for_like_sales_growth,
        cast(COALESCE(sm.siq, 0) AS INTEGER) AS sales_item_quantity,
        cast(COALESCE(TRY(sm.sa / sm.ra), 0) AS DECIMAL(18, 2)) AS discount_rate,
        cast(COALESCE(sm.ma, 0) AS INTEGER) AS member_amount,
        cast(COALESCE(lmr.ma, 0) AS INTEGER) AS past_12_month_remain_member_amount,
        cast(COALESCE(TRY(sm.ma / lmr.ma), 0) AS DECIMAL(18, 4)) AS second_trade_rate,
        cast(COALESCE(new_vip.ma, 0) AS INTEGER) AS new_vip_member_amount,
        cast(COALESCE(new_normal.ma, 0) AS INTEGER) AS new_normal_member_amount,
        cast(COALESCE(ugm.ma, 0) AS INTEGER) AS upgraded_member_amount,
        cast(COALESCE(stm.sa, 0) AS INTEGER) AS store_amount,
        cast(COALESCE(TRY(sm.ma / stm.sa), 0) AS DECIMAL(18, 2)) AS member_amount_per_store,
        cast(COALESCE(TRY(sm.sa / sm.ma), 0) AS DECIMAL(18, 2)) AS sales_amount_per_member,
        cast(COALESCE(TRY(sm.siq / sm.ma), 0) AS DECIMAL(18, 2)) AS sales_item_quantity_per_member,
        cast(COALESCE(TRY(sm.siq / sm.oa), 0) AS DECIMAL(18, 2)) AS su_per_member,
        cast(COALESCE(TRY(sm.oa / sm.ma), 0) AS DECIMAL(18, 2)) AS order_amount_per_member
    FROM cmail
    LEFT JOIN sm ON cmail.{zone} = sm.{zone}
        AND cmail.dr_member_type = sm.dr_member_type
    LEFT JOIN sm_tt ON cmail.{zone} = sm_tt.{zone}
    LEFT JOIN sm_mb_tt ON cmail.{zone} = sm_mb_tt.{zone}
    LEFT JOIN lyst ON cmail.{zone} = lyst.{zone}
        AND cmail.dr_member_type = lyst.dr_member_type
    LEFT JOIN lmr ON cmail.{zone} = lmr.{zone}
        AND cmail.dr_member_type = lmr.dr_member_type
    LEFT JOIN new_vip ON cmail.{zone} = new_vip.{zone}
        AND cmail.dr_member_type = new_vip.dr_member_type
    LEFT JOIN new_normal ON cmail.{zone} = new_normal.{zone}
        AND cmail.dr_member_type = new_normal.dr_member_type
    LEFT JOIN ugm ON cmail.{zone} = ugm.{zone}
        AND cmail.dr_member_type = ugm.dr_member_type
    LEFT JOIN stm ON cmail.{zone} = stm.{zone}
    WHERE cmail.dr_member_type != '非会员' AND cmail.{zone} IN ({zones})
"""