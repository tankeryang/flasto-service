from flask_restplus import Resource, Namespace

ns_1 = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')
ns_2 = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')
ns_3 = Namespace('CRM 客户资产', path='/crm/asset', description='客户资产api')

from query_service.query_biz.crm.service.impl import (
    ReportCenterServiceImpl,
    IncomeAnalyseServiceImpl,
    AssetAnalyseServiceImpl,
)

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_1.route('/DailyReport')
class CrmDailyReportController(Resource):
    service = ReportCenterServiceImpl()
    
    @ns_1.expect(dto.daily_report_dto, validate=True)
    @ns_1.marshal_with(po.daily_report_list_po)
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        return CrmDailyReportController.service.get_daily_report_data(ns_1.payload)


@ns_2.route('/TotalIncomeReport')
class TotalIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        return TotalIncomeReportController.service \
            .get_total_income_report_data(ns_2.payload)


@ns_2.route('/StoreTotalIncomeReport')
class StoreTotalIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询门店整体收入分析
        整体，会员，非会员
        """
        return StoreTotalIncomeReportController.service \
            .get_store_total_income_report_data(ns_2.payload)


@ns_2.route('/TotalDailyIncomeDetail')
class TotalDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询整体收入每日趋势
        整体销售收入，同比，日期
        """
        return TotalDailyIncomeDetailController.service \
            .get_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalDailyIncomeDetail')
class StoreTotalDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询门店整体收入每日趋势
        整体销售收入，同比，日期
        """
        return StoreTotalDailyIncomeDetailController.service \
            .get_store_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/TotalMonthlyIncomeDetail')
class TotalMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询整体收入每月趋势
        整体销售收入，同比，月份
        """
        return TotalMonthlyIncomeDetailController.service \
            .get_total_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalMonthlyIncomeDetail')
class StoreTotalMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询门店整体收入每月趋势
        整体销售收入，同比，月份
        """
        return StoreTotalMonthlyIncomeDetailController.service \
            .get_store_total_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberNowBeforeIncomeReport')
class MemberNowBeforeIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.now_before_all_list_po)
    def post(self):
        """
        查询会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        return MemberNowBeforeIncomeReportController.service \
            .get_member_now_before_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberNowBeforeIncomeReport')
class StoreMemberNowBeforeIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.now_before_all_list_po)
    def post(self):
        """
        查询门店会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        return StoreMemberNowBeforeIncomeReportController.service \
            .get_store_member_now_before_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldIncomeReport')
class MemberNewOldIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        return MemberNewOldIncomeReportController.service \
            .get_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldIncomeReport')
class StoreMemberNewOldIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询门店新老会员收入分析
        会员，新会员，老会员
        """
        return StoreMemberNewOldIncomeReportController.service \
            .get_store_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldDailyIncomeDetail')
class MemberNewOldDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return MemberNewOldDailyIncomeDetailController.service \
            .get_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldDailyIncomeDetail')
class StoreMemberNewOldDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        return StoreMemberNewOldDailyIncomeDetailController.service \
            .get_store_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberNewOldMonthlyIncomeDetail')
class MemberNewOldMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询新老会员每月收入趋势
        会员，新会员，老会员
        """
        return MemberNewOldMonthlyIncomeDetailController.service \
            .get_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldMonthlyIncomeDetail')
class StoreMemberNewOldMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询门店新老会员每月收入趋势
        会员，新会员，老会员
        """
        return StoreMemberNewOldMonthlyIncomeDetailController.service \
            .get_store_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelIncomeReport')
class MemberLevelIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        return MemberLevelIncomeReportController.service \
            .get_member_level_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelIncomeReport')
class StoreMemberLevelIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询门店会员等级收入分析
        会员，普通会员，VIP会员
        """
        return StoreMemberLevelIncomeReportController.service \
            .get_store_member_level_income_report_data(ns_2.payload)


@ns_2.route('/MemberLevelDailyIncomeDetail')
class MemberLevelDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        return MemberLevelDailyIncomeDetailController.service \
            .get_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询门店会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        return StoreMemberLevelDailyIncomeDetailController.service \
            .get_store_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelMonthlyIncomeDetail')
class MemberLevelMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        return MemberLevelMonthlyIncomeDetailController.service \
            .get_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelMonthlyIncomeDetail')
class StoreMemberLevelMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询门店会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        return StoreMemberLevelMonthlyIncomeDetailController.service \
            .get_store_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimIncomeReport')
class MemberMulDimIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return MemberMulDimIncomeReportController.service \
            .get_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimIncomeReport')
class StoreMemberMulDimIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询门店多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return StoreMemberMulDimIncomeReportController.service \
            .get_store_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/MemberMulDimDailyIncomeDetail')
class MemberMulDimDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return MemberMulDimDailyIncomeDetailController.service \
            .get_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimDailyIncomeDetail')
class StoreMemberMulDimDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询门店多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return StoreMemberMulDimDailyIncomeDetailController.service \
            .get_store_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimMonthlyIncomeDetail')
class MemberMulDimMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return MemberMulDimMonthlyIncomeDetailController.service \
            .get_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimMonthlyIncomeDetail')
class StoreMemberMulDimMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询门店多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return StoreMemberMulDimMonthlyIncomeDetailController.service \
            .get_store_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberRegisterProportionReport')
class CrmMemberRegisterProportionReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_list_po)
    def post(self):
        """
        查询登记率
        登记率
        """
        return CrmMemberRegisterProportionReportController.crm_service \
            .get_crm_member_register_proportion_report_data(ns_2.payload)


@ns_3.route('/MemberAmountDetail')
class CrmMemberAmountDetailController(Resource):
    service = AssetAnalyseServiceImpl()
    
    @ns_3.expect(dto.member_analyse_zone_dto)
    @ns_3.marshal_with(po.member_amount_list_po)
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return CrmMemberAmountDetailController.service.get_member_amount_detail(ns_3.payload)
