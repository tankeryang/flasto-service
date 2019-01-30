from flask_restplus import fields
from query_service.query_web.crm.controller.income_analyse_controller import ns_2


total_all_po = ns_2.model('MemberTotalIncomeReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readonly=True, description="消费人数"),
    'order_amount': fields.Integer(readonly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readonly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readonly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readonly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readonly=True, description="客单件(件)"),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
})
total_all_list_po = ns_2.model('MemberTotalIncomeReportListModel', {
    'data': fields.List(fields.Nested(total_all_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


total_daily_po = ns_2.model('MemberTotalDailyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
total_daily_list_po = ns_2.model('MemberTotalDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(total_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readonly=True, description="返回结果信息")
})


total_monthly_po = ns_2.model('MemberTotalMonthlyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
total_monthly_list_po = ns_2.model('MemberTotalMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(total_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readonly=True, description="返回结果信息")
})


now_before_all_po = ns_2.model('MemberNowBeforeIncomeReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readonly=True, description="消费人数"),
    'order_amount': fields.Integer(readonly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readonly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readonly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readonly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readonly=True, description="客单件(件)")
})
now_before_all_list_po = ns_2.model('MemberNowBeforeIncomeReportListModel', {
    'data': fields.List(fields.Nested(now_before_all_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_all_po = ns_2.model('MemberNewOldIncomeReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readonly=True, description="消费人数"),
    'order_amount': fields.Integer(readonly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readonly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readonly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readonly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readonly=True, description="客单件(件)"),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
})
new_old_all_list_po = ns_2.model('MemberNewOldIncomeReportListModel', {
    'data': fields.List(fields.Nested(new_old_all_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_daily_po = ns_2.model('MemberNewOldDailyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
new_old_daily_list_po = ns_2.model('MemberNewOldDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(new_old_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_monthly_po = ns_2.model('MemberNewOldMonthlyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
new_old_monthly_list_po = ns_2.model('MemberNewOldMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(new_old_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


level_all_po = ns_2.model('MemberLevelIncomeReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readonly=True, description="消费人数"),
    'order_amount': fields.Integer(readonly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readonly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readonly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readonly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readonly=True, description="客单件(件)"),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
})
level_all_list_po = ns_2.model('MemberLevelIncomeReportListModel', {
    'data': fields.List(fields.Nested(level_all_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

level_daily_po = ns_2.model('MemberLevelDailyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
level_daily_list_po = ns_2.model('MemberLevelDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(level_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


level_monthly_po = ns_2.model('MemberLevelMonthlyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
level_monthly_list_po = ns_2.model('MemberLevelMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(level_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_all_po = ns_2.model('MemberMulDimIncomeReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_newold_type': fields.String(readonly=True, description="新老会员类型"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'customer_amount': fields.Integer(readonly=True, description="消费人数"),
    'order_amount': fields.Integer(readonly=True, description="交易单数"),
    'consumption_frequency': fields.Integer(readonly=True, description="消费频次"),
    'sales_income_per_order': fields.Float(readonly=True, description="客单价(元)"),
    'sales_income_per_item': fields.Float(readonly=True, description="件单价(元)"),
    'sales_item_per_order': fields.Float(readonly=True, description="客单件(件)"),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
})
mul_dim_all_list_po = ns_2.model('MemberMulDimIncomeReportListModel', {
    'data': fields.List(fields.Nested(mul_dim_all_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_daily_po = ns_2.model('MemberMulDimDailyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_newold_type': fields.String(readonly=True, description="新老会员类型"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
mul_dim_daily_list_po = ns_2.model('MemberMulDimDailyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(mul_dim_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_monthly_po = ns_2.model('MemberMulDimMonthlyIncomeDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_newold_type': fields.String(readonly=True, description="新老会员类型"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
mul_dim_monthly_list_po = ns_2.model('MemberMulDimMonthlyIncomeDetailListModel', {
    'data': fields.List(fields.Nested(mul_dim_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_po = ns_2.model('MemberRegisterProportionReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率")
})
rgp_list_po = ns_2.model('MemberRegisterProportionReportListModel', {
    'data': fields.List(fields.Nested(rgp_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_daily_po = ns_2.model('MemberDailyRegisterProportionReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率"),
    'date': fields.String(readonly=True, description="日期")
})
rgp_daily_list_po = ns_2.model('MemberDailyRegisterProportionReportListModel', {
    'data': fields.List(fields.Nested(rgp_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_monthly_po = ns_2.model('MemberMonthlyRegisterProportionReportModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率"),
    'year_month': fields.String(readonly=True, description="年-月")
})
rgp_monthly_list_po = ns_2.model('MemberMonthlyRegisterProportionReportListModel', {
    'data': fields.List(fields.Nested(rgp_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


