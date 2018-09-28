ALL = """
    WITH tt AS (
        SELECT brand_name, store_code, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type = '会员' AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code
    ), lyst AS (
        SELECT brand_name, store_code, member_newold_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type IS NOT NULL AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, store_code, member_newold_type
    )
    SELECT DISTINCT
        f.brand_name         AS brand,
        f.store_code         AS zone,
        f.member_newold_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.store_code = lyst.store_code AND f.member_newold_type = lyst.member_newold_type
    WHERE f.member_newold_type IS NOT NULL AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.store_code IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, f.member_newold_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

DAILY = """
    WITH tt AS (
        SELECT
            brand_name,
            store_code,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
            date
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type = '会员' AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code, date
    ), lyst AS (
        SELECT
            brand_name,
            store_code,
            member_newold_type,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
            date
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type IS NOT NULL AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, store_code, member_newold_type, date
    )
    SELECT DISTINCT
        f.brand_name         AS brand,
        f.store_code         AS zone,
        f.member_newold_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        f.date
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code AND f.date = tt.date
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.store_code = lyst.store_code
    AND f.member_newold_type = lyst.member_newold_type AND f.date - interval '1' year = lyst.date
    WHERE f.member_newold_type IS NOT NULL AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.store_code IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, f.member_newold_type, tt.sales_income, lyst.sales_income, f.date
"""

########################################################################################################################

MONTHLY = """
    WITH tt AS (
        SELECT
            brand_name,
            store_code,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
            year(date) AS year,
            month(date) AS month
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type = '会员' AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code, year(date), month(date)
    ), lyst AS (
        SELECT
            brand_name,
            store_code,
            member_newold_type,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
            year(date) AS year,
            month(date) AS month
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_newold_type IS NOT NULL AND member_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, store_code, member_newold_type, year(date), month(date)
    )
    SELECT DISTINCT
        f.brand_name         AS brand,
        f.store_code         AS zone,
        f.member_newold_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        year(f.date) AS year,
        month(f.date) AS month
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    AND year(f.date) = tt.year AND month(f.date) = tt.month
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.store_code = lyst.store_code
    AND f.member_newold_type = lyst.member_newold_type
    AND year(f.date) - 1 = lyst.year AND month(date) = lyst.month
    WHERE f.member_newold_type IS NOT NULL AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.store_code IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, f.member_newold_type, tt.sales_income, lyst.sales_income, year(f.date), month(f.date)
"""
