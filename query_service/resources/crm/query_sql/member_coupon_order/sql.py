QUERY = """
    SELECT
        -- 券批次类型
        CASE coupon_category
            WHEN 'Cash' THEN '现金券'
            WHEN 'Discount' THEN '折扣券'
        ELSE '其他' END AS coupon_category,
        -- 券批次类型描述
        CASE coupon_type_detail
            WHEN 'CouponBirthday' THEN '生日券'
            WHEN 'ScoreConvert' THEN '积分兑换'
            WHEN 'Activity' THEN '活动券'
            WHEN 'JoinMember' THEN '入会券'
            WHEN 'MaintainMember' THEN '顾客维系券'
            WHEN 'Fan' THEN '粉丝券'
            WHEN 'Other' THEN '其他'
        ELSE NULL END AS coupon_type_detail,
        -- 券活动名称
        coupon_name,
        -- 券批次号
        coupon_template_no,
        -- 券号
        coupon_no,
        -- 券面额
        coupon_denomination,
        -- 券状态
        CASE coupon_status
            WHEN '-1' THEN '过期'
            WHEN '0' THEN '未到时间'
            WHEN '15' THEN '禁用'
            WHEN '7' THEN '有效'
            WHEN '11' THEN '已使用'
            WHEN '-2' THEN '取消'
        ELSE '其他' END AS coupon_status,
        -- 券生效日期
        CAST(coupon_start_time AS VARCHAR) AS coupon_start_time,
        -- 券失效日期
        CAST(coupon_end_time AS VARCHAR) AS coupon_end_time,
        -- 券绑定日期
        CAST(coupon_batch_time AS VARCHAR) AS coupon_batch_time,
        -- 券使用日期
        CAST(coupon_used_time AS VARCHAR) AS coupon_used_time,
        -- 管理门店编号
        member_manage_store_code AS member_manage_store_code,
        -- 管理门店
        member_manage_store_name AS member_manage_store_name,
        -- 会员编号
        member_no,
        -- OpenID
        member_wechat_id AS member_wechat_id,
        -- 会员名称
        member_name AS member_name,
        -- 会员手机号
        member_mobile AS member_mobile,
        -- 消费会员当前等级
        CASE order_grade_id
            WHEN 13 THEN 'Five Plus-普通会员'
            WHEN 9  THEN 'M60-普通会员'
            WHEN 5  THEN 'Trendiano-普通会员'
            WHEN 14 THEN 'FIve Plus-VIP会员'
            WHEN 10 THEN 'M60-银卡会员'
            WHEN 11 THEN 'M60-金卡会员'
            WHEN 6  THEN 'Trendiano-银卡会员'
            WHEN 7  THEN 'Trendiano-金卡会员'
            WHEN 8  THEN 'Trendiano-黑卡会员'
        ELSE NULL END AS order_grade_id,
        -- 消费渠道
        order_trade_source AS order_trade_source,
        -- 消费门店编号
        order_store_code AS order_store_code,
        -- 消费门店名称
        order_store_name AS order_store_name,
        -- 券使用订单编号
        coupon_used_order_no AS coupon_used_order_no,
        -- 销售金额 (未扣券)
        order_fact_amount AS order_fact_amount,
        -- 销售金额 (扣券)
        order_fact_amount_include_coupon AS order_fact_amount_include_coupon,
        -- 吊牌金额
        order_retail_amount AS order_retail_amount,
        -- 订单件数
        CAST(order_item_quantity AS DECIMAL(18, 2)) AS order_item_quantity,
        -- 订单折扣
        order_discount AS order_discount,
        -- 券密码
        coupon_passcode
    FROM ads_crm.member_coupon_order_info_detail
    WHERE 1 = 1
    {condition_sql}
"""

EXPORT = """
    SELECT
        -- 券批次类型
        CASE coupon_category
            WHEN 'Cash' THEN '现金券'
            WHEN 'Discount' THEN '折扣券'
        ELSE '其他' END AS coupon_category,
        -- 券批次类型描述
        CASE coupon_type_detail
            WHEN 'CouponBirthday' THEN '生日券'
            WHEN 'ScoreConvert' THEN '积分兑换'
            WHEN 'Activity' THEN '活动券'
            WHEN 'JoinMember' THEN '入会券'
            WHEN 'MaintainMember' THEN '顾客维系券'
            WHEN 'Fan' THEN '粉丝券'
            WHEN 'Other' THEN '其他'
        ELSE '' END AS coupon_type_detail,
        -- 券活动名称
        coupon_name,
        -- 券批次号
        coupon_template_no,
        -- 券号
        coupon_no,
        -- 券面额
        coupon_denomination,
        -- 券状态
        CASE coupon_status
            WHEN '-1' THEN '过期'
            WHEN '0' THEN '未到时间'
            WHEN '15' THEN '禁用'
            WHEN '7' THEN '有效'
            WHEN '11' THEN '已使用'
            WHEN '-2' THEN '取消'
        ELSE '其他' END AS coupon_status,
        -- 券生效日期
        IF(coupon_start_time IS NOT NULL, CAST(coupon_start_time AS VARCHAR), '') AS coupon_start_time,
        -- 券失效日期
        IF(coupon_end_time IS NOT NULL, CAST(coupon_end_time AS VARCHAR), '') AS coupon_end_time,
        -- 券绑定日期
        IF(coupon_batch_time IS NOT NULL, CAST(coupon_batch_time AS VARCHAR), '') AS coupon_batch_time,
        -- 券使用日期
        IF(coupon_used_time IS NOT NULL, CAST(coupon_used_time AS VARCHAR), '') AS coupon_used_time,
        -- 管理门店编号
        IF(member_manage_store_code IS NOT NULL, member_manage_store_code, '') AS member_manage_store_code,
        -- 管理门店
        IF(member_manage_store_name IS NOT NULL , member_manage_store_name, '') AS member_manage_store_name,
        -- 会员编号
        IF(member_no IS NOT NULL, member_no, '') AS member_no,
        -- OpenID
        IF(member_wechat_id IS NOT NULL, member_wechat_id, '') AS member_wechat_id,
        -- 会员名称
        IF(member_name IS NOT NULL, member_name, '') AS member_name,
        -- 会员手机号
        IF(member_mobile IS NOT NULL, member_mobile, '') AS member_mobile,
        -- 消费会员当前等级
        CASE order_grade_id
            WHEN 13 THEN 'Five Plus-普通会员'
            WHEN 9  THEN 'M60-普通会员'
            WHEN 5  THEN 'Trendiano-普通会员'
            WHEN 14 THEN 'FIve Plus-VIP会员'
            WHEN 10 THEN 'M60-银卡会员'
            WHEN 11 THEN 'M60-金卡会员'
            WHEN 6  THEN 'Trendiano-银卡会员'
            WHEN 7  THEN 'Trendiano-金卡会员'
            WHEN 8  THEN 'Trendiano-黑卡会员'
        ELSE '' END AS order_grade_id,
        -- 消费渠道
        IF(order_trade_source IS NOT NULL, order_trade_source, '') AS order_trade_source,
        -- 消费门店编号
        IF(order_store_code IS NOT NULL, order_store_code, '') AS order_store_code,
        -- 消费门店名称
        IF(order_store_name IS NOT NULL, order_store_name, '') AS order_store_name,
        -- 券使用订单编号
        IF(coupon_used_order_no IS NOT NULL, coupon_used_order_no, '') AS coupon_used_order_no,
        -- 销售金额 (未扣券)
        IF(order_fact_amount IS NOT NULL, CAST(order_fact_amount AS VARCHAR), '') AS order_fact_amount,
        -- 销售金额 (扣券)
        IF(order_fact_amount_include_coupon IS NOT NULL, CAST(order_fact_amount_include_coupon AS VARCHAR), '') AS order_fact_amount_include_coupon,
        -- 吊牌金额
        IF(order_retail_amount IS NOT NULL, CAST(order_retail_amount AS VARCHAR), '') AS order_retail_amount,
        -- 订单件数
        IF(order_item_quantity IS NOT NULL, CAST(order_item_quantity AS VARCHAR), '') AS order_item_quantity,
        -- 订单折扣
        IF(order_discount IS NOT NULL, CAST(order_discount AS VARCHAR), '') AS order_discount,
        -- 券密码
        IF(coupon_passcode IS NOT NULL, CONCAT('[', coupon_passcode, ']'), '') AS coupon_passcode
    FROM ads_crm.member_coupon_order_info_detail
    WHERE 1 = 1
    {condition_sql}
"""

COUPON_DEMONINATION_SUM = """
    SELECT
        outer_order_no,
        coupon_denomination_sum
    FROM cdm_crm.order_coupon_info_detail
    WHERE outer_order_no IN ({outer_order_no})
"""