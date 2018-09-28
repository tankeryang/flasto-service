from flask_restplus import Resource, Namespace
ns_1 = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')

from query_service.query_biz.crm.service.impl import ReportCenterServiceImpl

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_1.route('/DailyReport')
class CrmDailyReportController(Resource):
    service = ReportCenterServiceImpl()
    
    @ns_1.expect(dto.report_center.DAILY_DTO, validate=True)
    @ns_1.marshal_with(po.report_center.DAILY_LIST)
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        return CrmDailyReportController.service.get_daily_report_data(ns_1.payload)
