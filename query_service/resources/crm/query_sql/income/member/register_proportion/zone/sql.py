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
        f.brand_name AS brand,
        f.{zone}     AS zone,
        cast(COALESCE(TRY(
            ne_m.order_amount * 1.0 / (IF(no_m.order_amount IS NOT NULL, no_m.order_amount, 0) + IF(ne_m.order_amount IS NOT NULL, ne_m.order_amount, 0))
        ), 0) AS DECIMAL(18, 4)) AS register_proportion
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN ne_m ON f.brand_name = ne_m.brand_name AND f.{zone} = ne_m.{zone}
    LEFT JOIN no_m ON f.brand_name = no_m.brand_name AND f.{zone} = no_m.{zone}
    WHERE f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
"""

########################################################################################################################

DAILY = """
    WITH ne_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount, date
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
        GROUP BY brand_name, {zone}, date
    ), no_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount, date
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
        GROUP BY brand_name, {zone}, date
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone}     AS zone,
        cast(COALESCE(TRY(
            ne_m.order_amount * 1.0 / (IF(no_m.order_amount IS NOT NULL, no_m.order_amount, 0) + IF(ne_m.order_amount IS NOT NULL, ne_m.order_amount, 0))
        ), 0) AS DECIMAL(18, 4)) AS register_proportion,
        f.date AS date
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN ne_m ON f.brand_name = ne_m.brand_name AND f.{zone} = ne_m.{zone} AND f.date = ne_m.date
    LEFT JOIN no_m ON f.brand_name = no_m.brand_name AND f.{zone} = no_m.{zone} AND f.date = no_m.date
    WHERE f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
"""

########################################################################################################################

MONTHLY = """
    WITH ne_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount,
            year(date) AS year, month(date) AS month
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
        GROUP BY brand_name, {zone}, year(date), month(date)
    ), no_m AS (
        SELECT brand_name, {zone}, cast(sum(order_amount) AS INTEGER) AS order_amount,
            year(date) AS year, month(date) AS month
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
        GROUP BY brand_name, {zone}, year(date), month(date)
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone}     AS zone,
        cast(COALESCE(TRY(
            ne_m.order_amount * 1.0 / (IF(no_m.order_amount IS NOT NULL, no_m.order_amount, 0) + IF(ne_m.order_amount IS NOT NULL, ne_m.order_amount, 0))
        ), 0) AS DECIMAL(18, 4)) AS register_proportion,
        year(f.date) AS year,
        month(f.date) AS month
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN ne_m ON f.brand_name = ne_m.brand_name AND f.{zone} = ne_m.{zone}
    AND year(f.date) = ne_m.year AND month(f.date) = ne_m.month
    LEFT JOIN no_m ON f.brand_name = no_m.brand_name AND f.{zone} = no_m.{zone}
    AND year(f.date) = no_m.year AND month(f.date) = no_m.month
    WHERE f.brand_name IN ({brands})
    AND f.{zone} IN ({zones})
    AND f.order_channel IN ({order_channels})
    AND f.sales_mode IN ({sales_modes})
    AND f.store_type IN ({store_types})
    AND f.store_level IN ({store_levels})
    AND f.channel_type IN ({channel_types})
    AND f.date <= date('{end_date}')
    AND f.date >= date('{start_date}')
"""
