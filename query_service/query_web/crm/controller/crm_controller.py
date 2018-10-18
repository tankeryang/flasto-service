from flask_restplus import Resource, Namespace

ns_1 = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')
ns_2 = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')
ns_3 = Namespace('CRM 会员资产', path='/crm/asset', description='会员资产api')
ns_4 = Namespace('CRM 招募会员', path='/crm/recruit', description='招募会员api')

from query_service.query_biz.crm.service.impl import (
    ReportCenterServiceImpl,
    IncomeAnalyseServiceImpl,
    AssetAnalyseServiceImpl,
)

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_1.route('/DailyReport')
class CrmDailyReportController(Resource):
    
    @ns_1.expect(dto.daily_report_dto, validate=True)
    @ns_1.marshal_with(po.daily_report_list_po)
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        return ReportCenterServiceImpl()\
            .get_daily_report_data(ns_1.payload)


@ns_2.route('/TotalIncomeReport')
class TotalIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_total_income_report_data(ns_2.payload)


@ns_2.route('/StoreTotalIncomeReport')
class StoreTotalIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_all_list_po)
    def post(self):
        """
        查询门店整体收入分析
        整体，会员，非会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_total_income_report_data(ns_2.payload)


@ns_2.route('/TotalDailyIncomeDetail')
class TotalDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询整体收入每日趋势
        整体销售收入，同比，日期
        """
        return IncomeAnalyseServiceImpl()\
            .get_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalDailyIncomeDetail')
class StoreTotalDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_daily_list_po)
    def post(self):
        """
        查询门店整体收入每日趋势
        整体销售收入，同比，日期
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_total_daily_income_detail_data(ns_2.payload)


@ns_2.route('/TotalMonthlyIncomeDetail')
class TotalMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询整体收入每月趋势
        整体销售收入，同比，月份
        """
        return IncomeAnalyseServiceImpl()\
            .get_total_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreTotalMonthlyIncomeDetail')
class StoreTotalMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.total_monthly_list_po)
    def post(self):
        """
        查询门店整体收入每月趋势
        整体销售收入，同比，月份
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_total_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberNowBeforeIncomeReport')
class MemberNowBeforeIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.now_before_all_list_po)
    def post(self):
        """
        查询会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_now_before_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberNowBeforeIncomeReport')
class StoreMemberNowBeforeIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.now_before_all_list_po)
    def post(self):
        """
        查询门店会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_now_before_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldIncomeReport')
class MemberNewOldIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldIncomeReport')
class StoreMemberNewOldIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_all_list_po)
    def post(self):
        """
        查询门店新老会员收入分析
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_new_old_income_report_data(ns_2.payload)


@ns_2.route('/MemberNewOldDailyIncomeDetail')
class MemberNewOldDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询新老会员每日收入趋势
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldDailyIncomeDetail')
class StoreMemberNewOldDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_daily_list_po)
    def post(self):
        """
        查询门店新老会员每日收入趋势
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_new_old_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberNewOldMonthlyIncomeDetail')
class MemberNewOldMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询新老会员每月收入趋势
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberNewOldMonthlyIncomeDetail')
class StoreMemberNewOldMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.new_old_monthly_list_po)
    def post(self):
        """
        查询门店新老会员每月收入趋势
        会员，新会员，老会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_new_old_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelIncomeReport')
class MemberLevelIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_level_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelIncomeReport')
class StoreMemberLevelIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_all_list_po)
    def post(self):
        """
        查询门店会员等级收入分析
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_level_income_report_data(ns_2.payload)


@ns_2.route('/MemberLevelDailyIncomeDetail')
class MemberLevelDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelDailyIncomeDetail')
class StoreMemberLevelDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_daily_list_po)
    def post(self):
        """
        查询门店会员等级每日收入趋势
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_level_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberLevelMonthlyIncomeDetail')
class MemberLevelMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberLevelMonthlyIncomeDetail')
class StoreMemberLevelMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.level_monthly_list_po)
    def post(self):
        """
        查询门店会员等级每月收入趋势
        会员，普通会员，VIP会员
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_level_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimIncomeReport')
class MemberMulDimIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimIncomeReport')
class StoreMemberMulDimIncomeReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_all_list_po)
    def post(self):
        """
        查询门店多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_mul_dim_income_report_data(ns_2.payload)


@ns_2.route('/MemberMulDimDailyIncomeDetail')
class MemberMulDimDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimDailyIncomeDetail')
class StoreMemberMulDimDailyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_daily_list_po)
    def post(self):
        """
        查询门店多维度每日收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_mul_dim_daily_income_detail_data(ns_2.payload)


@ns_2.route('/MemberMulDimMonthlyIncomeDetail')
class MemberMulDimMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMulDimMonthlyIncomeDetail')
class StoreMemberMulDimMonthlyIncomeDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.mul_dim_monthly_list_po)
    def post(self):
        """
        查询门店多维度每月收入趋势
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_mul_dim_monthly_income_detail_data(ns_2.payload)


@ns_2.route('/MemberRegisterProportionReport')
class MemberRegisterProportionReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_list_po)
    def post(self):
        """
        查询登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_register_proportion_report_data(ns_2.payload)


@ns_2.route('/StoreMemberRegisterProportionReport')
class StoreMemberRegisterProportionReportController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_list_po)
    def post(self):
        """
        查询门店登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_register_proportion_report_data(ns_2.payload)


@ns_2.route('/MemberDailyRegisterProportionDetail')
class MemberDailyRegisterProportionDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_daily_list_po)
    def post(self):
        """
        查询每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_daily_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberDailyRegisterProportionDetail')
class StoreMemberDailyRegisterProportionDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_daily_list_po)
    def post(self):
        """
        查询门店每日登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_daily_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/MemberMonthlyRegisterProportionDetail')
class MemberMonthlyRegisterProportionDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_zone_dto, validate=True)
    @ns_2.marshal_with(po.rgp_monthly_list_po)
    def post(self):
        """
        查询每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_member_monthly_register_proportion_detail_data(ns_2.payload)


@ns_2.route('/StoreMemberMonthlyRegisterProportionDetail')
class StoreMemberMonthlyRegisterProportionDetailController(Resource):
    
    @ns_2.expect(dto.income_analyse_store_dto, validate=True)
    @ns_2.marshal_with(po.rgp_monthly_list_po)
    def post(self):
        """
        查询门店每月登记率
        登记率：新会员单 / 新会员单 + 非会员单
        """
        return IncomeAnalyseServiceImpl()\
            .get_store_member_monthly_register_proportion_detail_data(ns_2.payload)


@ns_3.route('/MemberAmountReport')
class MemberAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_amount_list_po)
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl()\
            .get_member_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberAmountReport')
class StoreMemberAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_amount_list_po)
    def post(self):
        """
        查询门店会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl()\
            .get_store_member_amount_report_data(ns_3.payload)
    


@ns_3.route('/MemberNewOldAmountReport')
class MemberNewOldAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_newold_amount_list_po)
    def post(self):
        """
        查询新老会员数
        新会员数/占比，老会员数/占比
        """
        return AssetAnalyseServiceImpl()\
            .get_member_new_old_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberNewOldAmountReport')
class StoreMemberNewOldAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_newold_amount_list_po)
    def post(self):
        """
        查询门店新老会员数
        新会员数/占比，老会员数/占比
        """
        return AssetAnalyseServiceImpl()\
            .get_store_member_new_old_amount_report_data(ns_3.payload)


@ns_3.route('/MemberLevelAmountReport')
class MemberLevelAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_level_amount_list_po)
    def post(self):
        """
        查询会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        return AssetAnalyseServiceImpl()\
            .get_member_level_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberLevelAmountReport')
class StoreMemberLevelAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_level_amount_list_po)
    def post(self):
        """
        查询门店会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        return AssetAnalyseServiceImpl()\
            .get_store_member_level_amount_report_data(ns_3.payload)


@ns_3.route('/MemberRemainAmountReport')
class MemberRemainAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_remain_amount_list_po)
    def post(self):
        """
        查询会员留存数
        留存会员数/占比，流失会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_member_remain_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberRemainAmountReport')
class StoreMemberRemainAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_remain_amount_list_po)
    def post(self):
        """
        查询门店留存会员数
        留存会员数/占比，流失会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_remain_amount_report_data(ns_3.payload)


@ns_3.route('/MemberActiveAmountReport')
class MemberActiveAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_active_amount_list_po)
    def post(self):
        """
        查询活跃会员数
        活跃会员数/占比，沉默会员数/占比，睡眠会员数/占比，预流失会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_member_active_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberActiveAmountReport')
class StoreMemberActiveAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_active_amount_list_po)
    def post(self):
        """
        查询门店活跃会员数
        活跃会员数/占比，沉默会员数/占比，睡眠会员数/占比，预流失会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_active_amount_report_data(ns_3.payload)


@ns_3.route('/MemberFrequencyAmountReport')
class MemberFrequencyAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_frequency_amount_list_po)
    def post(self):
        """
        查询累计消费频次会员数
        1, 2, 3, >=4
        """
        return AssetAnalyseServiceImpl() \
            .get_member_frequency_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberFrequencyAmountReport')
class StoreMemberFrequencyAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_frequency_amount_list_po)
    def post(self):
        """
        查询门店累计消费频次会员数
        1, 2, 3, >=4
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_frequency_amount_report_data(ns_3.payload)


@ns_3.route('/MemberRecencyAmountReport')
class MemberRecencyAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_recency_amount_list_po)
    def post(self):
        """
        查询最近一次消费次会员数
        <3, 3-5, 6-8, >9
        """
        return AssetAnalyseServiceImpl() \
            .get_member_recency_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberRecencyAmountReport')
class StoreMemberRecencyAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_recency_amount_list_po)
    def post(self):
        """
        查询门店最近一次消费次会员数
        <3, 3-5, 6-8, >9
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_recency_amount_report_data(ns_3.payload)


@ns_3.route('/MemberMonetaryAmountReport')
class MemberMonetaryAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_monetary_amount_list_po)
    def post(self):
        """
        查询累计消费金额次会员数
        <1500, 1500-2799, 3800-5000, >5000
        """
        return AssetAnalyseServiceImpl() \
            .get_member_monetary_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberMonetaryAmountReport')
class StoreMemberMonetaryAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_monetary_amount_list_po)
    def post(self):
        """
        查询门店累计消费金额次会员数
        <1500, 1500-2799, 3800-5000, >5000
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_monetary_amount_report_data(ns_3.payload)


@ns_3.route('/MemberTimeAmountReport')
class MemberTimeAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_time_amount_list_po)
    def post(self):
        """
        查询入会时长会员数
        <1, 1-3, 3-5, >5
        """
        return AssetAnalyseServiceImpl() \
            .get_member_time_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberTimeAmountReport')
class StoreMemberTimeAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_time_amount_list_po)
    def post(self):
        """
        查询门店入会时长会员数
        <1, 1-3, 3-5, >5
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_time_amount_report_data(ns_3.payload)


@ns_3.route('/MemberDiscountAmountReport')
class MemberDiscountAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_discount_amount_list_po)
    def post(self):
        """
        查询折扣率会员数
        <50, 50-69, 70-89, >=90
        """
        return AssetAnalyseServiceImpl() \
            .get_member_discount_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberDiscountAmountReport')
class StoreMemberDiscountAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_discount_amount_list_po)
    def post(self):
        """
        查询门店折扣率会员数
        <50, 50-69, 70-89, >=90
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_discount_amount_report_data(ns_3.payload)


@ns_3.route('/MemberSipoAmountReport')
class MemberSipoAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_sipo_amount_list_po)
    def post(self):
        """
        查询客单价会员数
        <1400, 1400-1799, 1800-2199, >=2200
        """
        return AssetAnalyseServiceImpl() \
            .get_member_sipo_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberSipoAmountReport')
class StoreMemberSipoAmountReportController(Resource):
    
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_sipo_amount_list_po)
    def post(self):
        """
        查询门店客单价会员数
        <1400, 1400-1799, 1800-2199, >=2200
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_sipo_amount_report_data(ns_3.payload)


@ns_4.route('/RecruitAmountReport')
class RecruitAmountReportController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_amount_list_po)
    def post(self):
        """
        查询招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_amount_report_data(ns_4.payload)


@ns_4.route('/StoreRecruitAmountReport')
class StoreRecruitAmountReportController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_amount_list_po)
    def post(self):
        """
        查询门店招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_amount_report_data(ns_4.payload)


@ns_4.route('/RecruitAmountDailyDetail')
class RecruitAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_amount_daily_list_po)
    def post(self):
        """
        查询每日招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitAmountDailyDetail')
class StoreRecruitAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_amount_daily_list_po)
    def post(self):
        """
        查询门店每日招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/RecruitAmountMonthlyDetail')
class RecruitAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_amount_monthly_list_po)
    def post(self):
        """
        查询每月招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_amount_monthly_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitAmountMonthlyDetail')
class StoreRecruitAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_amount_monthly_list_po)
    def post(self):
        """
        查询门店每月招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_amount_monthly_detail_data(ns_4.payload)


@ns_4.route('/RecruitConsumedAmountDailyDetail')
class RecruitConsumedAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_consumed_amount_daily_list_po)
    def post(self):
        """
        查询有消费会员每日详情
        普通会员，VIP会员，升级会员
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_consumed_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/RecruitConsumedAmountMonthlyDetail')
class RecruitConsumedAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_consumed_amount_monthly_list_po)
    def post(self):
        """
        查询有消费会员每月详情
        普通会员，VIP会员，升级会员
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_consumed_amount_monthly_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitConsumedAmountDailyDetail')
class StoreRecruitConsumedAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_consumed_amount_daily_list_po)
    def post(self):
        """
        查询门店有消费会员每日详情
        普通会员，VIP会员，升级会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_consumed_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitConsumedAmountMonthlyDetail')
class StoreRecruitConsumedAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_consumed_amount_monthly_list_po)
    def post(self):
        """
        查询门店有消费会员每月详情
        普通会员，VIP会员，升级会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_consumed_amount_monthly_detail_data(ns_4.payload)


@ns_4.route('/RecruitUnconsumedAmountDailyDetail')
class RecruitUnconsumedAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_unconsumed_amount_daily_list_po)
    def post(self):
        """
        查询未消费会员每日详情
        官网注册，门店注册
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_unconsumed_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/RecruitUnconsumedAmountMonthlyDetail')
class RecruitUnconsumedAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_unconsumed_amount_monthly_list_po)
    def post(self):
        """
        查询未消费会员每月详情
        官网注册，门店注册
        """
        return AssetAnalyseServiceImpl() \
            .get_recruit_unconsumed_amount_monthly_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitUnconsumedAmountDailyDetail')
class StoreRecruitUnconsumedAmountDailyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_unconsumed_amount_daily_list_po)
    def post(self):
        """
        查询门店未消费会员每日详情
        官网注册，门店注册
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_unconsumed_amount_daily_detail_data(ns_4.payload)


@ns_4.route('/StoreRecruitUnconsumedAmountMonthlyDetail')
class StoreRecruitUnconsumedAmountMonthlyDetailController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_store_dto)
    @ns_4.marshal_with(po.recruit_unconsumed_amount_monthly_list_po)
    def post(self):
        """
        查询门店未消费会员每月详情
        官网注册，门店注册
        """
        return AssetAnalyseServiceImpl() \
            .get_store_recruit_unconsumed_amount_monthly_detail_data(ns_4.payload)
