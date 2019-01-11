from flask_restplus import Resource, Namespace

ns_6 = Namespace('CRM 会员-券-订单关联查询', path='/crm/member_coupon_order', description="会员-券-订单关联查询api")

from query_service.query_biz.crm.service.impl.member_coupon_order_service_impl import MemberCouponOrderServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.member_coupon_order as dto
import query_service.query_api.crm.entity.po.member_coupon_order as po


@ns_6.route('/MemberCouponOrder')
class MemberCouponOrderController(Resource):
    
    @ns_6.doc(security='key')
    @ns_6.response(401, "Token authorized error")
    @authorized
    @ns_6.expect(dto.member_coupon_order_dto, validate=True)
    @ns_6.marshal_with(po.member_coupon_order_list_po)
    def post(self):
        """
        查询会员-券-订单关联数据
        """
        return MemberCouponOrderServiceImpl().get_member_coupon_order_data(ns_6.payload)