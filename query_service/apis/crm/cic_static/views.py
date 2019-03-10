from flask import current_app
from flask_restplus import Resource, Namespace

ns = Namespace('CRM cic首页静态展示', path='/crm/cic', description='cic 首页静态数据 api')

from .models import qo, ro
from .service import CicStaticService
from .utils.validator import CicStaticQOValidator

from query_service.apis.utils.decorator import authorized


@ns.route('/CicStaticMainPageDetail')
class CicStaticMainPageDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.cic_static_qo)
    @ns.marshal_with(ro.cic_static_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询cic首页静态展示数据
        昨日新增(招募)会员，日环比，周环比，月环比
        """
        res, err = CicStaticQOValidator().load(ns.payload)
        
        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return CicStaticService.get_cic_static_detail_data(res)
