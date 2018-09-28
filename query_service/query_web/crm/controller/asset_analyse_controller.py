from flask_restplus import Resource, Namespace
ns_3 = Namespace('CRM 客户资产', path='/crm/asset', description='客户资产api')

from query_service.query_biz.crm.service.impl import AssetAnalyseServiceImpl

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_3.route('/MemberAmountDetail')
class CrmMemberAmountDetailController(Resource):
    service = AssetAnalyseServiceImpl()
    
    @ns_3.expect(dto.member_anlyse.zone.ZONE_DTO)
    @ns_3.marshal_with(po.asset.STATIC_LIST)
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        return CrmMemberAmountDetailController.service.get_member_amount_detail(ns_3.payload)
