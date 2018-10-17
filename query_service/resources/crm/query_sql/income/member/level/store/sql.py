ALL = """
    WITH tt AS (
        SELECT brand_name, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type = '会员' AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name
    ), lyst AS (
        SELECT brand_name, member_level_type,
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type IS NOT NULL AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, member_level_type
    ), ss AS (
        SELECT ss.brand_name, ss.member_level_type,
        array_intersect(array_distinct(array_agg(ss.store_code)), lyst.store_array) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail ss
        LEFT JOIN lyst ON ss.brand_name = lyst.brand_name AND ss.member_level_type = lyst.member_level_type
        WHERE ss.member_level_type IS NOT NULL AND ss.member_newold_type IS NULL AND ss.member_type IS NULL
        AND ss.brand_name IN ({brands})
        AND ss.store_code IN ({zones})
        AND ss.order_channel IN ({order_channels})
        AND ss.date <= date('{end_date}')
        AND ss.date >= date('{start_date}')
        GROUP BY ss.brand_name, ss.member_level_type, lyst.store_array
    ), ss_lyst AS (
        SELECT ss_l.brand_name, ss_l.member_level_type,
        cast(sum(ss_l.sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail ss_l
        LEFT JOIN ss ON ss_l.brand_name = ss.brand_name AND ss_l.member_level_type = ss.member_level_type
        WHERE ss_l.member_level_type IS NOT NULL AND ss_l.member_newold_type IS NULL AND ss_l.member_type IS NULL
        AND contains(ss.store_array, ss_l.store_code)
        AND ss_l.brand_name IN ({brands})
        AND ss_l.store_code IN ({zones})
        AND ss_l.order_channel IN ({order_channels})
        AND ss_l.date <= date(date('{end_date}') - interval '1' year)
        AND ss_l.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY ss_l.brand_name, ss_l.member_level_type
    ), ss_now AS (
        SELECT DISTINCT f.brand_name, f.member_level_type,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / ss_lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN ss_lyst ON f.brand_name = ss_lyst.brand_name AND f.member_level_type = ss_lyst.member_level_type
        LEFT JOIN ss ON f.brand_name = ss.brand_name AND f.member_level_type = ss.member_level_type
        WHERE f.member_level_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_type IS NULL
        AND contains(ss.store_array, f.store_code)
        AND f.brand_name IN ({brands})
        AND f.store_code IN ({zones})
        AND f.order_channel IN ({order_channels})
        AND f.date <= date('{end_date}')
        AND f.date >= date('{start_date}')
        GROUP BY f.brand_name, f.member_level_type, ss_lyst.sales_income
    )
    SELECT DISTINCT
        f.brand_name        AS brand,
        array_distinct(array_agg(f.store_code)) AS zone,
        f.member_level_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        cast(COALESCE(ss_now.compared_with_ss_lyst, 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.member_level_type = lyst.member_level_type
    LEFT JOIN ss_now ON f.brand_name = ss_now.brand_name AND f.member_level_type = ss_now.member_level_type
    WHERE f.member_level_type IS NOT NULL AND f.member_type IS NULL AND f.member_newold_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.store_code IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.member_level_type, tt.sales_income, lyst.sales_income, ss_now.compared_with_ss_lyst
"""

########################################################################################################################

DAILY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, a.member_level_type AS member_type, b.date
        FROM (
            SELECT DISTINCT brand_name, member_level_type, store_code, 'key' AS key FROM cdm_crm.order_info_detail
            WHERE brand_name IN ({brands}) AND member_level_type IS NOT NULL AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT date(order_deal_time) date, 'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}')
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
        GROUP BY a.brand_name, a.member_level_type, b.date
    ), tt AS (
        SELECT brand_name, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income, date
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type = '会员' AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, date
    ), lyst AS (
        SELECT brand_name, member_level_type, date,
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type IS NOT NULL AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, member_level_type, date
    ), ss AS (
        SELECT ss.brand_name, ss.member_level_type, ss.date,
        array_intersect(array_distinct(array_agg(ss.store_code)), lyst.store_array) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail ss
        LEFT JOIN lyst ON ss.brand_name = lyst.brand_name AND ss.member_level_type = lyst.member_level_type
        AND ss.date - interval '1' year = lyst.date
        WHERE ss.member_level_type IS NOT NULL AND ss.member_newold_type IS NULL AND ss.member_type IS NULL
        AND ss.brand_name IN ({brands})
        AND ss.store_code IN ({zones})
        AND ss.order_channel IN ({order_channels})
        AND ss.date <= date('{end_date}')
        AND ss.date >= date('{start_date}')
        GROUP BY ss.brand_name, ss.member_level_type, lyst.store_array, ss.date
    ), ss_lyst AS (
        SELECT ss_l.brand_name, ss_l.member_level_type, ss_l.date,
        cast(sum(ss_l.sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail ss_l
        LEFT JOIN ss ON ss_l.brand_name = ss.brand_name AND ss_l.member_level_type = ss.member_level_type
        AND ss.date - interval '1' year = ss_l.date
        WHERE ss_l.member_level_type IS NOT NULL AND ss_l.member_newold_type IS NULL AND ss_l.member_type IS NULL
        AND contains(ss.store_array, ss_l.store_code)
        AND ss_l.brand_name IN ({brands})
        AND ss_l.store_code IN ({zones})
        AND ss_l.order_channel IN ({order_channels})
        AND ss_l.date <= date(date('{end_date}') - interval '1' year)
        AND ss_l.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY ss_l.brand_name, ss_l.member_level_type, ss_l.date
    ), ss_now AS (
        SELECT DISTINCT f.brand_name, f.member_level_type, f.date,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / ss_lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN ss_lyst ON f.brand_name = ss_lyst.brand_name AND f.member_level_type = ss_lyst.member_level_type
        AND f.date - interval '1' year = ss_lyst.date
        LEFT JOIN ss ON f.brand_name = ss.brand_name AND f.member_level_type = ss.member_level_type
        AND f.date = ss.date
        WHERE f.member_level_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_type IS NULL
        AND contains(ss.store_array, f.store_code)
        AND f.brand_name IN ({brands})
        AND f.store_code IN ({zones})
        AND f.order_channel IN ({order_channels})
        AND f.date <= date('{end_date}')
        AND f.date >= date('{start_date}')
        GROUP BY f.brand_name, f.member_level_type, ss_lyst.sales_income, f.date
    ), d AS (
        SELECT DISTINCT
            f.brand_name        AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
            f.member_level_type AS member_type,
            cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
            cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
            cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
            cast(COALESCE(ss_now.compared_with_ss_lyst, 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst,
            f.date
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.date = tt.date
        LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.member_level_type = lyst.member_level_type
        AND f.date - INTERVAL '1' YEAR = lyst.date
        LEFT JOIN ss_now ON f.brand_name = ss_now.brand_name AND f.member_level_type = ss_now.member_level_type
        AND f.date = ss_now.date
        WHERE f.member_level_type IS NOT NULL AND f.member_type IS NULL AND f.member_newold_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.store_code IN ({zones})
        AND f.order_channel IN ({order_channels})
        AND f.date <= DATE('{end_date}')
        AND f.date >= DATE('{start_date}')
        GROUP BY f.brand_name, f.member_level_type, tt.sales_income, lyst.sales_income, ss_now.compared_with_ss_lyst, f.date
    )
    SELECT DISTINCT l.brand, l.zone, l.member_type,
    COALESCE(d.sales_income, 0) AS sales_income,
    COALESCE(d.sales_income_proportion, 0) AS sales_income_proportion,
    COALESCE(d.compared_with_lyst, 0) AS compared_with_lyst,
    COALESCE(d.compared_with_ss_lyst, 0) AS compared_with_ss_lyst,
    l.date
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.member_type = d.member_type AND l.date = d.date
"""

########################################################################################################################

MONTHLY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, a.member_level_type AS member_type,
        b.year, b.month
        FROM (
            SELECT DISTINCT brand_name, member_level_type, store_code, 'key' AS key FROM cdm_crm.order_info_detail
            WHERE brand_name IN ({brands}) AND member_type IS NOT NULL AND store_code IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT year(order_deal_time) AS year, month(order_deal_time) AS month, 'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}')
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
        GROUP BY a.brand_name, a.member_level_type, b.year, b.month
    ), tt AS (
        SELECT brand_name, year(date) AS year, month(date) AS month,
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type = '会员' AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, year(date), month(date)
    ), lyst AS (
        SELECT brand_name, member_level_type, year(date) AS year, month(date) AS month,
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
        array_distinct(array_agg(store_code)) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_level_type IS NOT NULL AND member_type IS NULL AND member_newold_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, member_level_type, year(date), month(date)
    ), ss AS (
        SELECT ss.brand_name, ss.member_level_type, year(ss.date) AS year, month(ss.date) AS month,
        array_intersect(array_distinct(array_agg(ss.store_code)), lyst.store_array) AS store_array
        FROM ads_crm.member_analyse_fold_daily_income_detail ss
        LEFT JOIN lyst ON ss.brand_name = lyst.brand_name AND ss.member_level_type = lyst.member_level_type
        AND year(ss.date) - 1 = lyst.year AND month(ss.date) = lyst.month
        WHERE ss.member_level_type IS NOT NULL AND ss.member_newold_type IS NULL AND ss.member_type IS NULL
        AND ss.brand_name IN ({brands})
        AND ss.store_code IN ({zones})
        AND ss.order_channel IN ({order_channels})
        AND ss.date <= date('{end_date}')
        AND ss.date >= date('{start_date}')
        GROUP BY ss.brand_name, ss.member_level_type, lyst.store_array, year(ss.date), month(ss.date)
    ), ss_lyst AS (
        SELECT ss_l.brand_name, ss_l.member_level_type, year(ss_l.date) AS year, month(ss_l.date) AS month,
        cast(sum(ss_l.sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail ss_l
        LEFT JOIN ss ON ss_l.brand_name = ss.brand_name AND ss_l.member_level_type = ss.member_level_type
        AND ss.year - 1 = year(ss_l.date) AND ss.month = month(ss_l.date)
        WHERE ss_l.member_level_type IS NOT NULL AND ss_l.member_newold_type IS NULL AND ss_l.member_type IS NULL
        AND contains(ss.store_array, ss_l.store_code)
        AND ss_l.brand_name IN ({brands})
        AND ss_l.store_code IN ({zones})
        AND ss_l.order_channel IN ({order_channels})
        AND ss_l.date <= date(date('{end_date}') - interval '1' year)
        AND ss_l.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY ss_l.brand_name, ss_l.member_level_type, year(ss_l.date), month(ss_l.date)
    ), ss_now AS (
        SELECT DISTINCT f.brand_name, f.member_level_type, year(f.date) AS year, month(f.date) AS month,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / ss_lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN ss_lyst ON f.brand_name = ss_lyst.brand_name AND f.member_level_type = ss_lyst.member_level_type
        AND year(f.date) - 1 = ss_lyst.year AND month(f.date) = ss_lyst.month
        LEFT JOIN ss ON f.brand_name = ss.brand_name AND f.member_level_type = ss.member_level_type
        AND year(f.date) = ss.year AND month(f.date) = ss.month
        WHERE f.member_level_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_type IS NULL
        AND contains(ss.store_array, f.store_code)
        AND f.brand_name IN ({brands})
        AND f.store_code IN ({zones})
        AND f.order_channel IN ({order_channels})
        AND f.date <= date('{end_date}')
        AND f.date >= date('{start_date}')
        GROUP BY f.brand_name, f.member_level_type, ss_lyst.sales_income, year(f.date), month(f.date)
    ), d AS (
        SELECT DISTINCT
            f.brand_name        AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
            f.member_level_type AS member_type,
            cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
            cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
            cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
            cast(COALESCE(ss_now.compared_with_ss_lyst, 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst,
            YEAR(f.date) AS year,
            MONTH(f.date) AS month
        FROM ads_crm.member_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name AND YEAR(f.date) = tt.year AND MONTH(f.date) = tt.month
        LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.member_level_type = lyst.member_level_type
        AND YEAR(f.date) - 1 = lyst.year AND MONTH(DATE) = lyst.month
        LEFT JOIN ss_now ON f.brand_name = ss_now.brand_name AND f.member_level_type = ss_now.member_level_type
        AND year(f.date) = ss_now.year AND month(f.date) = ss_now.month
        WHERE f.member_level_type IS NOT NULL AND f.member_type IS NULL AND f.member_newold_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.store_code IN ({zones})
        AND f.order_channel IN ({order_channels})
        AND f.date <= DATE('{end_date}')
        AND f.date >= DATE('{start_date}')
        GROUP BY f.brand_name, f.member_level_type, tt.sales_income, lyst.sales_income, ss_now.compared_with_ss_lyst, YEAR(f.date), MONTH(f.date)
    )
    SELECT DISTINCT l.brand, l.zone, l.member_type,
    COALESCE(d.sales_income, 0) AS sales_income,
    COALESCE(d.sales_income_proportion, 0) AS sales_income_proportion,
    COALESCE(d.compared_with_lyst, 0) AS compared_with_lyst,
    COALESCE(d.compared_with_ss_lyst, 0) AS compared_with_ss_lyst,
    l.year, l.month
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.member_type = d.member_type AND l.year = d.year AND l.month = d.month
"""
