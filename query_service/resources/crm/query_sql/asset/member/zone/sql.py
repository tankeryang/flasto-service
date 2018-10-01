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
        cast(COALESCE(TRY(tt.register_member_amount * 1.0 / ytt.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_ystd,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0 / tt.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(tc.consumed_member_amount * 1.0 / yc.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_ystd,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0 - (cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0 / tt.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion
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
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS new_member_amount,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0 / tt.register_member_amount AS DECIMAL(18, 4)) AS new_member_amount_proportion,
        cast(tt.register_member_amount - cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS old_member_amount,
        cast(1 - (cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0 / tt.register_member_amount) AS DECIMAL(18, 4)) AS old_member_amount_proportion
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
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.{zone}     AS zone,
        CASE mi.member_grade_id
        WHEN 13 THEN '普通会员'
        WHEN 14 THEN 'VIP会员'
        ELSE NULL END  AS member_level_type,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS member_level_amount,
        cast(count(DISTINCT mi.member_no) * 1.0 / tt.register_member_amount AS DECIMAL(18, 4)) AS member_level_amount_proportion
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
