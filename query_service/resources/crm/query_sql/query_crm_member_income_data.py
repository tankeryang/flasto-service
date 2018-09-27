SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA = """
    WITH coid AS (
        SELECT DISTINCT
            t_.brand_name,
            t_.{zone},
            t_.order_channel,
            t_.brand_code,
            t_.store_code,
            t_.sales_mode,
            t_.store_type,
            t_.store_level,
            t_.channel_type,
            t_.outer_order_no,
            t_.member_no,
            t_.member_grade_id,
            t_.member_type,
            _t.member_nowbefore_type,
            t_.order_item_quantity,
            t_.order_amount,
            t_.order_fact_amount,
            t_.member_register_time,
            t_.last_grade_change_time,
            t_.order_deal_time
        FROM cdm_common.crm_order_info_detail t_
        LEFT JOIN (
            SELECT DISTINCT date(member_register_time) member_register_date,
            IF( year(member_register_time) = year(date('{end_date}')),
                IF(month(member_register_time) = month(date('{end_date}')), '当月会员', '当年会员'),
                IF(year(member_register_time) < year(date('{end_date}')), '往年会员', NULL)) member_nowbefore_type
            FROM cdm_common.crm_order_info_detail ) _t
        ON date(t_.member_register_time) = _t.member_register_date
        WHERE t_.member_type = '会员' AND date(t_.order_deal_time) <= date('{end_date}')
    ), t1 AS (
        SELECT DISTINCT
            cmail.brand_name  AS brand,
            cmail.{zone}      AS zone,
            cmail.member_type AS member_type,
            sm.si             AS si,
            sm.ca             AS ca,
            sm.oa             AS oa,
            sm.siq            AS siq,
            smtt.ttsi         AS ttsi
        FROM (
            SELECT DISTINCT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
            FROM cdm_common.crm_member_analyse_index_label
            WHERE member_type = '会员' ) cmail
        LEFT JOIN (
            SELECT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
            sum(coid.order_fact_amount) * 1.0   AS si,
            count(distinct coid.member_no)      AS ca,
            count(distinct coid.outer_order_no) AS oa,
            sum(coid.order_item_quantity)       AS siq
            FROM coid
            WHERE date(coid.order_deal_time) <= date('{end_date}')
            AND date(coid.order_deal_time) >= date('{start_date}')
            GROUP BY brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type) sm
        ON cmail.brand_name = sm.brand_name
        AND cmail.{zone} = sm.{zone}
        AND cmail.order_channel = sm.order_channel
        AND cmail.sales_mode = sm.sales_mode
        AND cmail.store_type = sm.store_type
        AND cmail.store_level = sm.store_level
        AND cmail.channel_type = sm.channel_type
        AND cmail.member_type = sm.member_type
        LEFT JOIN (
            SELECT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
            sum(coid.order_fact_amount) * 1.0 AS ttsi
            FROM coid
            WHERE date(coid.order_deal_time) <= date('{end_date}')
            AND date(coid.order_deal_time) >= date('{start_date}')
            GROUP BY brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type) smtt
        ON cmail.brand_name = smtt.brand_name
        AND cmail.{zone} = smtt.{zone}
        AND cmail.order_channel = smtt.order_channel
        AND cmail.sales_mode = smtt.sales_mode
        AND cmail.store_type = smtt.store_type
        AND cmail.store_level = smtt.store_level
        AND cmail.channel_type = smtt.channel_type
        WHERE cmail.brand_name IN ({brands})
        AND cmail.{zone} IN ({zones})
        AND cmail.order_channel IN ({order_channels})
        AND cmail.sales_mode IN ({sales_modes})
        AND cmail.store_type IN ({store_types})
        AND cmail.store_level IN ({store_levels})
        AND cmail.channel_type IN ({channel_types})
    ), t2 AS (
        SELECT DISTINCT
            cmail2.brand_name            AS brand,
            cmail2.{zone}                AS zone,
            cmail2.member_nowbefore_type AS member_type,
            sm2.si                       AS si,
            sm2.ca                       AS ca,
            sm2.oa                       AS oa,
            sm2.siq                      AS siq,
            smtt2.ttsi                   AS ttsi
        FROM (
            SELECT DISTINCT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type
            FROM cdm_common.crm_member_analyse_index_label
            WHERE member_type = '会员') cmail2
        LEFT JOIN (
            SELECT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type,
            sum(coid.order_fact_amount) * 1.0   AS si,
            count(distinct member_no)           AS ca,
            count(distinct coid.outer_order_no) AS oa,
            sum(coid.order_item_quantity)       AS siq
            FROM coid
            WHERE date(coid.order_deal_time) <= date('{end_date}')
            AND date(coid.order_deal_time) >= date('{start_date}')
            GROUP BY brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type) sm2
        ON cmail2.brand_name = sm2.brand_name
        AND cmail2.{zone} = sm2.{zone}
        AND cmail2.order_channel = sm2.order_channel
        AND cmail2.sales_mode = sm2.sales_mode
        AND cmail2.store_type = sm2.store_type
        AND cmail2.store_level = sm2.store_level
        AND cmail2.channel_type = sm2.channel_type
        AND cmail2.member_nowbefore_type = sm2.member_nowbefore_type
        LEFT JOIN (
            SELECT brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
            sum(coid.order_fact_amount) * 1.0 AS ttsi
            FROM coid
            WHERE date(coid.order_deal_time) <= date('{end_date}')
            AND date(coid.order_deal_time) >= date('{start_date}')
            GROUP BY brand_name, {zone}, order_channel, sales_mode, store_type, store_level, channel_type) smtt2
        ON cmail2.brand_name = smtt2.brand_name
        AND cmail2.{zone} = smtt2.{zone}
        AND cmail2.order_channel = smtt2.order_channel
        AND cmail2.sales_mode = smtt2.sales_mode
        AND cmail2.store_type = smtt2.store_type
        AND cmail2.store_level = smtt2.store_level
        AND cmail2.channel_type = smtt2.channel_type
        WHERE cmail2.brand_name IN ({brands})
        AND cmail2.{zone} IN ({zones})
        AND cmail2.order_channel IN ({order_channels})
        AND cmail2.sales_mode IN ({sales_modes})
        AND cmail2.store_type IN ({store_types})
        AND cmail2.store_level IN ({store_levels})
        AND cmail2.channel_type IN ({channel_types})
    )
    SELECT DISTINCT
        t1.brand       AS brand,
        t1.zone        AS zone,
        t1.member_type AS member_type,
        cast(COALESCE(SUM(t1.si), 0) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t1.si) / SUM(t1.ttsi)), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(COALESCE(SUM(t1.ca), 0) AS INTEGER) AS customer_amount,
        cast(COALESCE(SUM(t1.oa), 0) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(SUM(t1.oa) / SUM(t1.ca)), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(SUM(t1.si) / SUM(t1.oa)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(SUM(t1.si) / SUM(t1.siq)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(SUM(t1.siq) / SUM(t1.oa)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order
    FROM t1 GROUP BY t1.brand, t1.zone, t1.member_type
    UNION SELECT DISTINCT
        t2.brand       AS brand,
        t2.zone        AS zone,
        t2.member_type AS member_type,
        cast(COALESCE(SUM(t2.si), 0) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t2.si) / SUM(t2.ttsi)), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(COALESCE(SUM(t2.ca), 0) AS INTEGER) AS customer_amount,
        cast(COALESCE(SUM(t2.oa), 0) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(SUM(t2.oa) / SUM(t2.ca)), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(SUM(t2.si) / SUM(t2.oa)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(SUM(t2.si) / SUM(t2.siq)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(SUM(t2.siq) / SUM(t2.oa)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order
    FROM t2 GROUP BY t2.brand, t2.zone, t2.member_type
"""

########################################################################################################################

SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT brand_name, {zone}, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type = '会员' AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, {zone}
    ), lyst AS (
        SELECT brand_name, {zone}, member_newold_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type IS NOT NULL AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, {zone}, member_newold_type
    )
    SELECT DISTINCT
        f.brand_name         AS brand,
        f.{zone}             AS zone,
        f.member_newold_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.{zone} = lyst.{zone} AND f.member_newold_type = lyst.member_newold_type
    WHERE f.member_newold_type IS NOT NULL AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.{zone}, f.member_newold_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT brand_name, {zone}, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type = '会员' AND member_newold_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, {zone}
    ), lyst AS (
        SELECT brand_name, {zone}, member_newold_type, member_level_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type IS NOT NULL AND member_level_type IS NOT NULL AND member_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, {zone}, member_newold_type, member_level_type
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone}     AS zone,
        f.member_newold_type,
        f.member_level_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.{zone} = lyst.{zone}
    AND f.member_newold_type = lyst.member_newold_type AND f.member_level_type = lyst.member_level_type
    WHERE f.member_newold_type IS NOT NULL AND f.member_level_type IS NOT NULL AND f.member_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.{zone}, f.member_newold_type, f.member_level_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT brand_name, {zone}, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type = '会员' AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, {zone}
    ), lyst AS (
        SELECT brand_name, {zone}, member_level_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type IS NOT NULL AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, {zone}, member_level_type
    )
    SELECT DISTINCT
        f.brand_name        AS brand,
        f.{zone}            AS zone,
        f.member_level_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.{zone} = lyst.{zone} AND f.member_level_type = lyst.member_level_type
    WHERE f.member_level_type IS NOT NULL AND f.member_type IS NULL AND f.member_newold_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.member_level_type, tt.sales_income, lyst.sales_income
"""
