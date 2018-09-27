from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns_2


crm_total_income_report_model = ns_2.model('MemberTotalIncomeReportModel', {
    'member_type': fields.String(readOnly=True, description="会员类型"),
    'sales_income': fields.Float(readOnly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readOnly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readOnly=True, description="消费人数"),
    'order_amount': fields.Integer(readOnly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readOnly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readOnly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readOnly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readOnly=True, description="客单件(件)"),
    'compared_with_lyst': fields.Float(readOnly=True, description="去年同比"),
})

crm_total_income_report_list_model = ns_2.model('MemberTotalIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_total_income_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

crm_total_daily_income_detail_model = ns_2.model('MemberTotalDailyIncomeDetailModel', {
    'sales_income': fields.Float(readOnly=True, description="销售收入(元)"),
    'compared_with_lyst': fields.Float(readOnly=True, description="去年同比"),
    'date': fields.String(readOnly=True, description="日期")
})

crm_total_daily_income_detail_list_model = ns_2.model('MemberTotalDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(crm_total_daily_income_detail_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readOnly=True, description="返回结果信息")
})

crm_total_monthly_income_detail_model = ns_2.model('MemberTotalMonthlyIncomeDetailModel', {
    'sales_income': fields.Float(readOnly=True, description="销售收入(元)"),
    'compared_with_lyst': fields.Float(readOnly=True, description="去年同比"),
    'month': fields.String(readOnly=True, description="月份")
})

crm_total_monthly_income_detail_list_model = ns_2.model('MemberTotalMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(crm_total_monthly_income_detail_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readOnly=True, description="返回结果信息")
})
