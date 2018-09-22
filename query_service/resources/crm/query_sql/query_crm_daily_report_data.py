SQL_CRM_DAILY_REPORT_DATA = """
    SELECT DISTINCT
        {mtl_sales_area} AS sales_area,
        {mtl_city} AS city,
        {mtl_store_code} AS store_code,
        mtl.member_type AS member_type,
        cast(COALESCE(sm.sa, 0) AS DECIMAL(18, 2)) AS sales_amount,
        cast(COALESCE(TRY(sm.sa * 1.0 / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion,
        cast(COALESCE(TRY(sm_mb_tt.sa * 1.0 / sm_tt.sa), 0) AS DECIMAL(18, 4)) AS sales_amount_proportion_total,
        cast(COALESCE(lyst.sa, 0) AS DECIMAL(18, 2)) AS last_year_same_time_sales_amount,
        cast(COALESCE(TRY((sm.sa - lyst.sa) * 1.0 / lyst.sa), 0) AS DECIMAL(18, 4)) AS like_for_like_sales_growth,
        cast(COALESCE(sm.siq, 0) AS INTEGER) AS sales_item_quantity,
        cast(COALESCE(TRY(sm.sa * 1.0 / sm.ra), 0) AS DECIMAL(18, 2)) AS discount_rate,
        cast(COALESCE(sm.ma, 0) AS INTEGER) AS member_amount,
        cast(COALESCE(lmr.ma, 0) AS INTEGER) AS past_12_month_remain_member_amount,
        cast(COALESCE(TRY(sm.ma * 1.0 / lmr.ma), 0) AS DECIMAL(18, 4)) AS second_trade_rate,
        cast(COALESCE(new_vip.ma, 0) AS INTEGER) AS new_vip_member_amount,
        cast(COALESCE(new_normal.ma, 0) AS INTEGER) AS new_normal_member_amount,
        cast(COALESCE(ugm.ma, 0) AS INTEGER) AS upgraded_member_amount,
        cast(COALESCE(stm.sa, 0) AS INTEGER) AS store_amount,
        cast(COALESCE(TRY(sm.ma * 1.0 / stm.sa), 0) AS DECIMAL(18, 2)) AS member_amount_per_store,
        cast(COALESCE(TRY(sm.sa * 1.0 /sm.ma), 0) AS DECIMAL(18, 2)) AS sales_amount_per_member,
        cast(COALESCE(TRY(sm.siq * 1.0 / sm.ma), 0) AS DECIMAL(18, 2)) AS sales_item_quantity_per_member,
        cast(COALESCE(TRY(sm.siq * 1.0 / sm.oa), 0) AS DECIMAL(18, 2)) AS su_per_member,
        cast(COALESCE(TRY(sm.oa * 1.0 / sm.ma), 0) AS DECIMAL(18, 2)) AS order_amount_per_member
    FROM (
        SELECT DISTINCT {zone_index}, member_type
        FROM cdm_crm.member_type_label
    ) mtl

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        sum(drb.order_fact_amount)         AS sa,
        sum(drb.order_amount)              AS ra,
        count(distinct drb.outer_order_no) AS oa,
        sum(drb.order_item_quantity)       AS siq,
        count(distinct drb.member_no)      AS ma
        FROM cdm_crm.daliy_report_base drb
        WHERE date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}, drb.member_type
    ) sm
    ON mtl.{zone} = sm.{zone}
    AND mtl.member_type = sm.member_type

    LEFT JOIN (
        SELECT drb.{zone},
        sum(drb.order_fact_amount) AS sa
        FROM cdm_crm.daliy_report_base drb
        WHERE date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}
    ) sm_tt
    ON mtl.{zone} = sm_tt.{zone}

    LEFT JOIN (
        SELECT drb.{zone},
        sum(drb.order_fact_amount) AS sa
        FROM cdm_crm.daliy_report_base drb
        WHERE date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        AND drb.member_type != '非会员'
        GROUP BY drb.{zone}
    ) sm_mb_tt
    ON mtl.{zone} = sm_mb_tt.{zone}

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        sum(drb.order_fact_amount) AS sa
        FROM cdm_crm.daliy_report_base drb
        WHERE date(drb.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(drb.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        GROUP BY drb.{zone}, drb.member_type
    ) lyst
    ON mtl.{zone} = lyst.{zone}
    AND mtl.member_type = lyst.member_type

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        count(distinct drb.member_no) AS ma
        FROM cdm_crm.daliy_report_base drb
        WHERE drb.member_type IN ('普通会员', 'VIP会员')
        AND date(drb.order_deal_time) <= date(date('{start_date}') - interval '1' day)
        AND date(drb.order_deal_time) >= date(date('{start_date}') - interval '12' month)
        GROUP BY drb.{zone}, drb.member_type
    ) lmr
    ON mtl.{zone} = lmr.{zone}
    AND mtl.member_type = lmr.member_type

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        count(distinct drb.member_no) AS ma
        FROM cdm_crm.daliy_report_base drb
        WHERE drb.member_type = '新会员'
        AND date(drb.member_register_time) = date(drb.order_deal_time)
        AND drb.last_grade_change_time IS NOT NULL
        AND date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}, drb.member_type
    ) new_vip
    ON mtl.{zone} = new_vip.{zone}
    AND mtl.member_type = new_vip.member_type

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        count(distinct drb.member_no) AS ma
        FROM cdm_crm.daliy_report_base drb
        WHERE drb.member_type = '新会员'
        AND drb.last_grade_change_time IS NULL
        AND date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}, drb.member_type
    ) new_normal
    ON mtl.{zone} = new_normal.{zone}
    AND mtl.member_type = new_normal.member_type

    LEFT JOIN (
        SELECT drb.{zone}, drb.member_type,
        count(distinct drb.member_no) AS ma
        FROM cdm_crm.daliy_report_base drb
        WHERE drb.member_type IN ('新会员', '普通会员')
        AND date(drb.last_grade_change_time) = date(drb.order_deal_time)
        AND date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}, drb.member_type
    ) ugm
    ON mtl.{zone} = ugm.{zone}
    AND mtl.member_type = ugm.member_type

    LEFT JOIN (
        SELECT drb.{zone},
        count(distinct drb.store_code) AS sa
        FROM cdm_crm.daliy_report_base drb
        WHERE date(drb.order_deal_time) <= date('{end_date}')
        AND date(drb.order_deal_time) >= date('{start_date}')
        GROUP BY drb.{zone}
    ) stm
    ON mtl.{zone} = stm.{zone}

    WHERE mtl.member_type != '非会员'
    AND mtl.{zone} IN ({zones})
"""