from flask_restplus import Resource, Namespace

ns_1 = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')

from query_service.query_biz.crm.service.impl.report_center_service_impl import ReportCenterServiceImpl
from query_service.query_web.crm.utils import authorized

import query_service.query_api.crm.entity.dto.report_center as dto
import query_service.query_api.crm.entity.po.report_center as po


@ns_1.route('/DailyReport')
class CrmDailyReportController(Resource):
    
    @ns_1.doc(security='key')
    @ns_1.expect(dto.daily_report_dto, validate=True)
    @ns_1.marshal_with(po.daily_report_list_po)
    @ns_1.response(401, "Token authorized error")
    @authorized
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        return ReportCenterServiceImpl.get_daily_report_data(ns_1.payload)
