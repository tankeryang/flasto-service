DAILY = """
    WITH l AS (
        SELECT DISTINCT a.brand_name AS brand, array[a.{zone}] AS zone, a.member_recruit_type, b.date
        FROM (
            SELECT DISTINCT brand_name, member_recruit_type, {zone}, 'key' AS key
            FROM ads_crm.member_recruit_analyse_fold_daily_income_detail
            WHERE brand_name IN ({brands}) AND member_recruit_type IS NOT NULL AND member_recruit_type != '未升级' AND {zone} IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT date(order_deal_time) date, 'key' AS key
            FROM cdm_crm.order_info_detail
            WHERE date(order_deal_time) <= date('{end_date}') - interval '1' day
            AND date(order_deal_time) >= date('{start_date}')
        ) b ON a.key = b.key
    ), tt AS (
        SELECT brand_name, {zone},
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
        GROUP BY brand_name, {zone}
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array[f.{zone}] AS zone,
            f.member_recruit_type,
            cast(COALESCE(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))), 0) AS INTEGER) AS member_amount,
            cast(COALESCE(TRY(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
            f.date AS date
        FROM ads_crm.member_recruit_analyse_fold_daily_income_detail f
        LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
        WHERE f.member_recruit_type IS NOT NULL AND f.member_recruit_type != '未升级' AND f.member_register_type IS NULL
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.{zone} IN ({zones})
        AND f.sales_mode IN ({sales_modes})
        AND f.store_type IN ({store_types})
        AND f.store_level IN ({store_levels})
        AND f.channel_type IN ({channel_types})
        AND f.date <= DATE('{end_date}') - INTERVAL '1' DAY
        AND f.date >= DATE('{start_date}')
        GROUP BY f.brand_name, f.{zone}, f.member_recruit_type, f.date, tt.register_member_array, tt.register_member_amount
    )
    SELECT DISTINCT l.brand, l.zone, l.member_recruit_type,
    COALESCE(d.member_amount, 0) AS member_amount,
    COALESCE(d.member_amount_proportion, 0) AS member_amount_proportion,
    l.date
    FROM l LEFT JOIN d ON l.brand = d.brand AND l.zone = d.zone AND l.member_recruit_type = d.member_recruit_type AND l.date = d.date
"""
