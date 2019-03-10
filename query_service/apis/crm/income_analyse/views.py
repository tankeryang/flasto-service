from flask import current_app
from flask_restplus import Resource, Namespace

ns = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')

from .models import qo, ro
from .service import IncomeAnalyseService
from .utils.validator import IncomeAnalyseStoreQOValidator, IncomeAnalyseZoneQOValidator

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
        res, err = IncomeAnalyseZoneQOValidator().load(payload)
    elif field == 'store':
        res, err = IncomeAnalyseStoreQOValidator().load(payload)
    else:
        raise ControllerError("internal call error!")

    if err:
        current_app.logger.error("Err: " + str(err))
        return dict(success=False, message=err)
    else:
        current_app.logger.info("Param: " + str(res))
        return service_method(res)


@ns.route('/TotalIncomeReport')
class TotalIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.total_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_total_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreTotalIncomeReport')
class StoreTotalIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.total_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店整体收入分析
        整体，会员，非会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_total_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/TotalDailyIncomeDetail')
class TotalDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.total_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询整体收入每日趋势
        整体销售收入，同比，日期
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_total_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreTotalDailyIncomeDetail')
class StoreTotalDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.total_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店整体收入每日趋势
        整体销售收入，同比，日期
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_total_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/TotalMonthlyIncomeDetail')
class TotalMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.total_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询整体收入每月趋势
        整体销售收入，同比，月份
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_total_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreTotalMonthlyIncomeDetail')
class StoreTotalMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.total_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店整体收入每月趋势
        整体销售收入，同比，月份
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_total_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberNewOldIncomeReport')
class MemberNewOldIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.new_old_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_new_old_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberNewOldIncomeReport')
class StoreMemberNewOldIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.new_old_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店新老会员收入分析
        会员，新会员，老会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_new_old_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberNewOldDailyIncomeDetail')
class MemberNewOldDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.new_old_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_new_old_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberNewOldDailyIncomeDetail')
class StoreMemberNewOldDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.new_old_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_new_old_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberNewOldMonthlyIncomeDetail')
class MemberNewOldMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.new_old_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询新老会员每月收入趋势
        会员，新会员，老会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_new_old_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberNewOldMonthlyIncomeDetail')
class StoreMemberNewOldMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.new_old_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店新老会员每月收入趋势
        会员，新会员，老会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_new_old_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberLevelIncomeReport')
class MemberLevelIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.level_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_level_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberLevelIncomeReport')
class StoreMemberLevelIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.level_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店会员等级收入分析
        会员，普通会员，VIP会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_level_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberLevelDailyIncomeDetail')
class MemberLevelDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.level_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_level_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.level_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_level_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberLevelMonthlyIncomeDetail')
class MemberLevelMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.level_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_level_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberLevelMonthlyIncomeDetail')
class StoreMemberLevelMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.level_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_level_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberMulDimIncomeReport')
class MemberMulDimIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.mul_dim_all_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_mul_dim_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberMulDimIncomeReport')
class StoreMemberMulDimIncomeReportView(Resource):
    
    @ns.doc(security='key')
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.mul_dim_all_list_ro)
    def post(self):
        """
        查询门店多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_mul_dim_income_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberMulDimDailyIncomeDetail')
class MemberMulDimDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.mul_dim_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_mul_dim_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberMulDimDailyIncomeDetail')
class StoreMemberMulDimDailyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.mul_dim_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_mul_dim_daily_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberMulDimMonthlyIncomeDetail')
class MemberMulDimMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.mul_dim_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_mul_dim_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberMulDimMonthlyIncomeDetail')
class StoreMemberMulDimMonthlyIncomeDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.mul_dim_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_mul_dim_monthly_income_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberRegisterProportionReport')
class MemberRegisterProportionReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.rgp_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_register_proportion_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberRegisterProportionReport')
class StoreMemberRegisterProportionReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.rgp_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_register_proportion_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberDailyRegisterProportionDetail')
class MemberDailyRegisterProportionDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.rgp_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_daily_register_proportion_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberDailyRegisterProportionDetail')
class StoreMemberDailyRegisterProportionDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.rgp_daily_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_daily_register_proportion_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberMonthlyRegisterProportionDetail')
class MemberMonthlyRegisterProportionDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_zone_qo)
    @ns.marshal_with(ro.rgp_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('zone', ns.payload, IncomeAnalyseService.get_member_monthly_register_proportion_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberMonthlyRegisterProportionDetail')
class StoreMemberMonthlyRegisterProportionDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.income_analyse_store_qo)
    @ns.marshal_with(ro.rgp_monthly_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        try:
            return controller('store', ns.payload, IncomeAnalyseService.get_store_member_monthly_register_proportion_detail_data)
        except ControllerError as e:
            current_app.logger.exception(e)
