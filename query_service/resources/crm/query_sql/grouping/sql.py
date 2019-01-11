MEMBER_INFO = """
    SELECT member_no FROM ads_crm.member_grouping_info_detail mgid
    WHERE mgid.flag = 1 AND brand_code = {brand_code}
    {condition_sql}
"""

COUPON_INFO = """
    WITH t AS (
        SELECT
            COUNT(DISTINCT coupon_no) AS coupon_amount,
            
    )
"""