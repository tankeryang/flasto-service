from flask_restplus import fields
from ..views import ns


total_all_ro = ns.model('MemberTotalIncomeReportRO', {
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
total_all_list_ro = ns.model('MemberTotalIncomeReportListRO', {
    'data': fields.List(fields.Nested(total_all_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


total_daily_ro = ns.model('MemberTotalDailyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
total_daily_list_ro = ns.model('MemberTotalDailyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(total_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readonly=True, description="返回结果信息")
})


total_monthly_ro = ns.model('MemberTotalMonthlyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
total_monthly_list_ro = ns.model('MemberTotalMonthlyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(total_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(readonly=True, description="返回结果信息")
})


now_before_all_ro = ns.model('MemberNowBeforeIncomeReportRO', {
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
now_before_all_list_ro = ns.model('MemberNowBeforeIncomeReportListRO', {
    'data': fields.List(fields.Nested(now_before_all_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_all_ro = ns.model('MemberNewOldIncomeReportRO', {
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
new_old_all_list_ro = ns.model('MemberNewOldIncomeReportListRO', {
    'data': fields.List(fields.Nested(new_old_all_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_daily_ro = ns.model('MemberNewOldDailyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
new_old_daily_list_ro = ns.model('MemberNewOldDailyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(new_old_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


new_old_monthly_ro = ns.model('MemberNewOldMonthlyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
new_old_monthly_list_ro = ns.model('MemberNewOldMonthlyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(new_old_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


level_all_ro = ns.model('MemberLevelIncomeReportRO', {
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
level_all_list_ro = ns.model('MemberLevelIncomeReportListRO', {
    'data': fields.List(fields.Nested(level_all_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

level_daily_ro = ns.model('MemberLevelDailyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
level_daily_list_ro = ns.model('MemberLevelDailyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(level_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


level_monthly_ro = ns.model('MemberLevelMonthlyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_lyst': fields.Float(readonly=True, description="去年同比"),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
level_monthly_list_ro = ns.model('MemberLevelMonthlyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(level_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_all_ro = ns.model('MemberMulDimIncomeReportRO', {
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
mul_dim_all_list_ro = ns.model('MemberMulDimIncomeReportListRO', {
    'data': fields.List(fields.Nested(mul_dim_all_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_daily_ro = ns.model('MemberMulDimDailyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_newold_type': fields.String(readonly=True, description="新老会员类型"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'date': fields.String(readonly=True, description="日期")
})
mul_dim_daily_list_ro = ns.model('MemberMulDimDailyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(mul_dim_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


mul_dim_monthly_ro = ns.model('MemberMulDimMonthlyIncomeDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_newold_type': fields.String(readonly=True, description="新老会员类型"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'sales_income': fields.Float(readonly=True, description="销售收入(元)"),
    'sales_income_proportion': fields.Float(readonly=True, description='销售收入(占比)'),
    'compared_with_ss_lyst': fields.Float(readonly=True, description="同店同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
mul_dim_monthly_list_ro = ns.model('MemberMulDimMonthlyIncomeDetailListRO', {
    'data': fields.List(fields.Nested(mul_dim_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_ro = ns.model('MemberRegisterProportionReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率")
})
rgp_list_ro = ns.model('MemberRegisterProportionReportListRO', {
    'data': fields.List(fields.Nested(rgp_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_daily_ro = ns.model('MemberDailyRegisterProportionReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率"),
    'date': fields.String(readonly=True, description="日期")
})
rgp_daily_list_ro = ns.model('MemberDailyRegisterProportionReportListRO', {
    'data': fields.List(fields.Nested(rgp_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


rgp_monthly_ro = ns.model('MemberMonthlyRegisterProportionReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_proportion': fields.Float(readonly=True, description="登记率"),
    'year_month': fields.String(readonly=True, description="年-月")
})
rgp_monthly_list_ro = ns.model('MemberMonthlyRegisterProportionReportListRO', {
    'data': fields.List(fields.Nested(rgp_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
