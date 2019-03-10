from flask import current_app
from flask_restplus import Resource, Namespace

ns = Namespace('CRM 会员-券-订单关联查询', path='/crm/member_coupon_order', description="会员-券-订单关联查询api")

from .models import qo, ro
from .service import CouponService
from .utils.validator import MemberCouponOrderQOValidator, CouponDenominationSumQOValidator

from query_service.apis.utils.decorator import authorized


@ns.route('/MemberCouponOrder')
class MemberCouponOrderView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_coupon_order_qo)
    @ns.marshal_with(ro.member_coupon_order_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员-券-订单关联数据
        """
        res, err = MemberCouponOrderQOValidator().load(ns.payload)

        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return CouponService.get_member_coupon_order_data(res)


@ns.route('/MemberCouponOrder/csv')
class MemberCouponOrderCsvView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_coupon_order_qo)
    @ns.marshal_with(ro.member_coupon_order_export_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        导出会员-券-订单关联数据
        """
        res, err = MemberCouponOrderQOValidator().load(ns.payload)

        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return CouponService.export_member_coupon_order_data_csv(res)


@ns.route('/CouponDenominationSum')
class CouponDenominationSumView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.coupon_denomination_sum_qo)
    @ns.marshal_with(ro.coupon_denomination_sum_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询订单扣券金额
        """
        res, err = CouponDenominationSumQOValidator().load(ns.payload)

        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return CouponService.get_coupon_denomination_sum(res)
