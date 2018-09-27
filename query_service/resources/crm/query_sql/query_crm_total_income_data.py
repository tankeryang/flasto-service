SQL_CRM_TOTAL_INCOME_REPORT_DATA = """
    WITH tt AS (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type = '整体' AND member_newold_type IS NULL AND member_level_type IS NULL
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN (store_levels)
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}')
        AND date >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ), lyst AS (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
            cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type IS NOT NULL AND member_newold_type IS NULL AND member_level_type IS NULL
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date(date('{end_date}') - interval '1' year)
        AND date >= date(date('{start_date}') - interval '1' year)
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
    )
    SELECT DISTINCT
        f.member_type AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 2)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) / tt.sales_income), 0) AS DECIMAL(18, 3)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS costomer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.{zone} = tt.{zone} AND f.order_channel = tt.order_channel AND f.sales_mode = tt.sales_mode
    AND f.store_type = tt.store_type AND f.store_level = tt.store_level AND f.channel_type = tt.channel_type
    LEFT JOIN lyst ON f.{zone} = lyst.{zone} AND f.order_channel = lyst.order_channel
    AND f.sales_mode = lyst.sales_mode AND f.store_type = lyst.store_type AND f.store_level = lyst.store_level
    AND f.channel_type = lyst.channel_type AND f.member_type = lyst.member_type
    WHERE f.member_type IS NOT NULL AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
    GROUP BY f.member_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

SQL_CRM_TOTAL_DAILY_INCOME_DETAIL_DATA = """
    SELECT
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(sales_income) / sum(lyst_sales_income)), 0) AS DECIMAL(18, 3)) AS compared_with_lyst,
        date AS date
    FROM ads_crm.member_analyse_daily_income_detail
    WHERE {zone} IN ({zones})
    AND order_channel IN ({order_channels})
    AND sales_mode IN ({sales_modes})
    AND store_type IN ({store_types})
    AND store_level IN ({store_levels})
    AND channel_type IN ({channel_types})
    AND date <= date('{end_date}')
    AND date >= date('{start_date}')
    GROUP BY date
"""

########################################################################################################################

SQL_CRM_TOTAL_MONTHLY_INCOME_DETAIL_DATA = """
    SELECT
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(sales_income) / sum(lyst_sales_income)), 0) AS DECIMAL(18, 3)) AS compared_with_lyst,
        cast(month(date) AS VARCHAR) AS month
    FROM ads_crm.member_analyse_daily_income_detail
    WHERE {zone} IN ({zones})
    AND order_channel IN ({order_channels})
    AND sales_mode IN ({sales_modes})
    AND store_type IN ({store_types})
    AND store_level IN ({store_levels})
    AND channel_type IN ({channel_types})
    AND date <= date('{end_date}')
    AND date >= date('{start_date}')
    GROUP BY month(date)
"""
