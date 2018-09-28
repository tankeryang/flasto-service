SQL_CRM_TOTAL_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT brand_name, {zone}, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type = '整体' AND member_newold_type IS NULL AND member_level_type IS NULL
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
        SELECT brand_name, {zone}, member_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type IS NOT NULL AND member_newold_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, {zone}, member_type
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        f.member_type AS member_type,
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
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.{zone} = lyst.{zone} AND f.member_type = lyst.member_type
    WHERE f.member_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.{zone}, f.member_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

SQL_CRM_STORE_TOTAL_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT brand_name, store_code, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type = '整体' AND member_newold_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY brand_name, store_code
    ), lyst AS (
        SELECT brand_name, store_code, member_type, cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type IS NOT NULL AND member_newold_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND store_code IN ({zones})
        AND order_channel IN ({order_channels})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY brand_name, store_code, member_type
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        f.member_type AS member_type,
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
    LEFT JOIN lyst ON f.brand_name = lyst.brand_name AND f.store_code = lyst.store_code AND f.member_type = lyst.member_type
    WHERE f.member_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.store_code IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, f.member_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

SQL_CRM_TOTAL_DAILY_INCOME_DETAIL_DATA = """
    WITH lyst_t AS (
        SELECT t.brand_name, t.{zone}, cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income, t.date
        FROM ads_crm.member_analyse_daily_income_detail t
        WHERE t.brand_name IN ({brands})
        AND t.{zone} IN ({zones})
        AND t.order_channel IN ({order_channels})
        AND t.sales_mode IN ({sales_modes})
        AND t.store_type IN ({store_types})
        AND t.store_level IN ({store_levels})
        AND t.channel_type IN ({channel_types})
        AND t.date <= date(date('{end_date}') - interval '1' year)
        AND t.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY t.brand_name, t.{zone}, t.date
    )
    SELECT
        t.brand_name AS brand,
        t.{zone}     AS zone,
        cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t.sales_income) * 1.0 / lyst_t.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        t.date AS date
    FROM ads_crm.member_analyse_daily_income_detail t
    LEFT JOIN lyst_t ON t.brand_name = lyst_t.brand_name AND t.{zone} = lyst_t.{zone}
    AND t.date - interval '1' year = lyst_t.date
    WHERE t.brand_name IN ({brands})
    AND t.{zone} IN ({zones})
    AND t.order_channel IN ({order_channels})
    AND t.sales_mode IN ({sales_modes})
    AND t.store_type IN ({store_types})
    AND t.store_level IN ({store_levels})
    AND t.channel_type IN ({channel_types})
    AND t.date <= date('{end_date}')
    AND t.date >= date('{start_date}')
    GROUP BY t.brand_name, t.{zone}, t.date, lyst_t.sales_income
"""

########################################################################################################################

SQL_CRM_STORE_TOTAL_DAILY_INCOME_DETAIL_DATA = """
    WITH lyst_t AS (
        SELECT t.brand_name, t.store_code, cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income, t.date
        FROM ads_crm.member_analyse_daily_income_detail t
        WHERE t.brand_name IN ({brands})
        AND t.store_code IN ({zones})
        AND t.order_channel IN ({order_channels})
        AND t.date <= date(date('{end_date}') - interval '1' year)
        AND t.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY t.brand_name, t.store_code, t.date
    )
    SELECT
        t.brand_name AS brand,
        t.store_code AS zone,
        cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t.sales_income) * 1.0 / lyst_t.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        t.date AS date
    FROM ads_crm.member_analyse_daily_income_detail t
    LEFT JOIN lyst_t ON t.brand_name = lyst_t.brand_name AND t.store_code = lyst_t.store_code
    AND t.date - interval '1' year = lyst_t.date
    WHERE t.brand_name IN ({brands})
    AND t.store_code IN ({zones})
    AND t.order_channel IN ({order_channels})
    AND t.date <= date('{end_date}')
    AND t.date >= date('{start_date}')
    GROUP BY t.brand_name, t.store_code, t.date, lyst_t.sales_income
"""

########################################################################################################################

SQL_CRM_TOTAL_MONTHLY_INCOME_DETAIL_DATA = """
    WITH lyst_t AS (
        SELECT t.brand_name, t.{zone}, cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
            year(t.date) AS year, month(t.date) AS month
        FROM ads_crm.member_analyse_daily_income_detail t
        WHERE t.brand_name IN ({brands})
        AND t.{zone} IN ({zones})
        AND t.order_channel IN ({order_channels})
        AND t.sales_mode IN ({sales_modes})
        AND t.store_type IN ({store_types})
        AND t.store_level IN ({store_levels})
        AND t.channel_type IN ({channel_types})
        AND t.date <= date(date('{end_date}') - interval '1' year)
        AND t.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY t.brand_name, t.{zone}, year(t.date), month(t.date)
    )
    SELECT
        t.brand_name AS brand,
        t.{zone}     AS zone,
        cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t.sales_income) * 1.0 / lyst_t.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        cast(month(t.date) AS VARCHAR) AS month
    FROM ads_crm.member_analyse_daily_income_detail t
    LEFT JOIN lyst_t ON t.brand_name = lyst_t.brand_name AND t.{zone} = lyst_t.{zone}
    AND year(t.date) - 1 = lyst_t.year AND month(t.date) = lyst_t.month
    WHERE t.brand_name IN ({brands})
    AND t.{zone} IN ({zones})
    AND t.order_channel IN ({order_channels})
    AND t.sales_mode IN ({sales_modes})
    AND t.store_type IN ({store_types})
    AND t.store_level IN ({store_levels})
    AND t.channel_type IN ({channel_types})
    AND t.date <= date('{end_date}')
    AND t.date >= date('{start_date}')
    GROUP BY t.brand_name, t.{zone}, month(t.date), lyst_t.sales_income
"""

########################################################################################################################

SQL_CRM_STORE_TOTAL_MONTHLY_INCOME_DETAIL_DATA = """
    WITH lyst_t AS (
        SELECT t.brand_name, t.store_code, cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
            year(t.date) AS year, month(t.date) AS month
        FROM ads_crm.member_analyse_daily_income_detail t
        WHERE t.brand_name IN ({brands})
        AND t.store_code IN ({zones})
        AND t.order_channel IN ({order_channels})
        AND t.date <= date(date('{end_date}') - interval '1' year)
        AND t.date >= date(date('{start_date}') - interval '1' year)
        GROUP BY t.brand_name, t.store_code, year(t.date), month(t.date)
    )
    SELECT
        t.brand_name AS brand,
        t.store_code AS zone,
        cast(SUM(t.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(SUM(t.sales_income) * 1.0 / lyst_t.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        cast(month(t.date) AS VARCHAR) AS month
    FROM ads_crm.member_analyse_daily_income_detail t
    LEFT JOIN lyst_t ON t.brand_name = lyst_t.brand_name AND t.store_code = lyst_t.store_code
    AND year(t.date) - 1 = lyst_t.year AND month(t.date) = lyst_t.month
    WHERE t.brand_name IN ({brands})
    AND t.store_code IN ({zones})
    AND t.order_channel IN ({order_channels})
    AND t.date <= date('{end_date}')
    AND t.date >= date('{start_date}')
    GROUP BY t.brand_name, t.store_code, month(t.date), lyst_t.sales_income
"""