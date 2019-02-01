from flask import current_app
from flask_restplus import Resource, Namespace

ns_0 = Namespace('CRM cic首页静态展示', path='/crm/cic', description='cic 首页静态数据 api')

from query_service.query_biz.crm.service.impl.cic_static_service_impl import CicStaticServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.cic_static as dto
import query_service.query_api.crm.entity.po.cic_static as po


@ns_0.route('/CicStaticMainPageDetail')
class CicStaticMainPageDetailController(Resource):
    
    @ns_0.doc(security='key')
    @ns_0.expect(dto.cic_static_dto, validate=True)
    @ns_0.marshal_with(po.cic_static_list_po)
    @ns_0.response(401, "Token authorized error")
    @authorized
    def post(self):
        """
        查询cic首页静态展示数据
        昨日新增(招募)会员，日环比，周环比，月环比
        """
        current_app.logger.info("Param: " + str(ns_0.payload))
        return CicStaticServiceImpl.get_cic_static_detail_data(ns_0.payload)
