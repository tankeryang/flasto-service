from flask_restplus import fields
from ..views import ns


member_amount_ro = ns.model('MemberAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'register_member_amount': fields.Integer(readonly=True, description="当前全部会员数"),
    'consumed_member_amount': fields.Integer(readonly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readonly=True, description="有消费会员数占比"),
    'unconsumed_member_amount': fields.Integer(readonly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readonly=True, description="未消费会员数占比")
})
member_amount_list_ro = ns.model('MemberAmountReportListRO', {
    'data': fields.List(fields.Nested(member_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_newold_amount_ro = ns.model('MemberNewOldAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'new_member_amount': fields.Integer(readonly=True, description="新会员数"),
    'new_member_amount_proportion': fields.Float(readonly=True, description="新会员数占比"),
    'old_member_amount': fields.Integer(readonly=True, description="老会员数"),
    'old_member_amount_proportion': fields.Float(readonly=True, description="老会员数占比"),
})
member_newold_amount_list_ro = ns.model('MemberNewOldAmountReportListRO', {
    'data': fields.List(fields.Nested(member_newold_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_level_amount_ro = ns.model('MemberLevelAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_level_type': fields.String(readonly=True, description="会员等级类型"),
    'member_level_amount': fields.Integer(readonly=True, description="会员数"),
    'member_level_amount_proportion': fields.Float(readonly=True, description="会员数占比")
})
member_level_amount_list_ro = ns.model('MemberLevelAmountReportListRO', {
    'data': fields.List(fields.Nested(member_level_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_remain_amount_ro = ns.model('MemberRemainAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'remain_member_amount': fields.Integer(readonly=True, description="留存会员数"),
    'remain_member_amount_proportion': fields.Float(readonly=True, description="留存会员数占比"),
    'lost_member_amount': fields.Integer(readonly=True, description="流失会员数"),
    'lost_member_amount_proportion': fields.Float(readonly=True, description="流失员数占比"),
})
member_remain_amount_list_ro = ns.model('MemberRemainAmountReportListRO', {
    'data': fields.List(fields.Nested(member_remain_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_active_amount_ro = ns.model('MemberActiveAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'active_member_amount': fields.Integer(readonly=True, description="活跃会员数"),
    'active_member_amount_proportion': fields.Float(readonly=True, description="活跃会员数占比"),
    'silent_member_amount': fields.Integer(readonly=True, description="沉默会员数"),
    'silent_member_amount_proportion': fields.Float(readonly=True, description="沉默会员数占比"),
    'sleep_member_amount': fields.Integer(readonly=True, description="睡眠会员数"),
    'sleep_member_amount_proportion': fields.Float(readonly=True, description="睡眠会员数占比"),
    'pre_lost_member_amount': fields.Integer(readonly=True, description="预流失会员数"),
    'pre_lost_member_amount_proportion': fields.Float(readonly=True, description="预流失会员数占比"),
})
member_active_amount_list_ro = ns.model('MemberActiveAmountReportListRO', {
    'data': fields.List(fields.Nested(member_active_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_time_amount_ro = ns.model('MemberTimeAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'time': fields.String(readonly=True, description="入会时长")
})
member_time_amount_list_ro = ns.model('MemberTimeAmountReportListRO', {
    'data': fields.List(fields.Nested(member_time_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_discount_amount_ro = ns.model('MemberDiscountAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'discount': fields.String(readonly=True, description="折扣率")
})
member_discount_amount_list_ro = ns.model('MemberDiscountAmountReportListRO', {
    'data': fields.List(fields.Nested(member_discount_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_sipo_amount_ro = ns.model('MemberSipoAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'sales_income_per_order': fields.String(readonly=True, description="客单价")
})
member_sipo_amount_list_ro = ns.model('MemberSipoAmountReportListRO', {
    'data': fields.List(fields.Nested(member_sipo_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_frequency_amount_ro = ns.model('MemberFrequencyAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'frequency': fields.String(readonly=True, description="累计消费频次")
})
member_frequency_amount_list_ro = ns.model('MemberFrequencyAmountReportListRO', {
    'data': fields.List(fields.Nested(member_frequency_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_recency_amount_ro = ns.model('MemberRecencyAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'recency': fields.String(readonly=True, description="最近一次消费")
})
member_recency_amount_list_ro = ns.model('MemberRecencyAmountReportListRO', {
    'data': fields.List(fields.Nested(member_recency_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_monetary_amount_ro = ns.model('MemberMonetaryAmountReportRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'zone': fields.String(readonly=True, description="查询范围"),
    'member_amount': fields.Integer(readonly=True, description="会员数"),
    'monetary': fields.String(readonly=True, description="累计消费金额")
})
member_monetary_amount_list_ro = ns.model('MemberRecencyAmountReportListRO', {
    'data': fields.List(fields.Nested(member_monetary_amount_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
