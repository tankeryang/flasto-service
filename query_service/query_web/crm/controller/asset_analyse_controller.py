from flask_restplus import Resource, Namespace

ns_3 = Namespace('CRM 会员资产', path='/crm/asset', description='会员资产api')

from query_service.query_biz.crm.service.impl.asset_analyse_service_impl import AssetAnalyseServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.asset as dto
import query_service.query_api.crm.entity.po.asset as po


@ns_3.route('/MemberAmountReport')
class MemberAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_amount_list_po)
    @ns_3.response(401, "Token authorized error")
    @authorized
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_member_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberAmountReport')
class StoreMemberAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_amount_list_po)
    def post(self):
        """
        查询门店会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_amount_report_data(ns_3.payload)


@ns_3.route('/MemberNewOldAmountReport')
class MemberNewOldAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_newold_amount_list_po)
    def post(self):
        """
        查询新老会员数
        新会员数/占比，老会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_member_new_old_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberNewOldAmountReport')
class StoreMemberNewOldAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_newold_amount_list_po)
    def post(self):
        """
        查询门店新老会员数
        新会员数/占比，老会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_new_old_amount_report_data(ns_3.payload)


@ns_3.route('/MemberLevelAmountReport')
class MemberLevelAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_zone_dto)
    @ns_3.marshal_with(po.member_level_amount_list_po)
    def post(self):
        """
        查询会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_member_level_amount_report_data(ns_3.payload)


@ns_3.route('/StoreMemberLevelAmountReport')
class StoreMemberLevelAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_level_amount_list_po)
    def post(self):
        """
        查询门店会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_level_amount_report_data(ns_3.payload)


@ns_3.route('/MemberRemainAmountReport')
class MemberRemainAmountReportController(Resource):
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
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
    
    @ns_3.doc(security='key')
    @ns_3.response(401, "Token authorized error")
    @authorized
    @ns_3.expect(dto.asset_analyse_store_dto)
    @ns_3.marshal_with(po.member_sipo_amount_list_po)
    def post(self):
        """
        查询门店客单价会员数
        <1400, 1400-1799, 1800-2199, >=2200
        """
        return AssetAnalyseServiceImpl() \
            .get_store_member_sipo_amount_report_data(ns_3.payload)
