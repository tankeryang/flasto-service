SQL_CRM_TOTAL_INCOME_REPORT_DATA = """
    WITH t1 AS (
        SELECT DISTINCT
            matl.all         AS member_type,
            sm.si            AS si,
            sm.sip           AS sip,
            sm.ca            AS ca,
            sm.oa            AS oa,
            sm.siq           AS siq,
            sm_new_member.oa AS new_oa,
            sm_not_member.oa AS not_oa,
            lyst.si          AS lyst_si
        FROM (
            SELECT DISTINCT
                {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all
            FROM cdm_crm.member_analyse_type_label
        ) matl
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all,
            sum(mab.order_fact_amount) * 1.0 / 10000  AS si,
            100.00                                    AS sip,
            count(distinct mab.member_no)             AS ca,
            count(distinct mab.outer_order_no)        AS oa,
            sum(mab.order_item_quantity)              AS siq
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date('{end_date}')
            AND date(mab.order_deal_time) >= date('{start_date}')
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all
        ) sm
        ON matl.{zone} = sm.{zone}
        AND matl.order_channel = sm.order_channel
        AND matl.sales_mode = sm.sales_mode
        AND matl.store_type = sm.store_type
        AND matl.store_level = sm.store_level
        AND matl.channel_type = sm.channel_type
        AND matl.all = sm.all
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all, member_newold_type,
            count(distinct mab.outer_order_no)  AS oa
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date('{end_date}')
            AND date(mab.order_deal_time) >= date('{start_date}')
            AND member_newold_type = '新会员'
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all, member_newold_type
        ) sm_new_member
        ON matl.{zone} = sm_new_member.{zone}
        AND matl.order_channel = sm_new_member.order_channel
        AND matl.sales_mode = sm_new_member.sales_mode
        AND matl.store_type = sm_new_member.store_type
        AND matl.store_level = sm_new_member.store_level
        AND matl.channel_type = sm_new_member.channel_type
        AND matl.all = sm_new_member.all
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all, member_type,
            count(distinct mab.outer_order_no)  AS oa
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date('{end_date}')
            AND date(mab.order_deal_time) >= date('{start_date}')
            AND member_type = '非会员'
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all, member_type
        ) sm_not_member
        ON matl.{zone} = sm_not_member.{zone}
        AND matl.order_channel = sm_not_member.order_channel
        AND matl.sales_mode = sm_not_member.sales_mode
        AND matl.store_type = sm_not_member.store_type
        AND matl.store_level = sm_not_member.store_level
        AND matl.channel_type = sm_not_member.channel_type
        AND matl.all = sm_not_member.all
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all,
            sum(mab.order_fact_amount) * 1.0 / 10000  AS si
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date(date('{end_date}') - interval '1' year)
            AND date(mab.order_deal_time) >= date(date('{start_date}') - interval '1' year)
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, all
        ) lyst
        ON matl.{zone} = lyst.{zone}
        AND matl.order_channel = lyst.order_channel
        AND matl.sales_mode = lyst.sales_mode
        AND matl.store_type = lyst.store_type
        AND matl.store_level = lyst.store_level
        AND matl.channel_type = lyst.channel_type
        AND matl.all = lyst.all
        
        WHERE matl.{zone} IN ({zones})
        AND matl.order_channel IN ({order_channels})
        AND matl.sales_mode IN ({sales_modes})
        AND matl.store_type IN ({store_types})
        AND matl.store_level IN ({store_levels})
        AND matl.channel_type IN ({channel_types})
    ),
    t2 AS (
        SELECT DISTINCT
            matl2.member_type AS member_type,
            sm2.si            AS si,
            sm2.ca            AS ca,
            sm2.oa            AS oa,
            sm2.siq           AS siq,
            smtt.ttsi         AS ttsi,
            lyst2.si          AS lyst_si
        FROM (
            SELECT DISTINCT
                {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
                FROM cdm_crm.member_analyse_type_label
        ) matl2
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
            sum(mab.order_fact_amount) * 1.0 / 10000                   AS si,
            IF(member_type = '会员', count(distinct mab.member_no), 0) AS ca,
            count(distinct mab.outer_order_no)                         AS oa,
            sum(mab.order_item_quantity)                               AS siq
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date('{end_date}')
            AND date(mab.order_deal_time) >= date('{start_date}')
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
        ) sm2
        ON matl2.{zone} = sm2.{zone}
        AND matl2.order_channel = sm2.order_channel
        AND matl2.sales_mode = sm2.sales_mode
        AND matl2.store_type = sm2.store_type
        AND matl2.store_level = sm2.store_level
        AND matl2.channel_type = sm2.channel_type
        AND matl2.member_type = sm2.member_type
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
            sum(mab.order_fact_amount) * 1.0 / 10000 AS ttsi
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date('{end_date}')
            AND date(mab.order_deal_time) >= date('{start_date}')
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
        ) smtt
        ON matl2.{zone} = smtt.{zone}
        AND matl2.order_channel = smtt.order_channel
        AND matl2.sales_mode = smtt.sales_mode
        AND matl2.store_type = smtt.store_type
        AND matl2.store_level = smtt.store_level
        AND matl2.channel_type = smtt.channel_type
        
        LEFT JOIN (
            SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
            sum(mab.order_fact_amount) * 1.0 / 10000  AS si
            FROM cdm_crm.member_analyse_base mab
            WHERE date(mab.order_deal_time) <= date(date('{end_date}') - interval '1' year)
            AND date(mab.order_deal_time) >= date(date('{start_date}') - interval '1' year)
            GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
        ) lyst2
        ON matl2.{zone} = lyst2.{zone}
        AND matl2.order_channel = lyst2.order_channel
        AND matl2.sales_mode = lyst2.sales_mode
        AND matl2.store_type = lyst2.store_type
        AND matl2.store_level = lyst2.store_level
        AND matl2.channel_type = lyst2.channel_type
        AND matl2.member_type = lyst2.member_type
        
        WHERE matl2.{zone} IN ({zones})
        AND matl2.order_channel IN ({order_channels})
        AND matl2.sales_mode IN ({sales_modes})
        AND matl2.store_type IN ({store_types})
        AND matl2.store_level IN ({store_levels})
        AND matl2.channel_type IN ({channel_types})
    )
    SELECT DISTINCT
        t1.member_type AS member_type,
        cast(COALESCE(SUM(t1.si), 0) AS DECIMAL(10, 3)) AS sales_income,
        cast(COALESCE(AVG(t1.sip), 0) AS DECIMAL(10, 2)) AS sales_income_proportion,
        cast(COALESCE(SUM(t1.ca), 0) AS INTEGER) AS customer_amount,
        cast(COALESCE(SUM(t1.oa), 0) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(SUM(t1.oa) / SUM(t1.ca)), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(SUM(t1.si) * 10000.0 / SUM(t1.oa)), 0) AS DECIMAL(10, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(SUM(t1.si) * 10000.0 / SUM(t1.siq)), 0) AS DECIMAL(10, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(SUM(t1.siq) / SUM(t1.oa)), 0) AS DECIMAL(10, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(SUM(t1.si - t1.lyst_si) * 100.0 / SUM(lyst_si)), 0) AS DECIMAL(10, 2)) AS sales_income_growth,
        cast(COALESCE(TRY(SUM(t1.new_oa) * 100.0 / SUM(t1.new_oa + t1.not_oa)), 0) AS DECIMAL(10, 2)) AS register_proportion
    FROM t1 GROUP BY t1.member_type
    UNION SELECT DISTINCT
        t2.member_type AS member_type,
        cast(COALESCE(SUM(t2.si), 0) AS DECIMAL(10, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t2.si) * 100.0 / SUM(t2.ttsi)), 0) AS DECIMAL(10, 2)) AS sales_income_proportion,
        cast(COALESCE(SUM(t2.ca), 0) AS INTEGER) AS customer_amount,
        cast(COALESCE(SUM(t2.oa), 0) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(SUM(t2.oa) / SUM(t2.ca)), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(SUM(t2.si) * 10000.0 / SUM(t2.oa)), 0) AS DECIMAL(10, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(SUM(t2.si) * 10000.0 / SUM(t2.siq)), 0) AS DECIMAL(10, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(SUM(t2.siq) * 1.0 / SUM(t2.oa)), 0) AS DECIMAL(10, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(SUM(t2.si - t2.lyst_si) * 100.0 / SUM(t2.lyst_si)), 0) AS DECIMAL(10, 2)) AS sales_income_growth,
        cast(SUM(0) AS DECIMAL(10, 2)) AS register_proportion
    FROM t2 GROUP BY t2.member_type
"""
