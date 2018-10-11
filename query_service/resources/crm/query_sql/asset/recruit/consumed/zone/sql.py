DAILY = """
    WITH tt AS (
        SELECT brand_name, {zone}, date,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND {zone} IN ({zones})
        AND sales_mode IN ({sales_modes})
        AND store_type IN ({store_types})
        AND store_level IN ({store_levels})
        AND channel_type IN ({channel_types})
        AND date <= date('{end_date}') - interval '1' day
        AND date >= date('{start_date}')
        GROUP BY brand_name, {zone}, date
    ), cs AS (
        SELECT cs.brand_name, cs.{zone}, cs.date,
        array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(cs.customer_array)))) AS consumed_member_array,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(cs.customer_array))))) AS INTEGER) AS consumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail cs
        LEFT JOIN tt ON cs.brand_name = tt.brand_name AND cs.{zone} = tt.{zone}
        WHERE cs.member_type = '会员' AND cs.member_newold_type IS NULL AND cs.member_level_type IS NULL
        AND cs.brand_name IN ({brands})
        AND cs.order_channel IN ({order_channels})
        AND cs.{zone} IN ({zones})
        AND cs.sales_mode IN ({sales_modes})
        AND cs.store_type IN ({store_types})
        AND cs.store_level IN ({store_levels})
        AND cs.channel_type IN ({channel_types})
        AND cs.date <= date('{end_date}') - interval '1' day
        AND cs.date >= date('{start_date}')
        GROUP BY cs.brand_name, cs.{zone}, cs.date, tt.register_member_array, cs.date
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone}     AS zone,
        f.member_recruit_type,
        cast(cardinality(array_intersect(cs.consumed_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS member_amount,
        cast(COALESCE(TRY(cardinality(array_intersect(cs.consumed_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / cs.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
        f.date AS date
    FROM ads_crm.member_recruit_analyse_fold_daily_income_detail f
    LEFT JOIN cs ON f.brand_name = cs.brand_name AND f.{zone} = cs.{zone} AND f.date = cs.date
    WHERE f.member_recruit_type IS NOT NULL AND f.member_recruit_type != '未升级' AND f.member_register_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.{zone} IN ({zones})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}') - interval '1' day
    AND f.date >= date('{start_date}')
    GROUP BY f.brand_name, f.{zone}, f.member_recruit_type, f.date, cs.consumed_member_array, cs.consumed_member_amount
"""
