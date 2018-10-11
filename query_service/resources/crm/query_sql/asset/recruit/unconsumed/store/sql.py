DAILY = """
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
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        f.member_register_type,
        cast(COALESCE(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS member_amount,
        cast(COALESCE(TRY(cardinality(array_except(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
        f.date AS date
    FROM ads_crm.member_recruit_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    WHERE f.member_register_type IS NOT NULL AND f.member_recruit_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.store_code, f.member_register_type, f.date, tt.register_member_array, tt.register_member_amount
"""
