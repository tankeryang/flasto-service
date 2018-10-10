ALL = """
    WITH tt AS (
        SELECT brand_name, store_code,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code
    ), tt_lyst AS (
        SELECT brand_name, store_code,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, store_code
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, f.store_code,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, f.store_code, tt_lyst.register_member_amount, tt_lyst.register_member_array
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(tt.register_member_amount AS INTEGER) AS register_member_amount,
        cast(tt.register_member_amount * 1.0000 / tt_lyst.register_member_amount AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs_lyst.consumed_member_amount AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - (cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast((tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array)))))) * 1.0000 / cs_lyst.unconsumed_member_amount AS DECIMAL(18, 4)) AS uma_compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code
    LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND f.store_code = cs_lyst.store_code
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, tt.register_member_amount, tt.register_member_array, tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount
"""

########################################################################################################################

DAILY = """
    WITH tt AS (
        SELECT brand_name, store_code, date,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code, date
    ), tt_lyst AS (
        SELECT brand_name, store_code, date,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, store_code, date
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, f.store_code, f.date,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code AND f.date = tt_lyst.date
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, f.store_code, tt_lyst.register_member_amount, tt_lyst.register_member_array, f.date
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(COALESCE(tt.register_member_amount, 0) AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt.register_member_amount * 1.0000 / tt_lyst.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(COALESCE(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumed_member_amount,
        cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(COALESCE(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast(COALESCE(TRY((tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array)))))) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst,
        f.date
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code AND f.date = tt.date
    LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code
    AND f.date - interval '1' year = tt_lyst.date
    LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND f.store_code = cs_lyst.store_code
    AND f.date - interval '1' year = cs_lyst.date
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY
        f.brand_name, f.store_code,
        tt.register_member_amount, tt.register_member_array,
        tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount,
        f.date
"""

########################################################################################################################

MONTHLY = """
    WITH tt AS (
        SELECT brand_name, store_code, year(date) AS year, month(date) AS month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code, year(date), month(date)
    ), tt_lyst AS (
        SELECT brand_name, store_code, year(date) AS year, month(date) AS month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, store_code, year(date), month(date)
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, f.store_code, year(f.date) AS year, month(f.date) AS month,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code AND year(f.date) = tt_lyst.year AND month(f.date) = tt_lyst.month
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, f.store_code, tt_lyst.register_member_amount, tt_lyst.register_member_array, year(f.date), month(f.date)
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(COALESCE(tt.register_member_amount, 0) AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt.register_member_amount * 1.0000 / tt_lyst.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(COALESCE(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumed_member_amount,
        cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(COALESCE(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast(COALESCE(TRY((tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array)))))) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst,
        year(f.date) AS year, month(f.date) AS month
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code AND year(f.date) = tt.year AND month(f.date) = tt.month
    LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.store_code = tt_lyst.store_code
    AND year(f.date) - 1 = tt_lyst.year AND month(f.date) - 1 = tt_lyst.month
    LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND f.store_code = cs_lyst.store_code
    AND year(f.date) - 1 = cs_lyst.year AND month(f.date) - 1 = cs_lyst.month
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY
        f.brand_name, f.store_code,
        tt.register_member_amount, tt.register_member_array,
        tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount,
        year(f.date), month(f.date)
"""
