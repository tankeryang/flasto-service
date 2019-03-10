from flask import current_app
from flask_restplus import Namespace, Resource

ns = Namespace('CRM 招募会员', path='/crm/recruit', description='招募会员api')

from .models import qo, ro
from .service import RecruitAnalyseService
from .utils.validator import RecruitAnalyseStoreQOValidator, RecruitAnalyseZoneQOValidator

from query_service.apis.utils.decorator import authorized
from query_service.apis.utils.exception import ControllerError


def controller(field, payload, service_method):
    """
    封装 service 逻辑
    :param field: 查询范围, zone or store
    :param payload: 请求参数
    :param service_method: service 层方法
    :return:
    """
    if field == 'zone':
        res, err = RecruitAnalyseZoneQOValidator().load(payload)
    elif field == 'store':
        res, err = RecruitAnalyseStoreQOValidator().load(payload)
    else:
        raise ControllerError("internal call error!")

    if err:
        current_app.logger.error("Err: " + str(err))
        return dict(success=False, message=err)
    else:
        current_app.logger.info("Param: " + str(res))
        return service_method(res)


@ns.route('/RecruitAmountReport')
class RecruitAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitAmountReport')
class StoreRecruitAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitAmountDailyDetail')
class RecruitAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询每日招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitAmountDailyDetail')
class StoreRecruitAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店每日招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitAmountMonthlyDetail')
class RecruitAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询每月招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitAmountMonthlyDetail')
class StoreRecruitAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店每月招募会员详情
        招募会员，有消费会员，未消费会员
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitConsumedAmountDailyDetail')
class RecruitConsumedAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_consumed_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询有消费会员每日详情
        普通会员，VIP会员，升级会员
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_consumed_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitConsumedAmountMonthlyDetail')
class RecruitConsumedAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_consumed_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询有消费会员每月详情
        普通会员，VIP会员，升级会员
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_consumed_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitConsumedAmountDailyDetail')
class StoreRecruitConsumedAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_consumed_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店有消费会员每日详情
        普通会员，VIP会员，升级会员
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_consumed_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitConsumedAmountMonthlyDetail')
class StoreRecruitConsumedAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_consumed_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店有消费会员每月详情
        普通会员，VIP会员，升级会员
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_consumed_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitUnconsumedAmountDailyDetail')
class RecruitUnconsumedAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_unconsumed_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询未消费会员每日详情
        官网注册，门店注册
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_unconsumed_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/RecruitUnconsumedAmountMonthlyDetail')
class RecruitUnconsumedAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_zone_qo)
    @ns.marshal_with(ro.recruit_unconsumed_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询未消费会员每月详情
        官网注册，门店注册
        """
        try:
            return controller('zone', ns.payload, RecruitAnalyseService.get_recruit_unconsumed_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitUnconsumedAmountDailyDetail')
class StoreRecruitUnconsumedAmountDailyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_unconsumed_amount_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店未消费会员每日详情
        官网注册，门店注册
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_unconsumed_amount_daily_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreRecruitUnconsumedAmountMonthlyDetail')
class StoreRecruitUnconsumedAmountMonthlyDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.recruit_analyse_store_qo)
    @ns.marshal_with(ro.recruit_unconsumed_amount_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店未消费会员每月详情
        官网注册，门店注册
        """
        try:
            return controller('store', ns.payload, RecruitAnalyseService.get_store_recruit_unconsumed_amount_monthly_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)
