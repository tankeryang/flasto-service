from flask_restplus import fields
from query_service.query_web.crm.controller.member_coupon_order_controller import ns_6


member_coupon_order_po = ns_6.model('MemberCouponOrderModel', {
    'coupon_category': fields.String(readonly=True, description="券批次类型"),
    'coupon_type_detail': fields.String(readOnly=True, description="券/券批次类型描述"),
    'coupon_name': fields.String(readonly=True, description="活动名称"),
    'coupon_template_no': fields.String(readOnly=True, description="券批次号"),
    'coupon_no': fields.String(readOnly=True, description="券号"),
    'coupon_denomination': fields.Float(readOnly=True, description="券面额/折扣"),
    'coupon_status': fields.String(readOnly=True, description="券状态"),
    'coupon_start_time': fields.String(readOnly=True, description="券生效日期"),
    'coupon_end_time': fields.String(readOnly=True, description="券失效日期"),
    'coupon_batch_time': fields.String(readOnly=True, description="券绑定日期"),
    'coupon_used_time': fields.String(readOnly=True, description="券使用日期"),
    'member_manage_store_code': fields.String(readOnly=True, description="会员管理门店编号"),
    'member_manage_store_name': fields.String(readOnly=True, description="会员管理门店名称"),
    'member_no': fields.String(readOnly=True, description="会员编号"),
    'member_wechat_id': fields.String(readonly=True, description="OpenID"),
    'member_name': fields.String(readOnly=True, description="会员姓名"),
    'member_mobile': fields.String(readOnly=True, description="会员手机"),
    'order_grade_id': fields.String(readonly=True, description="消费当前会员等级"),
    'order_trade_source': fields.String(readonly=True, description="消费渠道"),
    'order_store_code': fields.String(readOnly=True, description="订单消费门店编号"),
    'order_store_name': fields.String(readOnly=True, description="订单消费门店名称"),
    'coupon_used_order_no': fields.String(readOnly=True, description="券使用订单号"),
    'order_fact_amount': fields.Float(readOnly=True, description="销售金额(未扣券)"),
    'order_fact_amount_include_coupon': fields.Float(readOnly=True, description="销售金额(扣券)"),
    'order_retail_amount': fields.Float(readOnly=True, description="吊牌金额"),
    'order_item_quantity': fields.Float(readOnly=True, description="订单包含商品件数"),
    'order_discount': fields.Float(readOnly=True, description="订单折扣"),
    'coupon_passcode': fields.String(readonly=True, description="券密码")
})

member_coupon_order_list_po = ns_6.model('MemberCouponOrderListModel', {
    'data': fields.List(fields.Nested(member_coupon_order_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


coupon_denomination_sum_po = ns_6.model('CouponDenominationSumModel', {
    'outer_order_no': fields.String(readonly=True, description="订单号"),
    'coupon_denomination_sum': fields.Float(readonly=True, description="订单使用现金券总面额")
})

coupon_denomination_sum_list_po = ns_6.model('CouponDenominationSumListModel', {
    'data': fields.List(fields.Nested(coupon_denomination_sum_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})