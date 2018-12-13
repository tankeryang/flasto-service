DAILY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand_name AS brand,
            array[a.{zone}] AS zone,
            a.member_register_type,
            b.date
        FROM (
            SELECT DISTINCT
                brand_name,
                member_register_type,
                {zone},
                'key' AS key
            FROM ads_crm.member_recruit_analyse_fold_index_label
            WHERE brand_name IN ({brands})
                AND member_register_type IS NOT NULL
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
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array[f.{zone}] AS zone,
            f.member_register_type,
            cast(COALESCE(count(DISTINCT f.member_no), 0) AS INTEGER) AS member_amount,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
            f.order_deal_date AS date
        FROM ads_crm.order_info_detail f
        LEFT JOIN tt_num ON f.brand_name = tt_num.brand_name
            AND f.{zone} = tt_num.{zone}
            AND f.order_deal_date = tt_num.date
        WHERE f.member_register_type IS NOT NULL
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
        GROUP BY
            f.brand_name,
            f.{zone},
            f.member_register_type,
            f.order_deal_date,
            tt_num.register_member_amount
    )
    SELECT DISTINCT
        l.brand,
        l.zone,
        l.member_register_type,
        COALESCE(d.member_amount, 0) AS member_amount,
        COALESCE(d.member_amount_proportion, 0) AS member_amount_proportion,
        l.date
    FROM l LEFT JOIN d ON l.brand = d.brand
        AND l.zone = d.zone
        AND l.member_register_type = d.member_register_type
        AND l.date = d.date
"""

########################################################################################################################

MONTHLY = """
    WITH l AS (
        SELECT DISTINCT
            a.brand_name AS brand,
            array[a.{zone}] AS zone,
            a.member_register_type,
            b.year_month
        FROM (
            SELECT DISTINCT
                brand_name,
                member_register_type,
                {zone},
                'key' AS key
            FROM ads_crm.member_recruit_analyse_fold_index_label
            WHERE brand_name IN ({brands})
                AND member_register_type IS NOT NULL
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
            AND date(member_register_time) >= date('{start_date}')
            AND date(member_register_time) <= date('{end_date}')
    ), tt_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount, year_month
        FROM tt
        GROUP BY brand_name, {zone}, year_month
    ), d AS (
        SELECT DISTINCT
            f.brand_name AS brand,
            array[f.{zone}] AS zone,
            f.member_register_type,
            cast(COALESCE(count(DISTINCT f.member_no), 0) AS INTEGER) AS member_amount,
            cast(COALESCE(TRY(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount), 0) AS DECIMAL(18, 4)) AS member_amount_proportion,
            f.year_month
        FROM ads_crm.order_info_detail f
        LEFT JOIN tt_num ON f.brand_name = tt_num.brand_name
            AND f.{zone} = tt_num.{zone}
            AND f.year_month = tt_num.year_month
        WHERE f.member_register_type IS NOT NULL
            AND f.brand_name IN ({brands})
            AND f.order_channel IN ({order_channels})
            AND f.{zone} IN ({zones})
            AND f.year_month <= substr('{end_date}', 1, 7)
            AND f.year_month >= substr('{start_date}', 1, 7)
            AND f.vchr_date <= '{end_date}'
            AND f.vchr_date >= '{start_date}'
        GROUP BY
            f.brand_name,
            f.{zone},
            f.member_register_type,
            f.year_month,
            tt_num.register_member_amount
    )
    SELECT DISTINCT
        l.brand,
        l.zone,
        l.member_register_type,
        COALESCE(d.member_amount, 0) AS member_amount,
        COALESCE(d.member_amount_proportion, 0) AS member_amount_proportion,
        l.year_month
    FROM l LEFT JOIN d ON l.brand = d.brand
        AND l.zone = d.zone
        AND l.member_register_type = d.member_register_type
        AND l.year_month = d.year_month
"""
