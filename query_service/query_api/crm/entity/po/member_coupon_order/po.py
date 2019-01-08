from flask_restplus import fields
from query_service.query_web.crm.controller.member_coupon_order_controller import ns_6


member_coupon_order_po = ns_6.model('MemberCouponOrderModel', {
    'member_no': fields.String(readOnly=True, description="会员编号"),
    'member_name': fields.String(readOnly=True, description="会员姓名"),
    'member_mobile': fields.String(readOnly=True, description="会员手机"),
    'member_manage_store_code': fields.String(readOnly=True, description="会员管理门店编号"),
    'member_manage_store_name': fields.String(readOnly=True, description="会员管理门店名称"),
    'coupon_no': fields.String(readOnly=True, description="券号"),
    'coupon_status': fields.String(readOnly=True, description="券状态"),
    'coupon_batch_time': fields.String(readOnly=True, description="券绑定时间"),
    'coupon_start_time': fields.String(readOnly=True, description="券开始时间"),
    'coupon_end_time': fields.String(readOnly=True, description="券截止时间"),
    'coupon_template_no': fields.String(readOnly=True, description="券批次号"),
    'coupon_template_name': fields.String(readOnly=True, description="券批次名称"),
    'coupon_type': fields.String(readOnly=True, description="券类型"),
    'coupon_type_detail': fields.String(readOnly=True, description="券类型描述"),
    'coupon_denomination': fields.Float(readOnly=True, description="券面额"),
    'coupon_used_time': fields.String(readOnly=True, description="券使用时间"),
    'coupon_used_order_no': fields.String(readOnly=True, description="券使用订单号"),
    'order_store_code': fields.String(readOnly=True, description="订单消费门店编号"),
    'order_store_name': fields.String(readOnly=True, description="订单消费门店名称"),
    'order_retail_amount': fields.Float(readOnly=True, description="订单吊牌价"),
    'order_fact_amount': fields.Float(readOnly=True, description="订单实际金额"),
    'order_fact_amount_include_coupon': fields.Float(readOnly=True, description="订单实际扣券后金额"),
    'order_discount': fields.Float(readOnly=True, description="订单折扣"),
    'order_item_quantity': fields.Integer(readOnly=True, description="订单包含商品件数")
})

member_coupon_order_list_po = ns_6.model('MemberCouponOrderListModel', {
    'data': fields.List(fields.Nested(member_coupon_order_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})