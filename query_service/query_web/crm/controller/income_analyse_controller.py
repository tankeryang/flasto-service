from flask_restplus import Resource, Namespace
ns_2 = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')

from query_service.query_biz.crm.service.impl import IncomeAnalyseServiceImpl

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_2.route('/TotalIncomeReport')
class TotalIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.MONTHLY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.total.MONTHLY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.now_before.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.now_before.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.MONTHLY_LIST)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return MemberNewOldMonthlyIncomeDetailController.service \
            .get_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldMonthlyIncomeDetail')
class StoreMemberNewOldMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.new_old.MONTHLY_LIST)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return StoreMemberNewOldMonthlyIncomeDetailController.service \
            .get_store_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelIncomeReport')
class MemberLevelIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.ALL_LIST)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        return MemberLevelIncomeReportController.service \
            .get_member_level_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelIncomeReport')
class StoreMemberLevelIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.ALL_LIST)
    def post(self):
        """
        查询门店新老会员收入分析
        会员，新会员，老会员
        """
        return StoreMemberLevelIncomeReportController.service \
            .get_store_member_level_income_report_data(ns_2.payload)


@ns_2.route('/MemberLevelDailyIncomeDetail')
class MemberLevelDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.DAILY_LIST)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return MemberLevelDailyIncomeDetailController.service \
            .get_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelDailyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.DAILY_LIST)
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        return StoreMemberLevelDailyIncomeDetailController.service \
            .get_store_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelMonthlyIncomeDetail')
class MemberLevelMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.MONTHLY_LIST)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return MemberLevelMonthlyIncomeDetailController.service \
            .get_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelMonthlyIncomeDetailController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.level.MONTHLY_LIST)
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        return StoreMemberLevelMonthlyIncomeDetailController.service \
            .get_store_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimIncomeReport')
class MemberMulDimIncomeReportController(Resource):
    service = IncomeAnalyseServiceImpl()
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.ALL_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.DAILY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.MONTHLY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.store.STORE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.mul_dim.MONTHLY_LIST)
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
    
    @ns_2.expect(dto.member_anlyse.zone.ZONE_DTO, validate=True)
    @ns_2.marshal_with(po.income.member.register_proportion.ALL_LIST)
    def post(self):
        """
        查询登记率
        登记率
        """
        return CrmMemberRegisterProportionReportController.crm_service \
            .get_crm_member_register_proportion_report_data(ns_2.payload)
