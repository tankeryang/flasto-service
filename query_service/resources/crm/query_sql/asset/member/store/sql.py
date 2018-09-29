STATIC = """
    WITH tt AS (
        SELECT brand_name, store_code,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}')
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(tt.register_member_amount AS INTEGER) AS register_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}')
    GROUP BY f.brand_name, f.store_code, tt.register_member_amount, tt.register_member_array
"""
