from flask_restplus import fields
from ..views import ns


recruit_amount_ro = ns.model('RecruitAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readonly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readonly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readonly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readonly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readonly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readonly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readonly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readonly=True, description="未消费会员数同比")
})
recruit_amount_list_ro = ns.model('RecruitAmountReportListRO', {
    'data': fields.List(fields.Nested(recruit_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_amount_daily_ro = ns.model('RecruitAmountDailyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readonly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readonly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readonly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readonly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readonly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readonly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readonly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readonly=True, description="未消费会员数同比"),
    'date': fields.String(readonly=True, description="日期")
})
recruit_amount_daily_list_ro = ns.model('RecruitAmountDailyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_amount_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_amount_monthly_ro = ns.model('RecruitAmountMonthlyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'register_member_amount': fields.Integer(readonly=True, description="招募会员数"),
    'rma_compared_with_lyst': fields.Float(readonly=True, description="招募会员同比"),
    'consumed_member_amount': fields.Integer(readonly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readonly=True, description="有消费会员数占比"),
    'cma_compared_with_lyst': fields.Float(readonly=True, description="有消费会员数同比"),
    'unconsumed_member_amount': fields.Integer(readonly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readonly=True, description="未消费会员数占比"),
    'uma_compared_with_lyst': fields.Float(readonly=True, description="未消费会员数同比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
recruit_amount_monthly_list_ro = ns.model('RecruitAmountMonthlyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_amount_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_consumed_amount_daily_ro = ns.model('RecruitConsumedAmountDailyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_recruit_type': fields.String(readonly=True, description="招募会员类型"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readonly=True, description="占比"),
    'date': fields.String(readonly=True, description="日期")
})
recruit_consumed_amount_daily_list_ro = ns.model('RecruitConsumedAmountDailyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_consumed_amount_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_consumed_amount_monthly_ro = ns.model('RecruitConsumedAmountMonthlyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_recruit_type': fields.String(readonly=True, description="招募会员类型"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readonly=True, description="占比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
recruit_consumed_amount_monthly_list_ro = ns.model('RecruitConsumedAmountMonthlyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_consumed_amount_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_unconsumed_amount_daily_ro = ns.model('RecruitUnconsumedAmountDailyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_register_type': fields.String(readonly=True, description="会员注册类型"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readonly=True, description="占比"),
    'date': fields.String(readonly=True, description="日期")
})
recruit_unconsumed_amount_daily_list_ro = ns.model('RecruitUnconsumedAmountDailyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_unconsumed_amount_daily_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


recruit_unconsumed_amount_monthly_ro = ns.model('RecruitUnconsumedAmountMonthlyDetailRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.List(fields.String(readonly=True, description="查询范围")),
    'member_register_type': fields.String(readonly=True, description="会员注册类型"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'member_amount_proportion': fields.Float(readonly=True, description="占比"),
    'year_month': fields.String(readonly=True, description="年-月")
})
recruit_unconsumed_amount_monthly_list_ro = ns.model('RecruitUnconsumedAmountMonthlyDetailListRO', {
    'data': fields.List(fields.Nested(recruit_unconsumed_amount_monthly_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
