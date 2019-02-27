MEMBER_INFO = """
    SELECT DISTINCT member_no FROM ads_crm.member_grouping_info_detail mgid
    WHERE 1 = 1 AND brand_code = '{brand_code}'
    {condition_sql}
"""

COUPON_INFO_WITH_AMOUNT = """
    WITH t AS (
        SELECT
            member_no,
            COUNT(DISTINCT coupon_no) AS coupon_amount
        FROM cdm_crm.member_coupon_info_detail
        WHERE 1 = 1 AND brand_code = '{brand_code}'
        {condition_sql}
        GROUP BY member_no
    )
    SELECT DISTINCT member_no FROM t
    WHERE 1 = 1 {coupon_condition_sql}
"""

COUPON_INFO = """
    SELECT DISTINCT member_no FROM cdm_crm.member_coupon_info_detail
    WHERE 1 = 1 AND brand_code = '{brand_code}'
    {condition_sql}
"""

CML_CONSUMPTION_INFO = """
    WITH t AS (
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
    SELECT DISTINCT member_no FROM t
    WHERE 1 = 1
    {condition_sql}
"""
