from marshmallow import Schema, fields
from query_service.apis.utils.fields import StringDate


class MemberCouponOrderQOValidator(Schema):
    brand_code = fields.List(fields.String(description="品牌编号"))
    coupon_no = fields.List(fields.String(description="券号"))
    coupon_name = fields.List(fields.String(description="券活动名称"))
    coupon_category = fields.List(fields.String(description="券类型"))
    coupon_status = fields.List(fields.String(description="券状态"))
    coupon_template_no = fields.List(fields.String(description="券批次号"))
    coupon_batch_date = fields.List(StringDate(description="券绑定日期 [from_date, to_date]"))
    coupon_start_date = fields.List(StringDate(description="券生效日期 [from_date, to_date]"))
    coupon_end_date = fields.List(StringDate(description="券截止日期 [from_date, to_date]"))
    coupon_used_date = fields.List(StringDate(description="券使用日期 [from_date, to_date]"))
    member_name = fields.List(fields.String(description="会员姓名"))
    member_no_or_mobile = fields.List(fields.String(description="会员编号或手机号"))
    member_manage_store_code = fields.List(fields.String(description="会员管理门店编号"))
    order_store_code = fields.List(fields.String(description="会员消费门店编号"))


class CouponDenominationSumQOValidator(Schema):
    outer_order_no = fields.List(fields.String(description="订单号"), required=True)
