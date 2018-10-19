from flask_restplus import fields
from query_service.query_web.crm.controller.recruit_analyse_controller import ns_4


recruit_amount_po = ns_4.model('RecruitAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readOnly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readOnly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readOnly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readOnly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readOnly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readOnly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readOnly=True, description="未消费会员数同比")
})
recruit_amount_list_po = ns_4.model('RecruitAmountReportListModel', {
    'data': fields.List(fields.Nested(recruit_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_amount_daily_po = ns_4.model('RecruitAmountDailyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readOnly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readOnly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readOnly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readOnly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readOnly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readOnly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readOnly=True, description="未消费会员数同比"),
    'date': fields.String(readOnly=True, description="日期")
})
recruit_amount_daily_list_po = ns_4.model('RecruitAmountDailyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_amount_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_amount_monthly_po = ns_4.model('RecruitAmountMonthlyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readOnly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readOnly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readOnly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readOnly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readOnly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readOnly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readOnly=True, description="未消费会员数同比"),
    'year': fields.String(readOnly=True, description="年份"),
    'month': fields.String(readOnly=True, description="月份")
})
recruit_amount_monthly_list_po = ns_4.model('RecruitAmountMonthlyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_amount_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_consumed_amount_daily_po = ns_4.model('RecruitConsumedAmountDailyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'member_recruit_type': fields.String(readOnly=True, description="招募会员类型"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readOnly=True, description="占比"),
    'date': fields.String(readOnly=True, description="日期")
})
recruit_consumed_amount_daily_list_po = ns_4.model('RecruitConsumedAmountDailyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_consumed_amount_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_consumed_amount_monthly_po = ns_4.model('RecruitConsumedAmountMonthlyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'member_recruit_type': fields.String(readOnly=True, description="招募会员类型"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readOnly=True, description="占比"),
    'year': fields.String(readOnly=True, description="年份"),
    'month': fields.String(readOnly=True, description="月份")
})
recruit_consumed_amount_monthly_list_po = ns_4.model('RecruitConsumedAmountMonthlyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_consumed_amount_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_unconsumed_amount_daily_po = ns_4.model('RecruitUnconsumedAmountDailyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'member_register_type': fields.String(readOnly=True, description="会员注册类型"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readOnly=True, description="占比"),
    'date': fields.String(readOnly=True, description="日期")
})
recruit_unconsumed_amount_daily_list_po = ns_4.model('RecruitUnconsumedAmountDailyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_unconsumed_amount_daily_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_unconsumed_amount_monthly_po = ns_4.model('RecruitUnconsumedAmountMonthlyDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.List(fields.String(readOnly=True, description="查询范围")),
    'member_register_type': fields.String(readOnly=True, description="会员注册类型"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readOnly=True, description="占比"),
    'year': fields.String(readOnly=True, description="年份"),
    'month': fields.String(readOnly=True, description="月份")
})
recruit_unconsumed_amount_monthly_list_po = ns_4.model('RecruitUnconsumedAmountMonthlyDetailListModel', {
    'data': fields.List(fields.Nested(recruit_unconsumed_amount_monthly_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
