from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns_2


crm_daily_report_req_dto_model = ns_2.model('CrmDailyReportReqDtoModel', {
    'sales_areas': fields.List(fields.String(description="大区", enum=['全国', '华南', '华东', '华北', '华中'])),
    'cities': fields.List(fields.String(description="城市", enum=['广州市', '上海市', '北京市', '深圳市'])),
    'store_codes': fields.List(fields.String(description="门店编码", enum=['1102', '1101'])),
    'start_date': fields.String(required=True, description="开始日期(yyyy-mm-dd)", enum=['2018-01-01']),
    'end_date': fields.String(required=True, description="结束日期(yyyy-mm-dd)", enum=['2018-08-10'])
})