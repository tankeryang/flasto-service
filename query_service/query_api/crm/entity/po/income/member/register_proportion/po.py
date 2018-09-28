from flask_restplus import fields
from query_service.query_web.crm.controller.income_analyse_controller import ns_2


ALL = ns_2.model('MemberRegisterProportionReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'register_proportion': fields.Float(readOnly=True, description="登记率")
})
ALL_LIST = ns_2.model('MemberRegisterProportionReportListModel', {
    'data': fields.List(fields.Nested(ALL)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
