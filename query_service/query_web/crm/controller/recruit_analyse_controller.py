from flask_restplus import Resource, Namespace

ns_4 = Namespace('CRM 招募会员', path='/crm/recruit', description='招募会员api')

from query_service.query_biz.crm.service.impl.recruit_analyse_service_impl import RecruitAnalyseServiceImpl

import query_service.query_api.crm.entity.dto.recruit as dto
import query_service.query_api.crm.entity.po.recruit as po


@ns_4.route('/RecruitAmountReport')
class RecruitAmountReportController(Resource):
    
    @ns_4.expect(dto.recruit_analyse_zone_dto)
    @ns_4.marshal_with(po.recruit_amount_list_po)
    def post(self):
        """
        查询招募会员详情
        招募会员，有消费会员，未消费会员
        """
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
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
        return RecruitAnalyseServiceImpl() \
            .get_store_recruit_unconsumed_amount_monthly_detail_data(ns_4.payload)
