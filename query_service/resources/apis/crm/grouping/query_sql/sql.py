# 查询分组详情和导出的sql =================================================================================================
MEMBER_INFO = """
    mi AS (
        SELECT DISTINCT member_no FROM ads_crm.member_grouping_info_detail mgid
        WHERE 1 = 1 AND brand_code = '{brand_code}'
        {condition_sql}
    )
"""

COUPON_INFO_WITH_AMOUNT = """
    ciwa AS (
        WITH ciwa_t AS (
            SELECT
                member_no,
                COUNT(DISTINCT coupon_no) AS coupon_amount
            FROM cdm_crm.member_coupon_info_detail
            WHERE 1 = 1 AND brand_code = '{brand_code}'
            {condition_sql}
            GROUP BY member_no
        )
        SELECT DISTINCT member_no FROM ciwa_t
        WHERE 1 = 1 {coupon_condition_sql}
    )
"""

COUPON_INFO = """
    ci AS (
        SELECT DISTINCT member_no FROM cdm_crm.member_coupon_info_detail
        WHERE 1 = 1 AND brand_code = '{brand_code}'
        {condition_sql}
    )
"""

CML_CONSUMPTION_INFO = """
    cci AS (
        WITH cci_t AS (
            SELECT
                member_no,
                SUM(cml_consumption_times) AS cml_consumption_times,
                SUM(cml_consumption_item_quantity) AS cml_consumption_item_quantity,
                COUNT(DISTINCT cml_order_deal_date) AS cml_consumption_days,
                COUNT(DISTINCT vchr_cml_order_deal_year_month) AS cml_consumption_months,
                SUM(cml_consumption_amount) AS cml_consumption_amount,
                SUM(cml_consumption_amount_include_coupon) AS cml_consumption_amount_include_coupon,
                SUM(cml_return_times) AS cml_return_times,
                SUM(cml_return_amount) AS cml_return_amount,
                COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_retail_amount) * 1.0), 0) AS cml_avg_discount,
                COALESCE(TRY(SUM(cml_consumption_amount_include_coupon) / SUM(cml_consumption_retail_amount) * 1.0), 0) AS cml_avg_discount_include_coupon,
                COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_times) * 1.0), 0) AS cml_avg_sales_amount_per_order,
                COALESCE(TRY(SUM(cml_consumption_item_quantity) / SUM(cml_consumption_times) * 1.0), 0) AS cml_avg_sales_item_per_order,
                COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_item_quantity) * 1.0), 0) AS cml_avg_sales_amount_per_item
            FROM ads_crm.member_cumulative_consumption_daily_detail
            WHERE brand_code = '{brand_code}'
                {condition_sql_cml_consumption_store}
                AND vchr_cml_order_deal_year_month >= SUBSTR('{start_date}', 1, 7)
                AND vchr_cml_order_deal_year_month <= SUBSTR('{end_date}', 1, 7)
                AND vchr_cml_order_deal_date >= '{start_date}'
                AND vchr_cml_order_deal_date <= '{end_date}'
            GROUP BY member_no
        )
        SELECT DISTINCT member_no FROM cci_t
        WHERE 1 = 1
        {condition_sql}
    )
"""

MEMBER_GROUPING_DETAIL = """
    WITH tmp AS (
        WITH {with_sql}
        SELECT DISTINCT
            mid.brand_code,
            mid.member_no,
            mid.member_name,
            mid.member_wechat_id,
            mid.member_mobile,
            mid.member_grade_name,
            mid.member_first_order_time,
            mid.member_reg_source,
            row_number() OVER (
                PARTITION BY mid.brand_code
                ORDER BY mid.member_no
            ) AS id
        FROM cdm_crm.member_info_detail mid
        {join_sql}
        WHERE mid.brand_code = '{brand_code}'
    )
    SELECT
        member_no,
        member_name,
        member_wechat_id,
        member_mobile,
        member_grade_name,
        member_first_order_time,
        member_reg_source
    FROM tmp
    WHERE id BETWEEN {start} AND {end}
"""

MEMBER_GROUPING_COUNT = """
    WITH tmp AS (
        WITH {with_sql}
        SELECT DISTINCT
            mid.brand_code,
            mid.member_no,
            mid.member_name,
            mid.member_wechat_id,
            mid.member_mobile,
            mid.member_grade_name,
            mid.member_first_order_time,
            mid.member_reg_source
        FROM cdm_crm.member_info_detail mid
        {join_sql}
        WHERE mid.brand_code = '{brand_code}'
    )
    SELECT
        COUNT(member_no) AS total
    FROM tmp
"""

# 查询分组总人数的sql ====================================================================================================
COUNT_MEMBER_INFO = """
    SELECT DISTINCT member_no FROM ads_crm.member_grouping_info_detail mgid
    WHERE 1 = 1 AND brand_code = '{brand_code}'
    {condition_sql}
"""

COUNT_COUPON_INFO_WITH_AMOUNT = """
    WITH ciwa_t AS (
        SELECT
            member_no,
            COUNT(DISTINCT coupon_no) AS coupon_amount
        FROM cdm_crm.member_coupon_info_detail
        WHERE 1 = 1 AND brand_code = '{brand_code}'
        {condition_sql}
        GROUP BY member_no
    )
    SELECT DISTINCT member_no FROM ciwa_t
    WHERE 1 = 1 {coupon_condition_sql}
"""

COUNT_COUPON_INFO = """
    SELECT DISTINCT member_no FROM cdm_crm.member_coupon_info_detail
    WHERE 1 = 1 AND brand_code = '{brand_code}'
    {condition_sql}
"""

COUNT_CML_CONSUMPTION_INFO = """
    WITH cci_t AS (
        SELECT
            member_no,
            SUM(cml_consumption_times) AS cml_consumption_times,
            SUM(cml_consumption_item_quantity) AS cml_consumption_item_quantity,
            COUNT(DISTINCT cml_order_deal_date) AS cml_consumption_days,
            COUNT(DISTINCT vchr_cml_order_deal_year_month) AS cml_consumption_months,
            SUM(cml_consumption_amount) AS cml_consumption_amount,
            SUM(cml_consumption_amount_include_coupon) AS cml_consumption_amount_include_coupon,
            SUM(cml_return_times) AS cml_return_times,
            SUM(cml_return_amount) AS cml_return_amount,
            COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_retail_amount) * 1.0), 0) AS cml_avg_discount,
            COALESCE(TRY(SUM(cml_consumption_amount_include_coupon) / SUM(cml_consumption_retail_amount) * 1.0), 0) AS cml_avg_discount_include_coupon,
            COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_times) * 1.0), 0) AS cml_avg_sales_amount_per_order,
            COALESCE(TRY(SUM(cml_consumption_item_quantity) / SUM(cml_consumption_times) * 1.0), 0) AS cml_avg_sales_item_per_order,
            COALESCE(TRY(SUM(cml_consumption_amount) / SUM(cml_consumption_item_quantity) * 1.0), 0) AS cml_avg_sales_amount_per_item
        FROM ads_crm.member_cumulative_consumption_daily_detail
        WHERE brand_code = '{brand_code}'
            {condition_sql_cml_consumption_store}
            AND vchr_cml_order_deal_year_month >= SUBSTR('{start_date}', 1, 7)
            AND vchr_cml_order_deal_year_month <= SUBSTR('{end_date}', 1, 7)
            AND vchr_cml_order_deal_date >= '{start_date}'
            AND vchr_cml_order_deal_date <= '{end_date}'
        GROUP BY member_no
    )
    SELECT DISTINCT member_no FROM cci_t
    WHERE 1 = 1
    {condition_sql}
"""
