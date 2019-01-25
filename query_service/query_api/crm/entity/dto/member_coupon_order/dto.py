from flask_restplus import fields
from query_service.query_web.crm.controller.member_coupon_order_controller import ns_6


member_coupon_order_dto = ns_6.model('MemberCouponOrderReqDtoModel', {
    'brand_code': fields.List(fields.String(description="品牌编号")),
    'member_no': fields.List(fields.String(description="会员编号")),
    'member_name': fields.List(fields.String(description="会员姓名")),
    'member_mobile': fields.List(fields.String(description="会员手机")),
    'member_manage_store_code': fields.List(fields.String(description="会员管理门店编号"), example=['1101', '1102']),
    'coupon_no': fields.List(fields.String(description="券号")),
    'coupon_name': fields.List(fields.String(description="券名称")),
    'coupon_template_no': fields.List(fields.String(description="券批次号")),
    'coupon_category': fields.List(fields.String(description="券类别")),
    'coupon_type_detail': fields.List(fields.String(description="券类型描述")),
    'coupon_status': fields.List(fields.String(description="券状态")),
    'coupon_start_date': fields.List(fields.Date(description="券开始日期"), example=['2018-12-01'])
})


coupon_denomination_sum_dto = ns_6.model('OrderIncludeCouponDtoModel', {
    'outer_order_no': fields.List(fields.String(description="订单号"), required=True)
})
