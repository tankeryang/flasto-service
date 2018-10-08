ALL = """
    WITH tt AS (
        SELECT brand_name, {zone},
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}') - interval '1' day
        GROUP BY brand_name, {zone}
    ), ytt AS (
        SELECT brand_name, {zone},
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}') - interval '2' day
        GROUP BY brand_name, {zone}
    ), yc AS (
        SELECT brand_name, {zone},
        cardinality(array_distinct(flatten(array_agg(customer_array)))) AS consumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}') - interval '2' day
        GROUP BY brand_name, {zone}
    ), tc AS (
        SELECT brand_name, {zone},
        cardinality(array_distinct(flatten(array_agg(customer_array)))) AS consumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}') - interval '1' day
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        cast(tt.register_member_amount AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt.register_member_amount * 1.0000 / ytt.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_ystd,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(tc.consumed_member_amount * 1.0000 / yc.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_ystd,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - (cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    LEFT JOIN ytt ON f.brand_name = ytt.brand_name AND f.{zone} = ytt.{zone}
    LEFT JOIN yc ON f.brand_name = yc.brand_name AND f.{zone} = yc.{zone}
    LEFT JOIN tc ON f.brand_name = tc.brand_name AND f.{zone} = tc.{zone}
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.{zone} IN ({zones})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}') - interval '1' day
    GROUP BY
        f.brand_name, f.{zone},
        tt.register_member_amount, tt.register_member_array, ytt.register_member_amount,
        yc.consumed_member_amount, tc.consumed_member_amount
"""

########################################################################################################################

NEW_OLD = """
    WITH tt AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS new_member_amount,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS new_member_amount_proportion,
        cast(tt.register_member_amount - cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS old_member_amount,
        cast(1 - (cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS old_member_amount_proportion
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    WHERE f.member_newold_type = '新会员' AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.{zone} IN ({zones})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}') - interval '1' day
    GROUP BY f.brand_name, f.{zone}, tt.register_member_amount
"""

########################################################################################################################

LEVEL = """
    WITH tt AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.{zone}     AS zone,
        CASE mi.member_grade_id
        WHEN 13 THEN '普通会员'
        WHEN 14 THEN 'VIP会员'
        ELSE NULL END  AS member_level_type,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS member_level_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS member_level_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.{zone} = tt.{zone}
    WHERE mi.brand_name IN ({brands})
    AND mi.{zone} IN ({zones})
    AND mi.sales_mode IN ({sales_modes})
    AND mi.store_type IN ({store_types})
    AND mi.store_level IN ({store_levels})
    AND mi.channel_type IN ({channel_types})
    AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    GROUP BY mi.brand_name, mi.{zone}, tt.register_member_amount,
    CASE mi.member_grade_id
    WHEN 13 THEN '普通会员'
    WHEN 14 THEN 'VIP会员'
    ELSE NULL END
"""

########################################################################################################################

REMAIN = """
    WITH tt AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.{zone}     AS zone,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS remain_member_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS remain_member_amount_proportion,
        cast(tt.register_member_amount - count(DISTINCT mi.member_no) AS INTEGER) AS lost_member_amount,
        cast(1.0000 - count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS lost_member_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.{zone} = tt.{zone}
    WHERE mi.brand_name IN ({brands})
    AND mi.{zone} IN ({zones})
    AND mi.sales_mode IN ({sales_modes})
    AND mi.store_type IN ({store_types})
    AND mi.store_level IN ({store_levels})
    AND mi.channel_type IN ({channel_types})
    AND date(mi.member_last_order_time) <= date('{end_date}') - interval '1' day
    AND date(mi.member_last_order_time) >= date('{end_date}') - interval '1' year
    GROUP BY mi.brand_name, mi.{zone}, tt.register_member_amount
"""

########################################################################################################################

ACTIVE = """
    WITH tt AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '1' DAY
        AND date(member_last_order_time) >= date('{end_date}') - interval '1' year
        GROUP BY brand_name, {zone}
    ), t_36 AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '3' month
        AND date(member_last_order_time) >= date('{end_date}') - interval '6' month
        GROUP BY brand_name, {zone}
    ), t_69 AS (
        SELECT brand_name, {zone},
        count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '6' month
        AND date(member_last_order_time) >= date('{end_date}') - interval '9' month
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.{zone}     AS zone,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS active_member_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS active_member_amount_proportion,
        cast(t_36.member_amount AS INTEGER) AS silent_member_amount,
        cast(t_36.member_amount * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS silent_member_amount_proportion,
        cast(t_69.member_amount AS INTEGER) AS sleep_member_amount,
        cast(t_69.member_amount * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS sleep_member_amount_proportion,
        cast(tt.member_amount - (count(DISTINCT mi.member_no) + t_36.member_amount + t_69.member_amount) AS INTEGER) AS pre_lost_member_amount,
        cast(1.0000 - (count(DISTINCT mi.member_no) + t_36.member_amount + t_69.member_amount) * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS pre_lost_member_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.{zone} = tt.{zone}
    LEFT JOIN t_36 ON mi.brand_name = t_36.brand_name AND mi.{zone} = t_36.{zone}
    LEFT JOIN t_69 ON mi.brand_name = t_69.brand_name AND mi.{zone} = t_69.{zone}
    WHERE mi.brand_name IN ({brands})
    AND mi.{zone} IN ({zones})
    AND mi.sales_mode IN ({sales_modes})
    AND mi.store_type IN ({store_types})
    AND mi.store_level IN ({store_levels})
    AND mi.channel_type IN ({channel_types})
    AND date(mi.member_last_order_time) <= date('{end_date}') - interval '1' day
    AND date(mi.member_last_order_time) >= date('{end_date}') - interval '3' month
    GROUP BY mi.brand_name, mi.{zone}, tt.member_amount, t_36.member_amount, t_69.member_amount
"""

########################################################################################################################

RECENCY = """
    WITH r AS (
        SELECT
            mi.brand_name,
            mi.{zone},
            mi.member_no,
            IF (mi.member_last_order_time IS NOT NULL,
                CASE
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '1' DAY
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '3' month
                ) THEN '<3'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '3' month
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '5' month
                ) THEN '3-5'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '6' month
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '8' month
                ) THEN '6-8'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '9' month
                ) THEN '>9'
                ELSE NULL END,
                NULL
            ) recency
        FROM cdm_crm.member_info_detail mi
        WHERE mi.brand_name IN ({brands})
        AND mi.{zone} IN ({zones})
        AND mi.sales_mode IN ({sales_modes})
        AND mi.store_type IN ({store_types})
        AND mi.store_level IN ({store_levels})
        AND mi.channel_type IN ({channel_types})
        AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    )
    SELECT DISTINCT
        brand_name AS brand,
        {zone} AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        recency
    FROM r WHERE recency IS NOT NULL
    GROUP BY brand_name, {zone}, recency
"""

########################################################################################################################

FREQUENCY = """
    WITH f AS (
        SELECT
            mi.brand_name,
            mi.{zone},
            mi.member_no,
            IF (count(distinct oi.outer_order_no) IS NOT NULL,
                CASE count(distinct oi.outer_order_no)
                WHEN 1 THEN '1'
                WHEN 2 THEN '2'
                WHEN 3 THEN '3'
                WHEN 4 THEN '>=4'
                ELSE '>=4' END,
                NULL
            ) frequency
        FROM cdm_crm.member_info_detail mi
        LEFT JOIN ods_crm.order_info oi ON mi.member_no = oi.member_no
        WHERE mi.brand_name IN ({brands})
        AND mi.{zone} IN ({zones})
        AND mi.sales_mode IN ({sales_modes})
        AND mi.store_type IN ({store_types})
        AND mi.store_level IN ({store_levels})
        AND mi.channel_type IN ({channel_types})
        AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
        GROUP BY mi.member_no, mi.brand_name, mi.{zone}
    )
    SELECT DISTINCT
        brand_name AS brand,
        {zone} AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        frequency
    FROM f WHERE frequency IS NOT NULL
    GROUP BY brand_name, {zone}, frequency
"""

########################################################################################################################

MONETARY = """
    WITH m AS (
        SELECT
            mi.brand_name,
            mi.{zone},
            mi.member_no,
            IF (sum(oi.order_fact_amount) IS NOT NULL,
                CASE
                    WHEN (
                        sum(oi.order_fact_amount) < 1500
                    ) THEN '<1500'
                    WHEN (
                        sum(oi.order_fact_amount) < 3800
                        AND sum(oi.order_fact_amount) >= 1500
                    ) THEN '1500-3799'
                    WHEN (
                        sum(oi.order_fact_amount) < 5000
                        AND sum(oi.order_fact_amount) >= 3800
                    ) THEN '3800-4999'
                    WHEN (
                        sum(oi.order_fact_amount) >= 5000
                    ) THEN '>5000'
                    ELSE NULL END,
                NULL
            ) monetary
        FROM cdm_crm.member_info_detail mi
        LEFT JOIN ods_crm.order_info oi ON mi.member_no = oi.member_no
        WHERE mi.brand_name IN ({brands})
        AND mi.{zone} IN ({zones})
        AND mi.sales_mode IN ({sales_modes})
        AND mi.store_type IN ({store_types})
        AND mi.store_level IN ({store_levels})
        AND mi.channel_type IN ({channel_types})
        AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
        GROUP BY mi.member_no, mi.brand_name, mi.{zone}
    )
    SELECT DISTINCT
        brand_name AS brand,
        {zone} AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        monetary
    FROM m WHERE monetary IS NOT NULL
    GROUP BY brand_name, {zone}, monetary
"""