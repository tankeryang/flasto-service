DAILY = """
     WITH l AS (
         SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, a.member_register_type, b.date
         FROM (
             SELECT DISTINCT brand_name, member_register_type, store_code, 'key' AS key
             FROM ads_crm.member_recruit_analyse_fold_index_label
             WHERE brand_name IN ({brands}) AND member_register_type IS NOT NULL AND store_code IN ({zones})
         ) a FULL JOIN (
             SELECT DISTINCT date(order_deal_time) date, 'key' AS key
             FROM cdm_crm.order_info_detail
             WHERE date(order_deal_time) <= date('{end_date}') - interval '1' day
             AND date(order_deal_time) >= date('{start_date}')
         ) b ON a.key = b.key
         GROUP BY a.brand_name, a.store_code, a.member_register_type, b.date
    ), tt AS (
        SELECT brand_name,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
            f.member_register_type,
            cast(COALESCE(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS member_amount,
            cast(COALESCE(TRY(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
            f.date AS DATE
        FROM ads_crm.member_recruit_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name
        WHERE f.member_register_type IS NOT NULL AND f.member_recruit_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= DATE('{end_date}') - INTERVAL '1' DAY
        AND f.date >= DATE('{start_date}')
        GROUP BY f.brand_name, f.member_register_type, f.date, tt.register_member_array, tt.register_member_amount
    )
    SELECT DISTINCT l.brand, l.zone, l.member_register_type,
    COALESCE(d.member_amount, 0) AS member_amount,
    COALESCE(d.member_amount_proportion, 0) AS member_amount_proportion,
    l.date
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.member_register_type = d.member_register_type AND l.date = d.date
"""

########################################################################################################################

MONTHLY = """
     WITH l AS (
         SELECT DISTINCT a.brand_name AS brand, array_distinct(array_agg(a.store_code)) AS zone, a.member_register_type, b.year, b.month
         FROM (
             SELECT DISTINCT brand_name, member_register_type, store_code, 'key' AS key
             FROM ads_crm.member_recruit_analyse_fold_index_label
             WHERE brand_name IN ({brands}) AND member_register_type IS NOT NULL AND store_code IN ({zones})
         ) a FULL JOIN (
             SELECT DISTINCT year(order_deal_time) AS year, month(order_deal_time) AS month, 'key' AS key
             FROM cdm_crm.order_info_detail
             WHERE date(order_deal_time) <= date('{end_date}') - interval '1' day
             AND date(order_deal_time) >= date('{start_date}')
         ) b ON a.key = b.key
         GROUP BY a.brand_name, a.store_code, a.member_register_type, b.year, b.month
    ), tt AS (
        SELECT brand_name,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array_distinct(array_agg(f.store_code)) AS zone,
            f.member_register_type,
            cast(COALESCE(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS member_amount,
            cast(COALESCE(TRY(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
            year(f.date) AS year,
            month(f.date) AS month
        FROM ads_crm.member_recruit_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name
        WHERE f.member_register_type IS NOT NULL AND f.member_recruit_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.store_code IN ({zones})
        AND f.date <= DATE('{end_date}') - INTERVAL '1' DAY
        AND f.date >= DATE('{start_date}')
        GROUP BY f.brand_name, f.member_register_type, year(f.date), month(f.date), tt.register_member_array, tt.register_member_amount
    )
    SELECT DISTINCT l.brand, l.zone, l.member_register_type,
    COALESCE(d.member_amount, 0) AS member_amount,
    COALESCE(d.member_amount_proportion, 0) AS member_amount_proportion,
    l.year, l.month
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.member_register_type = d.member_register_type
    AND l.year = d.year AND l.month = d.month
"""
