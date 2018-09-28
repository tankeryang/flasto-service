from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns_2


crm_member_nowbefore_income_report_model = ns_2.model('MemberNowBeforeIncomeReportModel', {
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
    'sales_item_per_order': fields.Float(readOnly=True, description="客单件(件)")
})

crm_member_nowbefore_income_report_list_model = ns_2.model('MemberNowBeforeIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_member_nowbefore_income_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

crm_member_newold_income_report_model = ns_2.model('MemberNewOldIncomeReportModel', {
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

crm_member_newold_income_report_list_model = ns_2.model('MemberNewOldIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_member_newold_income_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

crm_member_muldim_income_report_model = ns_2.model('MemberMulDimIncomeReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_newold_type': fields.String(readOnly=True, description="新老会员类型"),
    'member_level_type': fields.String(readOnly=True, description="会员等级类型"),
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

crm_member_muldim_income_report_list_model = ns_2.model('MemberMulDimIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_member_muldim_income_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

crm_member_level_income_report_model = ns_2.model('MemberLevelIncomeReportModel', {
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

crm_member_level_income_report_list_model = ns_2.model('MemberLevelIncomeReportListModel', {
    'data': fields.List(fields.Nested(crm_member_level_income_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

crm_member_register_proportion_report_model = ns_2.model('MemberRegisterProportionReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'register_proportion': fields.Float(readOnly=True, description="登记率")
})

crm_member_register_proportion_report_list_model = ns_2.model('MemberRegisterProportionReportListModel', {
    'data': fields.List(fields.Nested(crm_member_register_proportion_report_model)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
