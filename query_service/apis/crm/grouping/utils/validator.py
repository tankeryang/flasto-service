from marshmallow import Schema, fields
from query_service.apis.utils.fields import EnumString, NotEmptyList, StringDate, MinMaxInteger


# 会员基础信息 ==========================================================================================================
class MemberBirthday(Schema):
    lt = fields.String(description="早于")
    gt = fields.String(description="晚于")
    eq = fields.String(description="等于")
    bt = NotEmptyList(fields.String(description="介于"), length=2)


class MemberAge(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class MemberRegisterDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class MemberInfoModel(Schema):
    member_birthday = fields.Nested(MemberBirthday, description="会员生日")
    member_birthday_month = fields.List(fields.String(description="会员生日月份"))
    member_gender = fields.List(EnumString(description="会员性别", enum=['男', '女', '其他']))
    member_age = fields.Nested(MemberAge, description="会员年龄")
    member_status = fields.List(EnumString(description="会员状态", enum=['正常', '作废', '异常卡']))
    member_register_date = fields.Nested(MemberRegisterDate, description="会员注册日期")
    member_manage_store = fields.List(fields.String(description="会员管理门店"))
    member_register_store = fields.List(fields.String(description="会员注册门店"))
    member_reg_source = fields.List(fields.String(description="注册渠道"))
    member_is_batch_mobile = MinMaxInteger(description="是否绑定手机(1:是/0:否)", min=0, max=1)
    member_is_batch_wechat = MinMaxInteger(description="是否绑定微信(1:是/0:否)", min=0, max=1)
    member_is_batch_taobao = MinMaxInteger(description="是否绑定淘宝(1:是/0:否)", min=0, max=1)


# 等级信息 ==============================================================================================================
class MemberGradeExpirationDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class GradeInfoModel(Schema):
    member_grade_id = fields.List(fields.Integer(description="会员等级id"))
    member_grade_expiration_date = fields.Nested(MemberGradeExpirationDate, description="会员等级到期日期")


# 积分信息 ==============================================================================================================
class MemberScore(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class MemberWillScore(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class ScoreInfoModel(Schema):
    member_score = fields.Nested(MemberScore, description="会员积分")
    member_will_score = fields.Nested(MemberWillScore, description="会员未到账积分")


# 最近消费 ==============================================================================================================
class LstConsumptionDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class LstConsumptionGap(Schema):
    lt = fields.Integer(description="小于")
    gt = fields.Integer(description="大于")
    eq = fields.Integer(description="等于")
    bt = NotEmptyList(fields.Integer(description="介于"), length=2)


class LstConsumptionItemQuantity(Schema):
    lt = fields.Integer(description="小于")
    gt = fields.Integer(description="大于")
    eq = fields.Integer(description="等于")
    bt = NotEmptyList(fields.Integer(description="介于"), length=2)


class LstConsumptionAmount(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class LstConsumptionAmountIncludeCoupon(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class LstConsumptionModel(Schema):
    lst_consumption_date = fields.Nested(LstConsumptionDate, description="最近消费日期")
    lst_consumption_gap = fields.Nested(LstConsumptionGap, description="最近消费间隙")
    lst_consumption_store = fields.List(fields.String(description="最近消费门店"))
    lst_consumption_item_quantity = fields.Nested(LstConsumptionItemQuantity, description="最近消费件数")
    lst_consumption_amount = fields.Nested(LstConsumptionAmount, description="最近消费金额")
    lst_consumption_amount_include_coupon = fields.Nested(LstConsumptionAmountIncludeCoupon, description="最近消费金额(含券)")


# 首次消费 ==============================================================================================================
class FstConsumptionDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class FstConsumptionGap(Schema):
    lt = fields.Integer(description="小于")
    gt = fields.Integer(description="大于")
    eq = fields.Integer(description="等于")
    bt = NotEmptyList(fields.Integer(description="介于"), length=2)


class FstConsumptionItemQuantity(Schema):
    lt = fields.Integer(description="小于")
    gt = fields.Integer(description="大于")
    eq = fields.Integer(description="等于")
    bt = NotEmptyList(fields.Integer(description="介于"), length=2)


class FstConsumptionAmount(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class FstConsumptionAmountIncludeCoupon(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class FstConsumptionModel(Schema):
    fst_consumption_date = fields.Nested(FstConsumptionDate, description="首次消费日期")
    fst_consumption_gap = fields.Nested(FstConsumptionGap, description="首次消费间隙")
    fst_consumption_store = fields.List(fields.String(description="首次消费门店"))
    fst_consumption_item_quantity = fields.Nested(FstConsumptionItemQuantity, description="首次消费件数")
    fst_consumption_amount = fields.Nested(FstConsumptionAmount, description="首次消费金额")
    fst_consumption_amount_include_coupon = fields.Nested(FstConsumptionAmountIncludeCoupon, description="首次消费金额(含券)")


# 券权益 ================================================================================================================
class CouponAmount(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CouponDiscount(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CouponDenomination(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CouponBatchDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class CouponStartDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class CouponEndDate(Schema):
    lt = StringDate(description="早于")
    gt = StringDate(description="晚于")
    eq = StringDate(description="等于")
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class CouponInfoModel(Schema):
    coupon_amount = fields.Nested(CouponAmount, description="券数量")
    coupon_template_no = fields.List(fields.String(description="券批次号"), example=['czkzcd000909'])
    coupon_status = fields.List(fields.String(description="券状态"), example=['7', '-2', '0'])
    coupon_category = fields.List(fields.String(description="券类别(现金券/折扣券)"), example=['Cash'])
    coupon_discount = fields.Nested(CouponDiscount, description="券折扣")
    coupon_denomination = fields.Nested(CouponDenomination, description="券面额")
    coupon_type_detail = fields.List(fields.String(description="券类型描述"), example=['Other'])
    coupon_batch_date = fields.Nested(CouponBatchDate, description="券绑定日期")
    coupon_start_date = fields.Nested(CouponStartDate, description="券开始日期")
    coupon_end_date = fields.Nested(CouponEndDate, description="券截止日期")


# 累计消费 ==============================================================================================================
class CmlConsumptionDate(Schema):
    bt = NotEmptyList(StringDate(description="介于"), length=2)


class CmlConsumptionTimes(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlConsumptionItemQuantity(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlConsumptionDays(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlConsumptionMonths(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlConsumptionAmount(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlConsumptionAmountIncludeCoupon(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlReturnTimes(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlReturnAmount(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlAvgDiscount(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlAvgDiscountIncludeCoupon(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlAvgSalesAmountPerOrder(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlAvgSalesItemPerOrder(Schema):
    lt = MinMaxInteger(description="小于", min=0)
    gt = MinMaxInteger(description="大于", min=0)
    eq = MinMaxInteger(description="等于", min=0)
    bt = NotEmptyList(MinMaxInteger(description="介于", min=0), length=2)


class CmlAvgSalesAmountPerItem(Schema):
    lt = fields.Float(description="小于")
    gt = fields.Float(description="大于")
    eq = fields.Float(description="等于")
    bt = NotEmptyList(fields.Float(description="介于"), length=2)


class CmlConsumptionModel(Schema):
    cml_consumption_date = fields.Nested(CmlConsumptionDate, description="累计消费计算日期", required=True)
    cml_consumption_store = fields.List(fields.String(description="累计消费门店"), example=['1101', '1102'])
    cml_consumption_times = fields.Nested(CmlConsumptionTimes, description="累计消费次数")
    cml_consumption_item_quantity = fields.Nested(CmlConsumptionItemQuantity, description="累计消费件数")
    cml_consumption_days = fields.Nested(CmlConsumptionDays, description="累计消费天数")
    cml_consumption_months = fields.Nested(CmlConsumptionMonths, description="累计消费月数")
    cml_consumption_amount = fields.Nested(CmlConsumptionAmount, description="累计消费金额")
    cml_consumption_amount_include_coupon = fields.Nested(CmlConsumptionAmountIncludeCoupon, description="累计消费金额(含券)")
    cml_return_times = fields.Nested(CmlReturnTimes, description="累计退款次数")
    cml_return_amount = fields.Nested(CmlReturnAmount, description="累计退款金额")
    cml_avg_discount = fields.Nested(CmlAvgDiscount, description="累计平均折扣")
    cml_avg_discount_include_coupon = fields.Nested(CmlAvgDiscountIncludeCoupon, description="累计平均折扣(含券)")
    cml_avg_sales_amount_per_order = fields.Nested(CmlAvgSalesAmountPerOrder, description="累计平均客单价")
    cml_avg_sales_item_per_order = fields.Nested(CmlAvgSalesItemPerOrder, description="累计平均客单件")
    cml_avg_sales_amount_per_item = fields.Nested(CmlAvgSalesAmountPerItem, description="累计平均件单价")


# 汇总 ==================================================================================================================
class MemberGroupingDetailQOValidator(Schema):
    brand_code = fields.String(description="品牌编号", required=True)
    member_info_model = fields.Nested(MemberInfoModel, description="会员基础信息相关参数")
    grade_info_model = fields.Nested(GradeInfoModel, description="等级信息相关参数")
    score_info_model = fields.Nested(ScoreInfoModel, description="积分相关信息参数")
    lst_consumption_model = fields.Nested(LstConsumptionModel, description="最近消费相关参数")
    fst_consumption_model = fields.Nested(FstConsumptionModel, description="首次消费相关参数")
    coupon_info_model = fields.Nested(CouponInfoModel, description="券相关参数")
    cml_consumption_model = fields.Nested(CmlConsumptionModel, description="累计消费相关参数")
    page = MinMaxInteger(description="页码", min=1, required=True)


class MemberGroupingCountQOValidator(Schema):
    brand_code = fields.String(description="品牌编号", required=True)
    member_info_model = fields.Nested(MemberInfoModel, description="会员基础信息相关参数")
    grade_info_model = fields.Nested(GradeInfoModel, description="等级信息相关参数")
    score_info_model = fields.Nested(ScoreInfoModel, description="积分相关信息参数")
    lst_consumption_model = fields.Nested(LstConsumptionModel, description="最近消费相关参数")
    fst_consumption_model = fields.Nested(FstConsumptionModel, description="首次消费相关参数")
    coupon_info_model = fields.Nested(CouponInfoModel, description="券相关参数")
    cml_consumption_model = fields.Nested(CmlConsumptionModel, description="累计消费相关参数")
