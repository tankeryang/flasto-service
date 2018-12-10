ALL = """
    WITH tt AS (
        SELECT DISTINCT brand_name, {zone}, member_no
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND date(member_register_time) >= date('{start_date}')
        AND date(member_register_time) <= date('{end_date}') - interval '1' day
    ), tt_num AS (
        SELECT brand_name, {zone}, count(DISTINCT member_no) AS register_member_amount
        FROM tt GROUP BY brand_name, {zone}
    ), tt_lyst AS (
        SELECT DISTINCT brand_name, {zone}, member_no
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND date(member_register_time) >= date('{start_date}') - interval '1' year
        AND date(member_register_time) <= date('{end_date}') - interval '1' year
    ), tt_lyst_num AS (
        SELECT brand_name, {zone}, count(DISTINCT member_no) AS register_member_amount
        FROM tt_lyst GROUP BY brand_name, {zone}
    ), cs_lyst AS (
        SELECT DISTINCT
            f.brand_name,
            f.{zone},
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(tt_lyst_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount
        FROM cdm_crm.order_info_detail f
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name AND f.{zone} = tt_lyst_num.{zone}
        WHERE f.member_type = '会员'
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.{zone} IN ({zones})
        AND date(f.order_deal_time) <= date('{end_date}') - interval '1' day
        GROUP BY f.brand_name, f.{zone}, tt_lyst_num.register_member_amount
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        array_distinct(array_agg(f.{zone})) AS zone,
        cast(tt_num.register_member_amount AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt_num.register_member_amount * 1.0000 / tt_lyst_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
        cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0)  AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(tt_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast(COALESCE(TRY((tt_num.register_member_amount - count(DISTINCT f.member_no)) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst
    FROM cdm_crm.order_info_detail f
    INNER JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone} AND f.member_no = tt.member_no
    INNER JOIN tt_num ON f.brand_name = tt_num.brand_name AND f.{zone} = tt_num.{zone}
    INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name AND f.{zone} = tt_lyst_num.{zone}
    INNER JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name AND f.{zone} = cs_lyst.{zone}
    WHERE f.member_type = '会员'
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.{zone} IN ({zones})
    AND date(f.order_deal_time) <= date('{end_date}') - interval '1' day
    GROUP BY f.brand_name, f.{zone}, tt_num.register_member_amount, tt_lyst_num.register_member_amount,
        cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount
"""

########################################################################################################################

DAILY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, b.date
        FROM (
            SELECT DISTINCT brand_name, store_code, 'key' AS key FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands}) AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT order_deal_date AS date, 'key' AS key
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
            AND f.year_month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.year_month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
            AND f.vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
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
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
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
        SELECT DISTINCT
            a.brand_name AS brand,
            array_distinct(array_agg(a.store_code)) AS zone,
            b.year_month
        FROM (
            SELECT DISTINCT brand_name, store_code, 'key' AS key FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands}) AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT
                substr(cast(order_deal_date AS VARCHAR), 1, 7) AS year_month,
                'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}')
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
        GROUP BY a.brand_name, b.year_month
    ), tt AS (
        SELECT brand_name, substr(cast(date AS VARCHAR), 1, 7) AS year_month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, substr(cast(date AS VARCHAR), 1, 7)
    ), tt_lyst AS (
        SELECT brand_name, substr(cast(date AS VARCHAR), 1, 7) AS year_month,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' year
        AND date >= date('{start_date}') - interval '1' year
        GROUP BY brand_name, substr(cast(date AS VARCHAR), 1, 7)
    ), cs_lyst AS (
        SELECT DISTINCT f.brand_name, f.year_month,
        cast(cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt_lyst.register_member_amount - cardinality(array_intersect(tt_lyst.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name
            AND f.year_month = tt_lyst.year_month
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.store_code IN ({zones})
            AND f.year_month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.year_month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
            AND f.vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
        GROUP BY f.brand_name, tt_lyst.register_member_amount, tt_lyst.register_member_array, f.year_month
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
            f.year_month
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name
            AND f.year_month = tt.year_month
        LEFT JOIN tt_lyst ON f.brand_name = tt_lyst.brand_name
            AND cast(substr(f.year_month, 1, 4) AS INTEGER) - 1 = cast(substr(tt_lyst.year_month, 1, 4) AS INTEGER)
            AND cast(substr(f.year_month, 6, 2) AS INTEGER) = cast(substr(tt_lyst.year_month, 6, 2) AS INTEGER)
        LEFT JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name
            AND cast(substr(f.year_month, 1, 4) AS INTEGER) - 1 = cast(substr(cs_lyst.year_month, 1, 4) AS INTEGER)
            AND cast(substr(f.year_month, 6, 2) AS INTEGER) = cast(substr(cs_lyst.year_month, 6, 2) AS INTEGER)
        WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.store_code IN ({zones})
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
        GROUP BY
            f.brand_name, tt.register_member_amount, tt.register_member_array,
            tt_lyst.register_member_amount, cs_lyst.consumed_member_amount, cs_lyst.unconsumed_member_amount,
            f.year_month
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
    l.year_month
    FROM l LEFT JOIN d ON l.brand = d.brand
        AND l.year_month = d.year_month
"""
