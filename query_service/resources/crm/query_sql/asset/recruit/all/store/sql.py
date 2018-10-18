ALL = """
    WITH tt AS (
        SELECT brand_name,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name
    ), tt_lyst AS (
        SELECT brand_name,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, tt_lyst.register_member_amount, tt_lyst.register_member_array
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        array_distinct(array_agg(f.store_code)) AS zone,
        cast(tt.register_member_amount AS INTEGER) AS register_member_amount,
        cast(tt.register_member_amount * 1.0000 / tt_lyst.register_member_amount AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs_lyst.consumed_member_amount AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - (cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast((tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array)))))) * 1.0000 / cs_lyst.unconsumed_member_amount AS DECIMAL(18, 4)) AS uma_compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name
    LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name
    LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, tt.register_member_amount, tt.register_member_array, tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount
"""

########################################################################################################################

DAILY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, b.date
        FROM (
            SELECT DISTINCT brand_name, store_code, 'key' AS key FROM cdm_crm.order_info_detail
            WHERE brand_name IN ({brands}) AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT date(order_deal_time) date, 'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}')
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
        GROUP BY a.brand_name, b.date
    ), tt AS (
        SELECT brand_name, date,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, date
    ), tt_lyst AS (
        SELECT brand_name, date,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, date
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, f.date,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.date = tt_lyst.date
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, tt_lyst.register_member_amount, tt_lyst.register_member_array, f.date
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
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
        LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.date = tt.date
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND f.date - INTERVAL '1' YEAR = tt_lyst.date
        LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND f.date - INTERVAL '1' YEAR = cs_lyst.date
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= DATE('{end_date}') - INTERVAL '1' DAY
        AND f.date >= DATE('{start_date}')
        GROUP BY
            f.brand_name, tt.register_member_amount, tt.register_member_array,
            tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount, f.date
    )
    SELECT DISTINCT l.brand, l.zone,
    COALESCE(d.register_member_amount, 0) AS register_member_amount,
    COALESCE(d.rma_compared_with_lyst, 0) AS rma_compared_with_lyst,
    COALESCE(d.consumed_member_amount, 0) AS consumed_member_amount,
    COALESCE(d.consumed_member_amount_proportion, 0) AS consumed_member_amount_proportion,
    COALESCE(d.cma_compared_with_lyst, 0) AS cma_compared_with_lyst,
    COALESCE(d.unconsumed_member_amount, 0) AS unconsumed_member_amount,
    COALESCE(d.unconsumed_member_amount_proportion, 0) AS unconsumed_member_amount_proportion,
    COALESCE(d.uma_compared_with_lyst, 0) AS uma_compared_with_lyst,
    l.date
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.date = d.date
"""

########################################################################################################################

MONTHLY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone,
        b.year, b.month
        FROM (
            SELECT DISTINCT brand_name, store_code, 'key' AS key FROM cdm_crm.order_info_detail
            WHERE brand_name IN ({brands}) AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT year(order_deal_time) AS year, month(order_deal_time) AS month, 'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}')
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
        GROUP BY a.brand_name, b.year, b.month
    ), tt AS (
        SELECT brand_name, year(date) AS year, month(date) AS month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, year(date), month(date)
    ), tt_lyst AS (
        SELECT brand_name, year(date) AS year, month(date) AS month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, year(date), month(date)
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, year(f.date) AS year, month(f.date) AS month,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND year(f.date) = tt_lyst.year AND month(f.date) = tt_lyst.month
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= date('{end_date}') - interval '1' year
        AND f.date >= date('{start_date}') - interval '1' year
        GROUP BY f.brand_name, tt_lyst.register_member_amount, tt_lyst.register_member_array, year(f.date), month(f.date)
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
            cast(COALESCE(tt.register_member_amount, 0) AS INTEGER) AS register_member_amount,
            cast(COALESCE(TRY(tt.register_member_amount * 1.0000 / tt_lyst.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
            cast(COALESCE(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumed_member_amount,
            cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
            cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
            cast(COALESCE(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS unconsumed_member_amount,
            cast(1.0000 - COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
            cast(COALESCE(TRY((tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array)))))) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst,
            YEAR(f.date) AS year, MONTH(f.date) AS month
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name AND YEAR(f.date) = tt.year AND MONTH(f.date) = tt.month
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name AND YEAR(f.date) - 1 = tt_lyst.year AND MONTH(f.date) - 1 = tt_lyst.month
        LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND YEAR(f.date) - 1 = cs_lyst.year AND MONTH(f.date) - 1 = cs_lyst.month
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= DATE('{end_date}') - INTERVAL '1' DAY
        AND f.date >= DATE('{start_date}')
        GROUP BY
            f.brand_name, tt.register_member_amount, tt.register_member_array,
            tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount,
            YEAR(f.date), MONTH(f.date)
    )
    SELECT DISTINCT l.brand, l.zone,
    COALESCE(d.register_member_amount, 0) AS register_member_amount,
    COALESCE(d.rma_compared_with_lyst, 0) AS rma_compared_with_lyst,
    COALESCE(d.consumed_member_amount, 0) AS consumed_member_amount,
    COALESCE(d.consumed_member_amount_proportion, 0) AS consumed_member_amount_proportion,
    COALESCE(d.cma_compared_with_lyst, 0) AS cma_compared_with_lyst,
    COALESCE(d.unconsumed_member_amount, 0) AS unconsumed_member_amount,
    COALESCE(d.unconsumed_member_amount_proportion, 0) AS unconsumed_member_amount_proportion,
    COALESCE(d.uma_compared_with_lyst, 0) AS uma_compared_with_lyst,
    l.year, l.month
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.year = d.year AND l.month = d.month
"""
