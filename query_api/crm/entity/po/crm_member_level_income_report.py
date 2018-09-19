from flask_restplus import fields
from query_api.crm.service.crm_service import ns


crm_member_level_income_report_model = ns.model('CrmMemberLevelIncomeModel', {
    'member_type': fields.String(readOnly=True, description="会员类型"),
    'sales_income': fields.Float(readOnly=True, description="销售收入(万元)"),
    'sales_income_proportion': fields.Float(readOnly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readOnly=True, description="消费人数"),
    'order_amount': fields.Integer(readOnly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readOnly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readOnly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readOnly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readOnly=True, description="客单件(件)"),
    'sales_income_growth': fields.Float(readOnly=True, description="同比增长(%)")
})

crm_member_level_income_report_list_model = ns.model('CrmMemberLevelIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_member_level_income_report_model)),
    'success': fields.Boolean(description="查询是否成功")
})