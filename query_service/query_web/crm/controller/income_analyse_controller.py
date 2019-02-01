from flask import current_app
from flask_restplus import Resource, Namespace

ns_2 = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')

from query_service.query_biz.crm.service.impl.income_analyse_service_impl import IncomeAnalyseServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.income as dto
import query_service.query_api.crm.entity.po.income as po


@ns_2.route('/TotalIncomeReport')
class TotalIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_total_income_report_data(ns_2.payload)


@ns_2.route('/StoreTotalIncomeReport')
class StoreTotalIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询门店整体收入分析
        整体，会员，非会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_total_income_report_data(ns_2.payload)


@ns_2.route('/TotalDailyIncomeDetail')
class TotalDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询整体收入每日趋势
        整体销售收入，同比，日期
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalDailyIncomeDetail')
class StoreTotalDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询门店整体收入每日趋势
        整体销售收入，同比，日期
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/TotalMonthlyIncomeDetail')
class TotalMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询整体收入每月趋势
        整体销售收入，同比，月份
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_total_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalMonthlyIncomeDetail')
class StoreTotalMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询门店整体收入每月趋势
        整体销售收入，同比，月份
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_total_monthly_income_detail_data(ns_2.payload)


# @ns_2.route('/MemberNowBeforeIncomeReport')
# class MemberNowBeforeIncomeReportController(Resource):
#
#     @ns_2.doc(security='key')
#     @ns_2.response(401, "Token authorized error")
#     @authorized
#     @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
#     @ns_2.marshal_with(po.now_before_all_list_po)
#     def post(self):
#         """
#         查询会员收入分析
#         会员，当月会员，当年会员，往年会员
#         """
#         return IncomeAnalyseServiceImpl() \
#             .get_member_now_before_income_report_data(ns_2.payload)
#
#
# @ns_2.route('/StoreMemberNowBeforeIncomeReport')
# class StoreMemberNowBeforeIncomeReportController(Resource):
#
#     @ns_2.doc(security='key')
#     @ns_2.response(401, "Token authorized error")
#     @authorized
#     @ns_2.expect(dto.income_analyse_store_dto, validate=True)
#     @ns_2.marshal_with(po.now_before_all_list_po)
#     def post(self):
#         """
#         查询门店会员收入分析
#         会员，当月会员，当年会员，往年会员
#         """
#         return IncomeAnalyseServiceImpl() \
#             .get_store_member_now_before_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldIncomeReport')
class MemberNewOldIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldIncomeReport')
class StoreMemberNewOldIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询门店新老会员收入分析
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldDailyIncomeDetail')
class MemberNewOldDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldDailyIncomeDetail')
class StoreMemberNewOldDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberNewOldMonthlyIncomeDetail')
class MemberNewOldMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询新老会员每月收入趋势
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldMonthlyIncomeDetail')
class StoreMemberNewOldMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询门店新老会员每月收入趋势
        会员，新会员，老会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelIncomeReport')
class MemberLevelIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_level_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelIncomeReport')
class StoreMemberLevelIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询门店会员等级收入分析
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_level_income_report_data(ns_2.payload)


@ns_2.route('/MemberLevelDailyIncomeDetail')
class MemberLevelDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询门店会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelMonthlyIncomeDetail')
class MemberLevelMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelMonthlyIncomeDetail')
class StoreMemberLevelMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询门店会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimIncomeReport')
class MemberMulDimIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimIncomeReport')
class StoreMemberMulDimIncomeReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询门店多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/MemberMulDimDailyIncomeDetail')
class MemberMulDimDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimDailyIncomeDetail')
class StoreMemberMulDimDailyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询门店多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimMonthlyIncomeDetail')
class MemberMulDimMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimMonthlyIncomeDetail')
class StoreMemberMulDimMonthlyIncomeDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询门店多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberRegisterProportionReport')
class MemberRegisterProportionReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_list_po)
    def post(self):
        """
        查询登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_register_proportion_report_data(ns_2.payload)


@ns_2.route('/StoreMemberRegisterProportionReport')
class StoreMemberRegisterProportionReportController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_list_po)
    def post(self):
        """
        查询门店登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_register_proportion_report_data(ns_2.payload)


@ns_2.route('/MemberDailyRegisterProportionDetail')
class MemberDailyRegisterProportionDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_daily_list_po)
    def post(self):
        """
        查询每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_daily_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberDailyRegisterProportionDetail')
class StoreMemberDailyRegisterProportionDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_daily_list_po)
    def post(self):
        """
        查询门店每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_daily_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/MemberMonthlyRegisterProportionDetail')
class MemberMonthlyRegisterProportionDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_monthly_list_po)
    def post(self):
        """
        查询每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_member_monthly_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMonthlyRegisterProportionDetail')
class StoreMemberMonthlyRegisterProportionDetailController(Resource):
    
    @ns_2.doc(security='key')
    @ns_2.response(401, "Token authorized error")
    @authorized
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_monthly_list_po)
    def post(self):
        """
        查询门店每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        current_app.logger.info("Param: " + str(ns_2.payload))
        return IncomeAnalyseServiceImpl.get_store_member_monthly_register_proportion_detail_data(ns_2.payload)
