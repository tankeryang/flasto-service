ALL = """
    WITH ne_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type IS NULL AND member_newold_type = '新会员' AND member_level_type IS NULL
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
    ), no_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE member_type = '非会员' AND member_newold_type IS NULL AND member_level_type IS NULL
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
    )
    SELECT DISTINCT
        cmail.brand_name AS brand,
        cmail.{zone}     AS zone,
        cast(COALESCE(TRY(ne_m.order_amount * 1.0 / no_m.order_amount), 0) AS DECIMAL(18, 4)) AS register_proportion
    FROM cdm_common.crm_member_analyse_index_label cmail
    RIGHT JOIN ne_m ON cmail.brand_name = ne_m.brand_name AND cmail.{zone} = ne_m.{zone}
    RIGHT JOIN no_m ON cmail.brand_name = no_m.brand_name AND cmail.{zone} = no_m.{zone}
"""