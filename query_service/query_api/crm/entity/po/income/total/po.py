from flask_restplus import fields
from query_service.query_web.crm.controller.income_analyse_controller import ns_2


ALL = ns_2.model('MemberTotalIncomeReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
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
ALL_LIST = ns_2.model('MemberTotalIncomeReportListModel', {
    'data': fields.List(fields.Nested(ALL)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


DAILY = ns_2.model('MemberTotalDailyIncomeDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_type': fields.String(readOnly=True, description="会员类型"),
    'sales_income': fields.Float(readOnly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readOnly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readOnly=True, description="去年同比"),
    'date': fields.String(readOnly=True, description="日期")
})
DAILY_LIST = ns_2.model('MemberTotalDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(DAILY)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readOnly=True, description="返回结果信息")
})


MONTHLY = ns_2.model('MemberTotalMonthlyIncomeDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_type': fields.String(readOnly=True, description="会员类型"),
    'sales_income': fields.Float(readOnly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readOnly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readOnly=True, description="去年同比"),
    'year': fields.String(readOnly=True, description="年份"),
    'month': fields.String(readOnly=True, description="月份")
})
MONTHLY_LIST = ns_2.model('MemberTotalMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(MONTHLY)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readOnly=True, description="返回结果信息")
})
