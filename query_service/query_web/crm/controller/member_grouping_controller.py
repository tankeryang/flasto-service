from flask import current_app
from flask_restplus import Resource, Namespace

ns_5 = Namespace('CRM 会员分组', path='/crm/grouping', description='会员分组api')

from query_service.query_biz.crm.service.impl.member_grouping_service_impl import MemberGroupingServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.grouping as dto
import query_service.query_api.crm.entity.po.grouping as po


@ns_5.route('/MemberGrouping')
class MemberGroupingController(Resource):
    
    @ns_5.doc(security='key')
    @ns_5.response(401, "Token authorized error")
    @authorized
    @ns_5.expect(dto.member_grouping_dto, validate=True)
    @ns_5.marshal_with(po.member_grouping_list_po)
    def post(self):
        """
        根据分组参数查询会员列表
        """
        current_app.logger.info("Param: " + str(ns_5.payload))
        return MemberGroupingServiceImpl.get_member_grouping_list(ns_5.payload)
