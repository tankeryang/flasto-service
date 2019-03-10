ALL = """
    WITH tt AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}')
            AND date(member_register_time) <= date('{end_date}')
    ), tt_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount
        FROM tt
        GROUP BY brand_name, {zone}
    ), tt_lyst AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}') - interval '1' year
            AND date(member_register_time) <= date('{end_date}') - interval '1' year
    ), tt_lyst_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount
        FROM tt_lyst
        GROUP BY brand_name, {zone}
    ), cs_lyst AS (
        SELECT DISTINCT
            f.brand_name,
            f.{zone},
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(tt_lyst_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount
        FROM ads_crm.order_info_detail f
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
            AND f.{zone} = tt_lyst_num.{zone}
        WHERE f.member_type = '会员'
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.sales_mode IN ({sales_modes})
            AND f.store_type IN ({store_types})
            AND f.store_level IN ({store_levels})
            AND f.channel_type IN ({channel_types})
            AND f.year_month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.year_month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
            AND f.vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
        GROUP BY f.brand_name, f.{zone}, tt_lyst_num.register_member_amount
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        array[f.{zone}] AS zone,
        cast(tt_num.register_member_amount AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt_num.register_member_amount * 1.0000 / tt_lyst_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
        cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
        cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0)  AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
        cast(tt_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
        cast(COALESCE(TRY((tt_num.register_member_amount - count(DISTINCT f.member_no)) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst
    FROM ads_crm.order_info_detail f
    INNER JOIN tt ON f.brand_name = tt.brand_name
        AND f.{zone} = tt.{zone}
        AND f.member_no = tt.member_no
    INNER JOIN tt_num ON f.brand_name = tt_num.brand_name
        AND f.{zone} = tt_num.{zone}
    INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
        AND f.{zone} = tt_lyst_num.{zone}
    INNER JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name
        AND f.{zone} = cs_lyst.{zone}
    WHERE f.member_type = '会员'
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.{zone} IN ({zones})
        AND f.sales_mode IN ({sales_modes})
        AND f.store_type IN ({store_types})
        AND f.store_level IN ({store_levels})
        AND f.channel_type IN ({channel_types})
        AND f.year_month <= substr('{end_date}', 1, 7)
        AND f.year_month >= substr('{start_date}', 1, 7)
        AND f.vchr_date <= '{end_date}'
        AND f.vchr_date >= '{start_date}'
    GROUP BY
        f.brand_name,
        f.{zone},
        tt_num.register_member_amount,
        tt_lyst_num.register_member_amount,
        cs_lyst.consumed_member_amount,
        cs_lyst.unconsumed_member_amount
"""

########################################################################################################################

DAILY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand_name AS brand,
            array[a.{zone}] AS zone,
            b.date
        FROM (
            SELECT DISTINCT
                brand_name,
                {zone},
                'key' AS key
            FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands})
                AND {zone} IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT
                order_deal_date AS date,
                'key' AS key
            FROM ads_crm.order_info_detail
            WHERE year_month <= substr('{end_date}', 1, 7)
                AND year_month >= substr('{start_date}', 1, 7)
                AND vchr_date <= '{end_date}'
                AND vchr_date >= '{start_date}'
        ) b ON a.key = b.key
    ), tt AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no,
            date(member_register_time) AS date
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}')
            AND date(member_register_time) <= date('{end_date}')
    ), tt_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount,
            date
        FROM tt
        GROUP BY brand_name, {zone}, date
    ), tt_lyst AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no,
            date(member_register_time) AS date
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}') - interval '1' year
            AND date(member_register_time) <= date('{end_date}') - interval '1' year
    ), tt_lyst_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount,
            date
        FROM tt_lyst
        GROUP BY brand_name, {zone}, date
    ), cs_lyst AS (
        SELECT DISTINCT
            f.brand_name,
            f.{zone},
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(tt_lyst_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
            order_deal_date AS date
        FROM ads_crm.order_info_detail f
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
            AND f.{zone} = tt_lyst_num.{zone}
            AND f.order_deal_date = tt_lyst_num.date
        WHERE f.member_type = '会员'
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.sales_mode IN ({sales_modes})
            AND f.store_type IN ({store_types})
            AND f.store_level IN ({store_levels})
            AND f.channel_type IN ({channel_types})
            AND f.year_month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.year_month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
            AND f.vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
        GROUP BY f.brand_name, f.{zone}, tt_lyst_num.register_member_amount, order_deal_date
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array[f.{zone}] AS zone,
            cast(tt_num.register_member_amount AS INTEGER) AS register_member_amount,
            cast(COALESCE(TRY(tt_num.register_member_amount * 1.0000 / tt_lyst_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0)  AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
            cast(tt_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
            cast(1.0000 - COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
            cast(COALESCE(TRY((tt_num.register_member_amount - count(DISTINCT f.member_no)) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst,
            f.order_deal_date AS date
        FROM ads_crm.order_info_detail f
        INNER JOIN tt ON f.brand_name = tt.brand_name
            AND f.{zone} = tt.{zone}
            AND f.member_no = tt.member_no
            AND f.order_deal_date = tt.date
        INNER JOIN tt_num ON f.brand_name = tt_num.brand_name
            AND f.{zone} = tt_num.{zone}
            AND f.order_deal_date = tt_num.date
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
            AND f.{zone} = tt_lyst_num.{zone}
            AND f.order_deal_date - interval '1' year = tt_lyst_num.date
        INNER JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name
            AND f.{zone} = cs_lyst.{zone}
            AND f.order_deal_date - interval '1' year = cs_lyst.date
        WHERE f.member_type = '会员'
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.sales_mode IN ({sales_modes})
            AND f.store_type IN ({store_types})
            AND f.store_level IN ({store_levels})
            AND f.channel_type IN ({channel_types})
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
        GROUP BY
            f.brand_name,
            f.{zone},
            tt_num.register_member_amount,
            tt_lyst_num.register_member_amount,
            cs_lyst.consumed_member_amount,
            cs_lyst.unconsumed_member_amount,
            f.order_deal_date
    )
    SELECT DISTINCT
        l.brand,
        l.zone,
        COALESCE(d.register_member_amount, 0) AS register_member_amount,
        COALESCE(d.rma_compared_with_lyst, 0) AS rma_compared_with_lyst,
        COALESCE(d.consumed_member_amount, 0) AS consumed_member_amount,
        COALESCE(d.consumed_member_amount_proportion, 0) AS consumed_member_amount_proportion,
        COALESCE(d.cma_compared_with_lyst, 0) AS cma_compared_with_lyst,
        COALESCE(d.unconsumed_member_amount, 0) AS unconsumed_member_amount,
        COALESCE(d.unconsumed_member_amount_proportion, 0) AS unconsumed_member_amount_proportion,
        COALESCE(d.uma_compared_with_lyst, 0) AS uma_compared_with_lyst,
        l.date
    FROM l LEFT JOIN d ON l.brand = d.brand
        AND l.zone = d.zone
        AND l.date = d.date
"""

########################################################################################################################

MONTHLY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand_name AS brand,
            array[a.{zone}] AS zone,
            b.year_month
        FROM (
            SELECT DISTINCT
                brand_name,
                {zone},
                'key' AS key
            FROM ads_crm.member_analyse_fold_index_label
            WHERE brand_name IN ({brands})
                AND {zone} IN ({zones})
        ) a FULL JOIN (
            SELECT DISTINCT
                year_month,
                'key' AS key
            FROM ads_crm.order_info_detail
            WHERE year_month <= substr('{end_date}', 1, 7)
                AND year_month >= substr('{start_date}', 1, 7)
                AND vchr_date <= '{end_date}'
                AND vchr_date >= '{start_date}'
        ) b ON a.key = b.key
    ), tt AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no,
            substr(cast(date(member_register_time) AS VARCHAR), 1, 7) AS year_month
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}')
            AND date(member_register_time) <= date('{end_date}')
    ), tt_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount, year_month
        FROM tt
        GROUP BY brand_name, {zone}, year_month
    ), tt_lyst AS (
        SELECT DISTINCT
            brand_name,
            {zone},
            member_no,
            substr(cast(date(member_register_time) AS VARCHAR), 1, 7) AS year_month
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND sales_mode IN ({sales_modes})
            AND store_type IN ({store_types})
            AND store_level IN ({store_levels})
            AND channel_type IN ({channel_types})
            AND date(member_register_time) >= date('{start_date}') - interval '1' year
            AND date(member_register_time) <= date('{end_date}') - interval '1' year
    ), tt_lyst_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount,
            year_month
        FROM tt_lyst
        GROUP BY brand_name, {zone}, year_month
    ), cs_lyst AS (
        SELECT DISTINCT
            f.brand_name,
            f.{zone},
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(tt_lyst_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
            f.year_month
        FROM ads_crm.order_info_detail f
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
            AND f.{zone} = tt_lyst_num.{zone}
            AND f.year_month = tt_lyst_num.year_month
        WHERE f.member_type = '会员'
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.sales_mode IN ({sales_modes})
            AND f.store_type IN ({store_types})
            AND f.store_level IN ({store_levels})
            AND f.channel_type IN ({channel_types})
            AND f.year_month <= substr(cast(date('{end_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.year_month >= substr(cast(date('{start_date}') - interval '1' year AS VARCHAR), 1, 7)
            AND f.vchr_date <= cast(date('{end_date}') - interval '1' year AS VARCHAR)
            AND f.vchr_date >= cast(date('{start_date}') - interval '1' year AS VARCHAR)
        GROUP BY
            f.brand_name,
            f.{zone},
            tt_lyst_num.register_member_amount,
            f.year_month
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array[f.{zone}] AS zone,
            cast(tt_num.register_member_amount AS INTEGER) AS register_member_amount,
            cast(COALESCE(TRY(tt_num.register_member_amount * 1.0000 / tt_lyst_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_lyst,
            cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0)  AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / cs_lyst.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_lyst,
            cast(tt_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
            cast(1.0000 - COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion,
            cast(COALESCE(TRY((tt_num.register_member_amount - count(DISTINCT f.member_no)) * 1.0000 / cs_lyst.unconsumed_member_amount), 0) AS DECIMAL(18, 4)) AS uma_compared_with_lyst,
            f.year_month
        FROM ads_crm.order_info_detail f
        INNER JOIN tt ON f.brand_name = tt.brand_name
            AND f.{zone} = tt.{zone}
            AND f.member_no = tt.member_no
            AND f.year_month = tt.year_month
        INNER JOIN tt_num ON f.brand_name = tt_num.brand_name
            AND f.{zone} = tt_num.{zone}
            AND f.year_month = tt_num.year_month
        INNER JOIN tt_lyst_num ON f.brand_name = tt_lyst_num.brand_name
            AND f.{zone} = tt_lyst_num.{zone}
            AND substr(cast(f.order_deal_date - interval '1' year AS VARCHAR), 1, 7) = tt_lyst_num.year_month
        INNER JOIN cs_lyst ON f.brand_name = cs_lyst.brand_name
            AND f.{zone} = cs_lyst.{zone}
            AND substr(cast(f.order_deal_date - interval '1' year AS VARCHAR), 1, 7) = cs_lyst.year_month
        WHERE f.member_type = '会员'
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.sales_mode IN ({sales_modes})
            AND f.store_type IN ({store_types})
            AND f.store_level IN ({store_levels})
            AND f.channel_type IN ({channel_types})
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
        GROUP BY
            f.brand_name,
            f.{zone},
            tt_num.register_member_amount,
            tt_lyst_num.register_member_amount,
            cs_lyst.consumed_member_amount,
            cs_lyst.unconsumed_member_amount,
            f.year_month
    )
    SELECT DISTINCT
        l.brand,
        l.zone,
        COALESCE(d.register_member_amount, 0) AS register_member_amount,
        COALESCE(d.rma_compared_with_lyst, 0) AS rma_compared_with_lyst,
        COALESCE(d.consumed_member_amount, 0) AS consumed_member_amount,
        COALESCE(d.consumed_member_amount_proportion, 0) AS consumed_member_amount_proportion,
        COALESCE(d.cma_compared_with_lyst, 0) AS cma_compared_with_lyst,
        COALESCE(d.unconsumed_member_amount, 0) AS unconsumed_member_amount,
        COALESCE(d.unconsumed_member_amount_proportion, 0) AS unconsumed_member_amount_proportion,
        COALESCE(d.uma_compared_with_lyst, 0) AS uma_compared_with_lyst,
        l.year_month
    FROM l LEFT JOIN d ON l.brand = d.brand
        AND l.zone = d.zone
        AND l.year_month = d.year_month
"""
