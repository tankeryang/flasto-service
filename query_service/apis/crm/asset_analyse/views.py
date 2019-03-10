from flask import current_app
from flask_restplus import Namespace, Resource

ns = Namespace('CRM 会员资产', path='/crm/asset', description='会员资产api')

from .models import qo, ro
from .service import AssetAnalyseService
from .utils.validator import AssetAnalyseStoreQOValidator, AssetAnalyseZoneQOValidator

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
        res, err = AssetAnalyseZoneQOValidator().load(payload)
    elif field == 'store':
        res, err = AssetAnalyseStoreQOValidator().load(payload)
    else:
        raise ControllerError("internal call error!")

    if err:
        current_app.logger.error("Err: " + str(err))
        return dict(success=False, message=err)
    else:
        current_app.logger.info("Param: " + str(res))
        return service_method(res)


@ns.route('/MemberAmountReport')
class MemberAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberAmountReport')
class StoreMemberAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberNewOldAmountReport')
class MemberNewOldAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_newold_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询新老会员数
        新会员数/占比，老会员数/占比
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_new_old_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberNewOldAmountReport')
class StoreMemberNewOldAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_newold_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店新老会员数
        新会员数/占比，老会员数/占比
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_new_old_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberLevelAmountReport')
class MemberLevelAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_level_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_level_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberLevelAmountReport')
class StoreMemberLevelAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_level_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店会员等级数
        普通会员数/占比，VIP会员数/占比
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_level_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberRemainAmountReport')
class MemberRemainAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_remain_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询会员留存数
        留存会员数/占比，流失会员数/占比
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_remain_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberRemainAmountReport')
class StoreMemberRemainAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_remain_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店留存会员数
        留存会员数/占比，流失会员数/占比
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_remain_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberActiveAmountReport')
class MemberActiveAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_active_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询活跃会员数
        活跃会员数/占比，沉默会员数/占比，睡眠会员数/占比，预流失会员数/占比
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_active_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberActiveAmountReport')
class StoreMemberActiveAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_active_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店活跃会员数
        活跃会员数/占比，沉默会员数/占比，睡眠会员数/占比，预流失会员数/占比
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_active_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberFrequencyAmountReport')
class MemberFrequencyAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_frequency_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询累计消费频次会员数
        1, 2, 3, >=4
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_frequency_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberFrequencyAmountReport')
class StoreMemberFrequencyAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_frequency_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店累计消费频次会员数
        1, 2, 3, >=4
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_frequency_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberRecencyAmountReport')
class MemberRecencyAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_recency_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询最近一次消费次会员数
        <3, 3-5, 6-8, >9
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_recency_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberRecencyAmountReport')
class StoreMemberRecencyAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_recency_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店最近一次消费次会员数
        <3, 3-5, 6-8, >9
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_recency_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberMonetaryAmountReport')
class MemberMonetaryAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_monetary_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询累计消费金额次会员数
        <1500, 1500-2799, 3800-5000, >5000
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_monetary_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberMonetaryAmountReport')
class StoreMemberMonetaryAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_monetary_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店累计消费金额次会员数
        <1500, 1500-2799, 3800-5000, >5000
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_monetary_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberTimeAmountReport')
class MemberTimeAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_time_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询入会时长会员数
        <1, 1-3, 3-5, >5
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_time_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberTimeAmountReport')
class StoreMemberTimeAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_time_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店入会时长会员数
        <1, 1-3, 3-5, >5
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_time_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberDiscountAmountReport')
class MemberDiscountAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_discount_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询折扣率会员数
        <50, 50-69, 70-89, >=90
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_discount_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberDiscountAmountReport')
class StoreMemberDiscountAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_discount_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店折扣率会员数
        <50, 50-69, 70-89, >=90
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_discount_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/MemberSipoAmountReport')
class MemberSipoAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_zone_qo)
    @ns.marshal_with(ro.member_sipo_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询客单价会员数
        <1400, 1400-1799, 1800-2199, >=2200
        """
        try:
            return controller('zone', ns.payload, AssetAnalyseService.get_member_sipo_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)


@ns.route('/StoreMemberSipoAmountReport')
class StoreMemberSipoAmountReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.asset_analyse_store_qo)
    @ns.marshal_with(ro.member_sipo_amount_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询门店客单价会员数
        <1400, 1400-1799, 1800-2199, >=2200
        """
        try:
            return controller('store', ns.payload, AssetAnalyseService.get_store_member_sipo_amount_report_data)
        except ControllerError as e:
            current_app.logger.exception(e)
