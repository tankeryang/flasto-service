ALL = """
    WITH tt AS (
        SELECT brand_name, store_code,
        array_distinct(flatten(array_agg(register_member_array))) AS register_member_array,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        GROUP BY brand_name, store_code
    ), ytt AS (
        SELECT brand_name, store_code,
        cardinality(array_distinct(flatten(array_agg(register_member_array)))) AS register_member_amount
        FROM ads_crm.member_register_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '2' day
        GROUP BY brand_name, store_code
    ), yc AS (
        SELECT brand_name, store_code,
        cardinality(array_distinct(flatten(array_agg(customer_array)))) AS consumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '2' day
        GROUP BY brand_name, store_code
    ), tc AS (
        SELECT brand_name, store_code,
        cardinality(array_distinct(flatten(array_agg(customer_array)))) AS consumed_member_amount
        FROM ads_crm.member_analyse_fold_daily_income_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date <= date('{end_date}') - interval '1' day
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(tt.register_member_amount AS INTEGER) AS register_member_amount,
        cast(COALESCE(TRY(tt.register_member_amount * 1.0000 / ytt.register_member_amount), 0) AS DECIMAL(18, 4)) AS rma_compared_with_ystd,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS consumed_member_amount,
        cast(cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS consumed_member_amount_proportion,
        cast(COALESCE(TRY(tc.consumed_member_amount * 1.0000 / yc.consumed_member_amount), 0) AS DECIMAL(18, 4)) AS cma_compared_with_ystd,
        cast(tt.register_member_amount - cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) AS INTEGER) AS unconsumed_member_amount,
        cast(1.0000 - (cardinality(array_intersect(tt.register_member_array, array_distinct(flatten(array_agg(f.customer_array))))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS unconsumed_member_amount_proportion
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    LEFT JOIN ytt ON f.brand_name = ytt.brand_name AND f.store_code = ytt.store_code
    LEFT JOIN yc ON f.brand_name = yc.brand_name AND f.store_code = yc.store_code
    LEFT JOIN tc ON f.brand_name = tc.brand_name AND f.store_code = tc.store_code
    WHERE f.member_type = '会员' AND f.member_newold_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    GROUP BY
        f.brand_name, f.store_code,
        tt.register_member_amount, tt.register_member_array, ytt.register_member_amount,
        yc.consumed_member_amount, tc.consumed_member_amount
"""

########################################################################################################################

NEW_OLD = """
    WITH tt AS (
        SELECT brand_name, store_code,
        count(DISTINCT member_no) AS register_member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date(member_register_time) <= date('{end_date}') - INTERVAL '1' DAY
        GROUP BY brand_name, store_code
    )
    SELECT DISTINCT
        f.brand_name AS brand,
        f.store_code AS zone,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS new_member_amount,
        cast(cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS new_member_amount_proportion,
        cast(tt.register_member_amount - cardinality(array_distinct(flatten(array_agg(f.customer_array)))) AS INTEGER) AS old_member_amount,
        cast(1 - (cardinality(array_distinct(flatten(array_agg(f.customer_array)))) * 1.0000 / tt.register_member_amount) AS DECIMAL(18, 4)) AS old_member_amount_proportion
    FROM ads_crm.member_analyse_fold_daily_income_detail f
    LEFT JOIN tt ON f.brand_name = tt.brand_name AND f.store_code = tt.store_code
    WHERE f.member_newold_type = '新会员' AND f.member_type IS NULL AND f.member_level_type IS NULL
    AND f.brand_name IN ({brands})
    AND f.order_channel IN ({order_channels})
    AND f.store_code IN ({zones})
    AND f.date <= date('{end_date}') - interval '1' day
    GROUP BY f.brand_name, f.store_code, tt.register_member_amount
"""

########################################################################################################################

LEVEL = """
    WITH tt AS (
        SELECT brand_name, store_code,
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
        WHEN 14 THEN 'VIP会员'
        ELSE NULL END  AS member_level_type,
        cast(count(DISTINCT mi.member_no) AS INTEGER) AS member_level_amount,
        cast(count(DISTINCT mi.member_no) * 1.0000 / tt.register_member_amount AS DECIMAL(18, 4)) AS member_level_amount_proportion
    FROM cdm_crm.member_info_detail mi
    LEFT JOIN tt ON mi.brand_name = tt.brand_name AND mi.store_code = tt.store_code
    WHERE mi.brand_name IN ({brands})
    AND mi.store_code IN ({zones})
    AND date(mi.member_register_time) <= date('{end_date}') - interval '1' day
    GROUP BY mi.brand_name, mi.store_code, tt.register_member_amount,
    CASE mi.member_grade_id
    WHEN 13 THEN '普通会员'
    WHEN 14 THEN 'VIP会员'
    ELSE NULL END
"""

########################################################################################################################

REMAIN = """
    WITH tt AS (
        SELECT brand_name, store_code,
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
        SELECT brand_name, store_code,
        count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '1' DAY
        AND date(member_last_order_time) >= date('{end_date}') - interval '1' year
        GROUP BY brand_name, store_code
    ), t_36 AS (
        SELECT brand_name, store_code,
        count(DISTINCT member_no) AS member_amount
        FROM cdm_crm.member_info_detail
        WHERE brand_name IN ({brands})
        AND store_code IN ({zones})
        AND date(member_last_order_time) <= date('{end_date}') - INTERVAL '3' month
        AND date(member_last_order_time) >= date('{end_date}') - interval '6' month
        GROUP BY brand_name, store_code
    ), t_69 AS (
        SELECT brand_name, store_code,
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
    GROUP BY mi.brand_name, mi.store_code, tt.member_amount, t_36.member_amount, t_69.member_amount
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
