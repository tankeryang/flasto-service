from flask_restplus import fields
from query_service.query_web.crm.controller.report_center_controller import ns_1


daily_report_dto = ns_1.model('CrmDailyReportReqDtoModel', {
    'brand_code': fields.String(description="品牌编码", example='2', required=True),
    'sales_areas': fields.List(fields.String(description="大区(看全国就传'全国')", example='华南')),
    'cities': fields.List(fields.String(description="城市", example='广州市')),
    'store_codes': fields.List(fields.String(description="门店编码", example='1102')),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-10-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-10-31')
})
