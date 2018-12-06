ALL = """
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
        AND year <= substr('{end_date}', 1, 4)
        AND year >= substr('{start_date}', 1, 4)
        AND month <= substr('{end_date}', 6, 2)
        AND month >= substr('{start_date}', 6, 2)
        AND vchr_date <= '{end_date}'
        AND vchr_date >= '{start_date}'
        GROUP BY brand_name, {zone}
    ), lyst AS (
        SELECT brand_name, {zone}, member_type,
        cast(sum(sales_income) AS DECIMAL(18, 3)) AS sales_income
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type IS NOT NULL AND member_newold_type IS NULL AND member_level_type IS NULL
        AND brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND year <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 4)
        AND year >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 4)
        AND month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 6, 2)
        AND month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 6, 2)
        AND vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
        AND vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
        GROUP BY brand_name, {zone}, member_type
    )
    SELECT DISTINCT
        f.brand_name    AS brand,
        array[f.{zone}] AS zone,
        f.member_type   AS member_type,
        cast(sum(f.sales_income) AS DECIMAL(18, 3)) AS sales_income,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / tt.sales_income), 0) AS DECIMAL(18, 4)) AS sales_income_proportion,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS customer_amount,
        cast(sum(f.order_amount) AS INTEGER) AS order_amount,
        cast(COALESCE(TRY(sum(f.order_amount) / cardinality(array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS consumption_frequency,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_income_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(f.sales_item_quantity)), 0) AS DECIMAL(18, 2)) AS sales_income_per_item,
        cast(COALESCE(TRY(sum(f.sales_item_quantity) * 1.0 / sum(f.order_amount)), 0) AS DECIMAL(18, 2)) AS sales_item_per_order,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / lyst.sales_income), 0) AS DECIMAL(18, 4)) AS compared_with_lyst,
        cast(COALESCE(TRY(sum(f.sales_income) * 1.0 / sum(lyst_sales_income)), 0) AS DECIMAL(18, 4)) AS compared_with_ss_lyst
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
    AND year <= substr('{end_date}', 1, 4)
    AND year >= substr('{start_date}', 1, 4)
    AND month <= substr('{end_date}', 6, 2)
    AND month >= substr('{start_date}', 6, 2)
    AND f.vchr_date <= '{end_date}'
    AND f.vchr_date >= '{start_date}'
    GROUP BY f.brand_name, f.{zone}, f.member_type, tt.sales_income, lyst.sales_income
"""

########################################################################################################################

DAILY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand, a.zone, a.member_type, b.date
        FROM (
            SELECT DISTINCT
                brand_name AS brand,
                {zone} AS zone,
                member_type AS member_type,
                'key' AS key
            FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands}) AND member_type IS NOT NULL AND {zone} IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT
                order_deal_date AS date,
                'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE order_deal_date <= date('{end_date}') AND order_deal_date >= date('{start_date}')
        ) b ON a.key = b.key
    ), tmp AS (
        SELECT DISTINCT
            brand,
            zone AS zone,
            member_type,
            sales_income,
            sales_income_proportion,
            compared_with_lyst,
            compared_with_ss_lyst,
            date,
            vchr_date
        FROM ads_crm.member_analyse_income_total_zone_daily
        WHERE vchr_date <= '{end_date}' AND vchr_date >= '{start_date}'
        AND brand IN ({brands})
        AND zone IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
    )
    SELECT DISTINCT
        l.brand,
        array[l.zone] AS zone,
        l.member_type,
        COALESCE(tmp.sales_income, 0) AS sales_income,
        COALESCE(tmp.sales_income_proportion, 0) AS sales_income_proportion,
        COALESCE(tmp.compared_with_lyst, 0) AS compared_with_lyst,
        COALESCE(tmp.compared_with_ss_lyst, 0) AS compared_with_ss_lyst,
        l.date
    FROM l LEFT JOIN tmp
    ON l.brand = tmp.brand
    AND l.zone = tmp.zone
    AND l.member_type = tmp.member_type
    AND l.date = tmp.date
"""

########################################################################################################################

MONTHLY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand, a.zone, a.member_type, b.year, b.month
        FROM (
            SELECT DISTINCT
                brand_name AS brand,
                {zone} AS zone,
                member_type AS member_type,
                'key' AS key
            FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands}) AND member_type IS NOT NULL AND {zone} IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT
                year(order_deal_date) AS year,
                month(order_deal_date) AS month,
                'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE order_deal_date <= date('{end_date}') AND order_deal_date >= date('{start_date}')
        ) b ON a.key = b.key
    ), tmp AS (
        SELECT DISTINCT
            brand,
            zone AS zone,
            member_type,
            sales_income,
            sales_income_proportion,
            compared_with_lyst,
            compared_with_ss_lyst,
            year,
            month
        FROM ads_crm.member_analyse_income_total_zone_monthly
        WHERE year <= year(date('{end_date}')) AND year >= year(date('{start_date}'))
        AND month <= month(date('{end_date}')) AND month >= month(date('{start_date}'))
        AND brand IN ({brands})
        AND zone IN ({zones})
        AND order_channel IN ({order_channels})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
    )
    SELECT DISTINCT
        l.brand,
        array[l.zone] AS zone,
        l.member_type,
        COALESCE(tmp.sales_income, 0) AS sales_income,
        COALESCE(tmp.sales_income_proportion, 0) AS sales_income_proportion,
        COALESCE(tmp.compared_with_lyst, 0) AS compared_with_lyst,
        COALESCE(tmp.compared_with_ss_lyst, 0) AS compared_with_ss_lyst,
        l.year,
        l.month
    FROM l LEFT JOIN tmp
    ON l.brand = tmp.brand
    AND l.zone = tmp.zone
    AND l.member_type = tmp.member_type
    AND l.year = tmp.year
    AND l.month = tmp.month
"""

########################################################################################################################

STATIC_ALL = """
    SELECT DISTINCT
        brand,
        array[zone] AS zone,
        member_type,
        sales_income,
        sales_income_proportion,
        customer_amount,
        order_amount,
        consumption_frequency,
        sales_income_per_order,
        sales_income_per_item,
        sales_item_per_order,
        compared_with_lyst,
        compared_with_ss_lyst
    FROM ads_crm.member_analyse_income_total_zone_all
    WHERE duration_type IN ({duration_type})
    AND brand IN ({brands})
    AND zone IN ({zones})
    AND order_channel IN ({order_channels})
    AND sales_mode IN ({sales_modes})
    AND store_type IN ({store_types})
    AND store_level IN ({store_levels})
    AND channel_type IN ({channel_types})
"""
