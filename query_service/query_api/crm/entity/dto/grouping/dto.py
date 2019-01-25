from flask_restplus import fields
from query_service.query_web.crm.controller.member_grouping_controller import ns_5


# 会员基础信息 ==========================================================================================================
member_birthday = ns_5.model('BirthdayConditionModel', {
    'lt': fields.String(description="早于", example='11-30'),
    'gt': fields.String(description="晚于", example='11-30'),
    'eq': fields.String(description="等于", example='11-30'),
    'bt': fields.List(fields.String(description="介于"), example=['09-01', '11-30']),
})

member_age = ns_5.model('AgeConditionModel', {
    'lt': fields.Integer(description="大于", example=26, min=0),
    'gt': fields.Integer(description="小于", example=26, min=0),
    'eq': fields.Integer(description="等于", example=26, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[10, 26])
})

member_register_date = ns_5.model('RegisterDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="晚于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

member_grade_expiration_date = ns_5.model('GradeExpirationDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="晚于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

member_score = ns_5.model('ScoreConditionModel', {
    'lt': fields.Float(description="大于", example=1000.00),
    'gt': fields.Float(description="小于", example=1000.00),
    'eq': fields.Float(description="等于", example=1000.00),
    'bt': fields.List(fields.Float(description="介于"), example=[0.00, 1000.00])
})

member_will_score = ns_5.model('WillScoreConditionModel', {
    'lt': fields.Float(description="大于", example=1000.00),
    'gt': fields.Float(description="小于", example=1000.00),
    'eq': fields.Float(description="等于", example=1000.00),
    'bt': fields.List(fields.Float(description="介于"), example=[0.00, 1000.00])
})

lst_consumption_date = ns_5.model('LastConsumptionDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="晚于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

lst_consumption_gap = ns_5.model('LastConsumptionGapConditionModel', {
    'lt': fields.Integer(description="小于", example=50, min=0),
    'gt': fields.Integer(description="大于", example=50, min=0),
    'eq': fields.Integer(description="等于", example=50, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 50]),
})

lst_consumption_item_quantity = ns_5.model('LastConsumptionItemQuantityConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

lst_consumption_amount = ns_5.model('LastConsumptionAmountConditionModel', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

lst_consumption_amount_include_coupon = ns_5.model('LastConsumptionAmountIncludeCouponConditionModel', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

fst_consumption_date = ns_5.model('LastConsumptionDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="晚于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

fst_consumption_gap = ns_5.model('LastConsumptionGapConditionModel', {
    'lt': fields.Integer(description="小于", example=50, min=0),
    'gt': fields.Integer(description="大于", example=50, min=0),
    'eq': fields.Integer(description="等于", example=50, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 50]),
})

fst_consumption_item_quantity = ns_5.model('LastConsumptionItemQuantityConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

fst_consumption_amount = ns_5.model('LastConsumptionAmountConditionModel', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

fst_consumption_amount_include_coupon = ns_5.model('LastConsumptionAmountIncludeCouponConditionModel', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

member_info_model = ns_5.model('MemberInfoModel', {
    'member_birthday': fields.Nested(member_birthday, description="会员生日"),
    'member_birthday_month': fields.String(description="会员生日月份", exmple='08'),
    'member_gender': fields.String(description="会员性别", example='男'),
    'member_age': fields.Nested(member_age, description="会员年龄"),
    'member_status': fields.String(description="会员状态", example='正常', enum=['正常', '作废', '异常卡']),
    'member_register_date': fields.Nested(member_register_date, description="会员注册日期"),
    'member_manage_store': fields.List(fields.String(description="会员管理门店"), example=['1101', '1102']),
    'member_register_store': fields.List(fields.String(description="会员管理门店"), example=['1101', '1102']),
    'member_reg_source': fields.List(fields.String(description="注册渠道"), example=['weixin']),
    'member_is_batch_mobile': fields.Integer(description="是否绑定手机(1:是/0:否)", example=1, min=0, max=1),
    'member_is_batch_wechat': fields.Integer(description="是否绑定微信(1:是/0:否)", example=1, min=0, max=1),
    'member_is_batch_taobao': fields.Integer(description="是否绑定淘宝(1:是/0:否)", example=1, min=0, max=1),
    'member_grade_id': fields.List(fields.Integer(description="会员等级id"), example=[13, 14]),
    'member_grade_expiration_date': fields.Nested(member_grade_expiration_date, description="会员等级到期日期"),
    'member_score': fields.Nested(member_score, description="会员积分"),
    'member_will_score': fields.Nested(member_will_score, description="会员未到账积分"),
    'lst_consumption_date': fields.Nested(lst_consumption_date, description="最近消费日期"),
    'lst_consumption_gap': fields.Nested(lst_consumption_gap, description="最近消费间隙"),
    'lst_consumption_store': fields.List(fields.String(description="最近消费门店"), example=['1101', '1102']),
    'lst_consumption_item_quantity': fields.Nested(lst_consumption_item_quantity, description="最近消费件数"),
    'lst_consumption_amount': fields.Nested(lst_consumption_amount, description="最近消费金额"),
    'lst_consumption_amount_include_coupon': fields.Nested(lst_consumption_amount_include_coupon, description="最近消费金额(含券)"),
    'fst_consumption_date': fields.Nested(fst_consumption_date, description="首次消费日期"),
    'fst_consumption_gap': fields.Nested(fst_consumption_gap, description="首次消费间隙"),
    'fst_consumption_store': fields.List(fields.String(description="首次消费门店"), example=['1101', '1102']),
    'fst_consumption_item_quantity': fields.Nested(fst_consumption_item_quantity, description="首次消费件数"),
    'fst_consumption_amount': fields.Nested(fst_consumption_amount, description="首次消费金额"),
    'fst_consumption_amount_include_coupon': fields.Nested(fst_consumption_amount_include_coupon, description="首次消费金额(含券)")
})

# 券权益 ================================================================================================================
coupon_amount = ns_5.model('CouponAmountConditionModel', {
    'lt': fields.Integer(description="小于", example=10, min=0),
    'gt': fields.Integer(description="大于", example=10, min=0),
    'eq': fields.Integer(description="等于", example=10, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 10]),
})

coupon_discount = ns_5.model('CouponDiscountConditionModel', {
    'lt': fields.Float(description="小于", example=1.0),
    'gt': fields.Float(description="大于", example=1.0),
    'eq': fields.Float(description="等于", example=1.0),
    'bt': fields.List(fields.Float(description="介于"), example=[0.0, 1.0])
})

coupon_denomination = ns_5.model('CouponDenominationConditionModel', {
    'lt': fields.Float(description="小于", example=200.0),
    'gt': fields.Float(description="大于", example=0.0),
    'eq': fields.Float(description="等于", example=200.0),
    'bt': fields.List(fields.Float(description="介于"), example=[0.0, 200.0])
})

coupon_batch_date = ns_5.model('CouponBatchDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="等于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

coupon_start_date = ns_5.model('CouponStartDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="等于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

coupon_end_date = ns_5.model('CouponEndDateConditionModel', {
    'lt': fields.Date(description="早于", example='2018-10-11'),
    'gt': fields.Date(description="晚于", example='2018-10-11'),
    'eq': fields.Date(description="等于", example='2018-10-11'),
    'bt': fields.List(fields.Date(description="介于"), example=['2018-09-01', '2018-10-11'])
})

coupon_info_model = ns_5.model('CouponInfoModel', {
    'coupon_amount': fields.Nested(coupon_amount, description="券数量"),
    'coupon_template_no': fields.String(description="券批次号", example='czkzcd000909'),
    'coupon_status': fields.List(fields.String(description="券状态"), example=['7', '-2', '0']),
    'coupon_category': fields.String(description="券类别(现金券/折扣券)", example='Cash'),
    'coupon_discount': fields.Nested(coupon_discount, description="券折扣"),
    'coupon_denomination': fields.Nested(coupon_denomination, description="券面额"),
    'coupon_type_detail': fields.String(description="券类型描述", example='Other'),
    'coupon_batch_date': fields.Nested(coupon_batch_date, description="券绑定日期"),
    'coupon_start_date': fields.Nested(coupon_start_date, description="券开始日期"),
    'coupon_end_date': fields.Nested(coupon_end_date, description="券截止日期")
})

# 累计消费 ==============================================================================================================
cml_consumption_times = ns_5.model('CumulativeConsumptionTimesConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_consumption_item_quantity = ns_5.model('CumulativeConsumptionItemQuantityConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_consumption_days = ns_5.model('CumulativeConsumptionDaysConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_consumption_months = ns_5.model('CumulativeConsumptionMonthsConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_consumption_amount = ns_5.model('CumulativeConsumptionAmountConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_consumption_amount_include_coupon = ns_5.model('CumulativeConsumptionAmountIncludeCoupon', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

cml_return_times = ns_5.model('CumulativeReturnTimesConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_return_amount = ns_5.model('CumulativeReturnAmountConditionModel', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

cml_avg_discount = ns_5.model('CumulativeAverageDiscountConditionModel', {
    'lt': fields.Float(description="小于", example=0.8, min=0),
    'gt': fields.Float(description="大于", example=0.8, min=0),
    'eq': fields.Float(description="等于", example=0.8, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 0.9]),
})

cml_avg_discount_include_coupon = ns_5.model('CumulativeAverageDiscountIncludeCouponConditionModel', {
    'lt': fields.Float(description="小于", example=0.8, min=0),
    'gt': fields.Float(description="大于", example=0.8, min=0),
    'eq': fields.Float(description="等于", example=0.8, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 0.9]),
})

cml_avg_sales_amount_per_order = ns_5.model('CumulativeAverageSalesAmountPerOrderConditionOrder', {
    'lt': fields.Float(description="小于", example=1000.0, min=0),
    'gt': fields.Float(description="大于", example=1000.0, min=0),
    'eq': fields.Float(description="等于", example=1000.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

cml_avg_sales_item_per_order = ns_5.model('CumulativeAverageSalesItemPerOrderConditionModel', {
    'lt': fields.Integer(description="小于", example=2, min=0),
    'gt': fields.Integer(description="大于", example=2, min=0),
    'eq': fields.Integer(description="等于", example=2, min=0),
    'bt': fields.List(fields.Integer(description="介于", min=0), example=[0, 5]),
})

cml_avg_sales_amount_per_item = ns_5.model('CumulativeAverageSalesAmountPerItemConditionModel', {
    'lt': fields.Float(description="小于", example=800.0, min=0),
    'gt': fields.Float(description="大于", example=800.0, min=0),
    'eq': fields.Float(description="等于", example=800.0, min=0),
    'bt': fields.List(fields.Float(description="介于", min=0), example=[0, 1000.0]),
})

cml_consumption_model = ns_5.model('CumulativeConsumptionModel', {
    'cml_consumption_date': fields.List(fields.Date(description="累计消费日期"), example=['2018-11-01', '2018-11-30'], required=True),
    'cml_consumption_store': fields.List(fields.String(description="累计消费门店"), example=['1101', '1102']),
    'cml_consumption_times': fields.Nested(cml_consumption_times, description="累计消费次数"),
    'cml_consumption_item_quantity': fields.Nested(cml_consumption_item_quantity, description="累计消费件数"),
    'cml_consumption_days': fields.Nested(cml_consumption_days, description="累计消费天数"),
    'cml_consumption_months': fields.Nested(cml_consumption_months, description="累计消费月数"),
    'cml_consumption_amount': fields.Nested(cml_consumption_amount, description="累计消费金额"),
    'cml_consumption_amount_include_coupon': fields.Nested(cml_consumption_amount_include_coupon, description="累计消费金额(含券)"),
    'cml_return_times': fields.Nested(cml_return_times, description="累计退款次数"),
    'cml_return_amount': fields.Nested(cml_return_amount, description="累计退款金额"),
    'cml_avg_discount': fields.Nested(cml_avg_discount, description="累计平均折扣"),
    'cml_avg_discount_include_coupon': fields.Nested(cml_avg_discount_include_coupon, description="累计平均折扣(含券)"),
    'cml_avg_sales_amount_per_order': fields.Nested(cml_avg_sales_amount_per_order, description="累计平均客单价"),
    'cml_avg_sales_item_per_order': fields.Nested(cml_avg_sales_item_per_order, description="累计平均客单件"),
    'cml_avg_sales_amount_per_item': fields.Nested(cml_avg_sales_amount_per_item, description="累计平均件单价")
})

# 汇总 ==================================================================================================================
member_grouping_dto = ns_5.model('MemberGroupingReqDtoModel', {
    'brand_code': fields.String(description="品牌编号", required=True),
    'member_info_model': fields.Nested(member_info_model, description="会员基础信息相关参数"),
    'coupon_info_model': fields.Nested(coupon_info_model, description="券相关参数"),
    'cml_consumption_model': fields.Nested(cml_consumption_model, description="累计消费相关参数")
})
