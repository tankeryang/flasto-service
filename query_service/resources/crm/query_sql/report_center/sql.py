# TODO: 日报改多品牌，member_type 字段需要调整

DAILY = """
    SELECT DISTINCT
        {cmail_sales_area} AS sales_area,
        {cmail_city} AS city,
        {cmail_store_code} AS store_code,
        cmail.dr_member_type AS member_type,
        cast(COALESCE(sm.sa, 0) AS DECIMAL(18, 2)) AS sales_amount,
        cast(COALESCE(TRY(sm.sa * 1.0000 / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion,
        cast(COALESCE(TRY(sm_mb_tt.sa * 1.0000 / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion_total,
        cast(COALESCE(lyst.sa, 0) AS DECIMAL(18, 2)) AS last_year_same_time_sales_amount,
        cast(COALESCE(TRY((sm.sa - lyst.sa) * 1.0000 / lyst.sa), 0) AS DECIMAL(18, 4)) AS like_for_like_sales_growth,
        cast(COALESCE(sm.siq, 0) AS INTEGER) AS sales_item_quantity,
        cast(COALESCE(TRY(sm.sa * 1.0000 / sm.ra), 0) AS DECIMAL(18, 2)) AS discount_rate,
        cast(COALESCE(sm.ma, 0) AS INTEGER) AS member_amount,
        cast(COALESCE(lmr.ma, 0) AS INTEGER) AS past_12_month_remain_member_amount,
        cast(COALESCE(TRY(sm.ma * 1.0000 / lmr.ma), 0) AS DECIMAL(18, 4)) AS second_trade_rate,
        cast(COALESCE(new_vip.ma, 0) AS INTEGER) AS new_vip_member_amount,
        cast(COALESCE(new_normal.ma, 0) AS INTEGER) AS new_normal_member_amount,
        cast(COALESCE(ugm.ma, 0) AS INTEGER) AS upgraded_member_amount,
        cast(COALESCE(stm.sa, 0) AS INTEGER) AS store_amount,
        cast(COALESCE(TRY(sm.ma * 1.00 / stm.sa), 0) AS DECIMAL(18, 2)) AS member_amount_per_store,
        cast(COALESCE(TRY(sm.sa * 1.00 /sm.ma), 0) AS DECIMAL(18, 2)) AS sales_amount_per_member,
        cast(COALESCE(TRY(sm.siq * 1.00 / sm.ma), 0) AS DECIMAL(18, 2)) AS sales_item_quantity_per_member,
        cast(COALESCE(TRY(sm.siq * 1.00 / sm.oa), 0) AS DECIMAL(18, 2)) AS su_per_member,
        cast(COALESCE(TRY(sm.oa * 1.00 / sm.ma), 0) AS DECIMAL(18, 2)) AS order_amount_per_member
    FROM (
        SELECT DISTINCT {zone_index}, dr_member_type
        FROM cdm_crm.member_analyse_index_label
        WHERE dr_member_type != '非会员'
        AND {zone} IN ({zones})) cmail

    LEFT JOIN (
        SELECT coid.{zone}, coid.dr_member_type,
        sum(coid.order_fact_amount_include_coupon) AS sa,
        sum(coid.order_amount)                     AS ra,
        sum(coid.order_type_num)                   AS oa,
        sum(coid.order_item_quantity)              AS siq,
        count(distinct coid.member_no)             AS ma
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        AND coid.channel_type IN ({channel_types})
        GROUP BY coid.{zone}, coid.dr_member_type
    ) sm
    ON cmail.{zone} = sm.{zone}
    AND cmail.channel_type = sm.channel_type
    AND cmail.dr_member_type = sm.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone},
        sum(coid.order_fact_amount) AS sa
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        AND coid.channel_type IN ({channel_types})
        GROUP BY coid.{zone}
    ) sm_tt
    ON cmail.{zone} = sm_tt.{zone}
    AND cmail.channel_type = sm_tt.channel_type

    LEFT JOIN (
        SELECT coid.{zone},
        sum(coid.order_fact_amount) AS sa
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.dr_member_type != '非会员'
        AND coid.brand_code = '{brand_code}'
        AND coid.channel_type IN ({channel_types})
        GROUP BY coid.{zone}
    ) sm_mb_tt
    ON cmail.{zone} = sm_mb_tt.{zone}
    AND cmail.channel_type = sm_mb_tt.channel_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type, coid.dr_member_type,
        sum(coid.order_fact_amount) AS sa
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE date(coid.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(coid.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type, coid.dr_member_type
    ) lyst
    ON cmail.{zone} = lyst.{zone}
    AND cmail.channel_type = lyst.channel_type
    AND cmail.dr_member_type = lyst.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type, coid.dr_member_type,
        count(distinct coid.member_no) AS ma
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE coid.dr_member_type IN ('普通会员', 'VIP会员')
        AND date(coid.order_deal_time) <= date(date('{start_date}') - interval '1' day)
        AND date(coid.order_deal_time) >= date(date('{start_date}') - interval '12' month)
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type, coid.dr_member_type
    ) lmr
    ON cmail.{zone} = lmr.{zone}
    AND cmail.channel_type = lmr.channel_type
    AND cmail.dr_member_type = lmr.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type, coid.dr_member_type,
        count(distinct coid.member_no) AS ma
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE coid.dr_member_type = '新会员'
        AND date(coid.member_register_time) = date(coid.order_deal_time)
        AND coid.last_grade_change_time IS NOT NULL
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type, coid.dr_member_type
    ) new_vip
    ON cmail.{zone} = new_vip.{zone}
    AND cmail.channel_type = new_vip.channel_type
    AND cmail.dr_member_type = new_vip.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type, coid.dr_member_type,
        count(distinct coid.member_no) AS ma
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE coid.dr_member_type = '新会员'
        AND coid.last_grade_change_time IS NULL
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type, coid.dr_member_type
    ) new_normal
    ON cmail.{zone} = new_normal.{zone}
    AND cmail.channel_type = new_normal.channel_type
    AND cmail.dr_member_type = new_normal.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type, coid.dr_member_type,
        count(distinct coid.member_no) AS ma
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE coid.dr_member_type IN ('新会员', '普通会员')
        AND date(coid.last_grade_change_time) = date(coid.order_deal_time)
        AND date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type, coid.dr_member_type
    ) ugm
    ON cmail.{zone} = ugm.{zone}
    AND cmail.channel_type = ugm.channel_type
    AND cmail.dr_member_type = ugm.dr_member_type

    LEFT JOIN (
        SELECT coid.{zone}, coid.channel_type,
        count(distinct coid.store_code) AS sa
        FROM cdm_crm.order_info_detail coid
        INNER JOIN cdm_crm.member_info_detail mid
        ON coid.store_code = mid.store_code
        WHERE date(coid.order_deal_time) <= date('{end_date}')
        AND date(coid.order_deal_time) >= date('{start_date}')
        AND coid.brand_code = '{brand_code}'
        GROUP BY coid.{zone}, coid.channel_type
    ) stm
    ON cmail.{zone} = stm.{zone}
    AND cmail.channel_type = stm.channel_type
"""