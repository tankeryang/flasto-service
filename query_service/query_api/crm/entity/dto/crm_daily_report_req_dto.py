from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns_1


crm_daily_report_req_dto_model = ns_1.model('CrmDailyReportReqDtoModel', {
    'sales_areas': fields.List(fields.String(description="大区", example='全国'), required=True),
    'cities': fields.List(fields.String(description="城市", example='广州市'), required=True),
    'store_codes': fields.List(fields.String(description="门店编码", example='1102'), required=True),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-01-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-08-10')
})