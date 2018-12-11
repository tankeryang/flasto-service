ALL = """
    WITH tt AS (
        SELECT DISTINCT
            brand_name, {zone}, member_no
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
        AND date(member_register_time) <= date('{end_date}') - interval '1' day
    ), tt_num AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount
        FROM tt
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        cast(tt_num.register_member_amount AS INTEGER) AS register_member_amount,
        cast(count(DISTINCT f.member_no) AS INTEGER) AS consumed_member_amount,
        cast(count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(tt_num.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - (count(DISTINCT f.member_no) * 1.0000 / tt_num.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion
    FROM ads_crm.order_info_detail f
    INNER JOIN tt ON f.brand_name = tt.brand_name
        AND f.{zone} = tt.{zone}
        AND f.member_no = tt.member_no
    INNER JOIN tt_num ON f.brand_name = tt_num.brand_name
        AND f.{zone} = tt_num.{zone}
    WHERE f.member_type = '会员'
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.{zone} IN ({zones})
        AND f.year_month <= substr('{end_date}', 1, 7)
        AND f.vchr_date <= cast(date('{end_date}') - interval '1' day AS VARCHAR)
    GROUP BY f.brand_name, f.{zone}, tt_num.register_member_amount
"""

########################################################################################################################

NEW_OLD = """
    WITH tt AS (
        SELECT
            brand_name,
            {zone},
            count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND {zone} IN ({zones})
            AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, {zone}
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.{zone} AS zone,
        cast(count(DISTINCT f.member_no) AS INTEGER) AS new_member_amount,
        cast(count(DISTINCT f.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS new_member_amount_proportion,
        cast(tt.register_member_amount - count(DISTINCT f.member_no) AS INTEGER) AS old_member_amount,
        cast(1 - (count(DISTINCT f.member_no) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS old_member_amount_proportion
    FROM ads_crm.order_info_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.{zone} = tt.{zone}
    WHERE f.member_newold_type = '新会员'
        AND f.brand_name IN ({brands})
        AND f.order_channel IN ({order_channels})
        AND f.{zone} IN ({zones})
        AND f.year_month <= substr('{end_date}', 1, 7)
        AND f.vchr_date <= cast(date('{end_date}') - interval '1' day AS VARCHAR)
    GROUP BY f.brand_name, f.{zone}, tt.register_member_amount
"""

########################################################################################################################

LEVEL = """
    WITH tt AS (
        SELECT
            brand_name,
            store_code,
            count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND store_code IN ({zones})
            AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.store_code     AS zone,
        CASE mi.member_grade_id
            WHEN 13 THEN '普通会员'
            WHEN 9 THEN '普通会员'
            WHEN 14 THEN 'VIP会员'
            WHEN 10 THEN 'VIP会员'
            WHEN 11 THEN 'VIP会员'
        ELSE NULL END  AS member_level_type,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS member_level_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS member_level_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.store_code = tt.store_code
    WHERE mi.brand_name IN ({brands})
        AND mi.store_code IN ({zones})
        AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    GROUP BY
        mi.brand_name,
        mi.store_code,
        tt.register_member_amount,
        CASE mi.member_grade_id
            WHEN 13 THEN '普通会员'
            WHEN 9 THEN '普通会员'
            WHEN 14 THEN 'VIP会员'
            WHEN 10 THEN 'VIP会员'
            WHEN 11 THEN 'VIP会员'
        ELSE NULL END
"""

########################################################################################################################

REMAIN = """
    WITH tt AS (
        SELECT
            brand_name,
            store_code,
            count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND store_code IN ({zones})
            AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.store_code AS zone,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS remain_member_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS remain_member_amount_proportion,
        cast(tt.register_member_amount - count(DISTINCT mi.member_no) AS INTEGER) AS lost_member_amount,
        cast(1.0000 - count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS lost_member_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.store_code = tt.store_code
    WHERE mi.brand_name IN ({brands})
        AND mi.store_code IN ({zones})
        AND date(mi.member_last_order_time) <= date('{end_date}') - interval '1' day
        AND date(mi.member_last_order_time) >= date('{end_date}') - interval '1' year
    GROUP BY mi.brand_name, mi.store_code, tt.register_member_amount
"""

########################################################################################################################

ACTIVE = """
    WITH tt AS (
        SELECT
            brand_name,
            store_code,
            count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND store_code IN ({zones})
            AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '1' DAY
            AND date(member_last_order_time) >= date('{end_date}') - interval '1' year
        GROUP BY brand_name, store_code
    ), t_36 AS (
        SELECT
            brand_name,
            store_code,
            count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND store_code IN ({zones})
            AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '3' month
            AND date(member_last_order_time) >= date('{end_date}') - interval '6' month
        GROUP BY brand_name, store_code
    ), t_69 AS (
        SELECT
            brand_name,
            store_code,
            count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
            AND store_code IN ({zones})
            AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '6' month
            AND date(member_last_order_time) >= date('{end_date}') - interval '9' month
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        mi.brand_name AS brand,
        mi.store_code AS zone,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS active_member_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS active_member_amount_proportion,
        cast(t_36.member_amount AS INTEGER) AS silent_member_amount,
        cast(t_36.member_amount * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS silent_member_amount_proportion,
        cast(t_69.member_amount AS INTEGER) AS sleep_member_amount,
        cast(t_69.member_amount * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS sleep_member_amount_proportion,
        cast(tt.member_amount - (count(DISTINCT mi.member_no) + t_36.member_amount + t_69.member_amount) AS INTEGER) AS pre_lost_member_amount,
        cast(1 - (count(DISTINCT mi.member_no) + t_36.member_amount + t_69.member_amount) * 1.0000 / tt.member_amount AS DECIMAL(18, 4)) AS pre_lost_member_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.store_code = tt.store_code
    LEFT JOIN t_36 ON mi.brand_name = t_36.brand_name AND mi.store_code = t_36.store_code
    LEFT JOIN t_69 ON mi.brand_name = t_69.brand_name AND mi.store_code = t_69.store_code
    WHERE mi.brand_name IN ({brands})
        AND mi.store_code IN ({zones})
        AND date(mi.member_last_order_time) <= date('{end_date}') - interval '1' day
        AND date(mi.member_last_order_time) >= date('{end_date}') - interval '3' month
    GROUP BY
        mi.brand_name,
        mi.store_code,
        tt.member_amount,
        t_36.member_amount,
        t_69.member_amount
"""

########################################################################################################################

TIME = """
    WITH t AS (
        SELECT
            mi.brand_name,
            mi.store_code,
            mi.member_no,
            IF (mi.member_register_time IS NOT NULL,
                CASE
                WHEN (
                    DATE(mi.member_register_time) <= DATE('{end_date}') - INTERVAL '1' DAY
                    AND DATE(mi.member_register_time) > DATE('{end_date}') - INTERVAL '1' month
                ) THEN '<1'
                WHEN (
                    DATE(mi.member_register_time) <= DATE('{end_date}') - INTERVAL '1' month
                    AND DATE(mi.member_register_time) >= DATE('{end_date}') - INTERVAL '2' month
                ) THEN '1-2'
                WHEN (
                    DATE(mi.member_register_time) <= DATE('{end_date}') - INTERVAL '3' month
                    AND DATE(mi.member_register_time) >= DATE('{end_date}') - INTERVAL '4' month
                ) THEN '3-4'
                WHEN (
                    DATE(mi.member_register_time) <= DATE('{end_date}') - INTERVAL '5' month
                ) THEN '>5'
                ELSE NULL END,
                NULL
            ) time
        FROM cdm_crm.member_info_detail mi
        WHERE mi.brand_name IN ({brands})
            AND mi.store_code IN ({zones})
            AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        time
    FROM t WHERE time IS NOT NULL
    GROUP BY brand_name, store_code, time
"""

########################################################################################################################

DISCOUNT = """
    WITH d AS (
        SELECT
            oi.brand_name,
            oi.store_code,
            oi.member_no,
            CASE
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) < 0.5
            ) THEN '<50'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) < 0.7
                AND sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) >= 0.5
            ) THEN '50-69'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) < 0.9
                AND sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) >= 0.7
            ) THEN '70-89'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / sum(oi.order_amount) >= 0.9
            ) THEN '>=90'
            ELSE NULL END discount
        FROM cdm_crm.order_info_detail oi
        WHERE oi.order_amount > 0
            AND oi.brand_name IN ({brands})
            AND oi.store_code IN ({zones})
            AND date(oi.order_deal_time) <= date('{end_date}') - interval '1' day
        GROUP BY oi.brand_name, oi.store_code, oi.member_no
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        discount
    FROM d WHERE discount IS NOT NULL
    GROUP BY brand_name, store_code, discount
"""

########################################################################################################################

SI_PO = """
    WITH s AS (
        SELECT
            oi.brand_name,
            oi.store_code,
            oi.member_no,
            CASE
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) < 1400
            ) THEN '<1400'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) < 1800
                AND sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) >= 1400
            ) THEN '1400-1799'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) < 2200
                AND sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) >= 1800
            ) THEN '1800-2199'
            WHEN (
                sum(oi.order_fact_amount) * 1.0 / count(distinct outer_order_no) >= 2200
            ) THEN '>=2200'
            ELSE NULL END sales_income_per_order
        FROM cdm_crm.order_info_detail oi
        WHERE oi.order_item_quantity > 0
            AND oi.brand_name IN ({brands})
            AND oi.store_code IN ({zones})
            AND date(oi.order_deal_time) <= date('{end_date}') - interval '1' day
        GROUP BY oi.brand_name, oi.store_code, oi.member_no
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        sales_income_per_order
    FROM s WHERE sales_income_per_order IS NOT NULL
    GROUP BY brand_name, store_code, sales_income_per_order
"""

########################################################################################################################

RECENCY = """
    WITH r AS (
        SELECT
            mi.brand_name,
            mi.store_code,
            mi.member_no,
            IF (mi.member_last_order_time IS NOT NULL,
                CASE
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '1' DAY
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '3' month
                ) THEN '<3'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '3' month
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '5' month
                ) THEN '3-5'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '6' month
                    AND DATE(mi.member_last_order_time) >= DATE('{end_date}') - INTERVAL '8' month
                ) THEN '6-8'
                WHEN (
                    DATE(mi.member_last_order_time) <= DATE('{end_date}') - INTERVAL '9' month
                ) THEN '>9'
                ELSE NULL END,
                NULL
            ) recency
        FROM cdm_crm.member_info_detail mi
        WHERE mi.brand_name IN ({brands})
            AND mi.store_code IN ({zones})
            AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        recency
    FROM r WHERE recency IS NOT NULL
    GROUP BY brand_name, store_code, recency
"""

########################################################################################################################

FREQUENCY = """
    WITH f AS (
        SELECT
            mi.brand_name,
            mi.store_code,
            mi.member_no,
            IF (count(distinct oi.outer_order_no) IS NOT NULL,
                CASE count(distinct oi.outer_order_no)
                WHEN 1 THEN '1'
                WHEN 2 THEN '2'
                WHEN 3 THEN '3'
                WHEN 4 THEN '>=4'
                ELSE '>=4' END,
                NULL
            ) frequency
        FROM cdm_crm.member_info_detail mi
        LEFT JOIN ods_crm.order_info oi ON mi.member_no = oi.member_no
        WHERE mi.brand_name IN ({brands})
            AND mi.store_code IN ({zones})
            AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
        GROUP BY mi.member_no, mi.brand_name, mi.store_code
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        frequency
    FROM f WHERE frequency IS NOT NULL
    GROUP BY brand_name, store_code, frequency
"""

########################################################################################################################

MONETARY = """
    WITH m AS (
        SELECT
            mi.brand_name,
            mi.store_code,
            mi.member_no,
            IF (sum(oi.order_fact_amount) IS NOT NULL,
                CASE
                    WHEN (
                        sum(oi.order_fact_amount) < 1500
                    ) THEN '<1500'
                    WHEN (
                        sum(oi.order_fact_amount) < 3800
                        AND sum(oi.order_fact_amount) >= 1500
                    ) THEN '1500-3799'
                    WHEN (
                        sum(oi.order_fact_amount) < 5000
                        AND sum(oi.order_fact_amount) >= 3800
                    ) THEN '3800-4999'
                    WHEN (
                        sum(oi.order_fact_amount) >= 5000
                    ) THEN '>5000'
                    ELSE NULL END,
                NULL
            ) monetary
        FROM cdm_crm.member_info_detail mi
        LEFT JOIN ods_crm.order_info oi ON mi.member_no = oi.member_no
        WHERE mi.brand_name IN ({brands})
            AND mi.store_code IN ({zones})
            AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
        GROUP BY mi.member_no, mi.brand_name, mi.store_code
    )
    SELECT DISTINCT
        brand_name AS brand,
        store_code AS zone,
        cast(count(distinct member_no) AS INTEGER) AS member_amount,
        monetary
    FROM m WHERE monetary IS NOT NULL
    GROUP BY brand_name, store_code, monetary
"""