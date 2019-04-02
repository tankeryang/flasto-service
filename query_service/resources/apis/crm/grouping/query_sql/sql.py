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

# 查询分组详情分页 =======================================================================================================
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
            mid.member_last_order_time_ty,
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
        member_last_order_time_ty,
        member_reg_source
    FROM tmp
    WHERE id BETWEEN {start} AND {end}
"""

# 查询分组总数 ===========================================================================================================
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
            mid.member_last_order_time_ty,
            mid.member_reg_source
        FROM cdm_crm.member_info_detail mid
        {join_sql}
        WHERE mid.brand_code = '{brand_code}'
    )
    SELECT
        COUNT(member_no) AS total
    FROM tmp
"""

# 导出分组详情 ===========================================================================================================
MEMBER_GROUPING_DETAIL_CSV = """
    WITH {with_sql}
    SELECT DISTINCT
        mid.channel_type,
        mid.sales_area,
        mid.city,
        mid.store_code,
        mid.member_manage_clerk,
        mid.member_ec_status,
        mid.member_no,
        mid.member_card,
        mid.member_mobile,
        mid.member_name,
        mid.member_gender,
        mid.member_grade_name,
        mid.member_grade_expiration,
        mid.member_score,
        mid.member_will_score,
        mid.member_wechat_id,
        mid.member_birthday,
        mid.member_register_time,
        mid.member_last_order_time_ty,
        mid.member_last_feedback_time,
        mid.member_reg_source
    FROM cdm_crm.member_info_detail mid
    {join_sql}
    WHERE mid.brand_code = '{brand_code}'
"""

# 查询分组会员编号列表 ====================================================================================================
MEMBER_GROUPING_NO_LIST = """
    WITH {with_sql}
    SELECT DISTINCT
        mid.member_no
    FROM cdm_crm.member_info_detail mid
    {join_sql}
    WHERE mid.brand_code = '{brand_code}'
"""
