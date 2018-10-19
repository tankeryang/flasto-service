from flask_restplus import fields
from query_service.query_web.crm.controller.asset_analyse_controller import ns_3


member_amount_po = ns_3.model('MemberAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'register_member_amount': fields.Integer(readOnly=True, description="当前全部会员数"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readOnly=True, description="有消费会员数占比"),
    'unconsumed_member_amount': fields.Integer(readOnly=True, description="未消费会员数"),
    'unconsumed_member_amount_proportion': fields.Float(readOnly=True, description="未消费会员数占比")
})
member_amount_list_po = ns_3.model('MemberAmountReportListModel', {
    'data': fields.List(fields.Nested(member_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_newold_amount_po = ns_3.model('MemberNewOldAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'new_member_amount': fields.Integer(readOnly=True, description="新会员数"),
    'new_member_amount_proportion': fields.Float(readOnly=True, description="新会员数占比"),
    'old_member_amount': fields.Integer(readOnly=True, description="老会员数"),
    'old_member_amount_proportion': fields.Float(readOnly=True, description="老会员数占比"),
})
member_newold_amount_list_po = ns_3.model('MemberNewOldAmountReportListModel', {
    'data': fields.List(fields.Nested(member_newold_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_level_amount_po = ns_3.model('MemberLevelAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_level_type': fields.String(readOnly=True, description="会员等级类型"),
    'member_level_amount': fields.Integer(readOnly=True, description="会员数"),
    'member_level_amount_proportion': fields.Float(readOnly=True, description="会员数占比")
})
member_level_amount_list_po = ns_3.model('MemberLevelAmountReportListModel', {
    'data': fields.List(fields.Nested(member_level_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_remain_amount_po = ns_3.model('MemberRemainAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'remain_member_amount': fields.Integer(readOnly=True, description="留存会员数"),
    'remain_member_amount_proportion': fields.Float(readOnly=True, description="留存会员数占比"),
    'lost_member_amount': fields.Integer(readOnly=True, description="流失会员数"),
    'lost_member_amount_proportion': fields.Float(readOnly=True, description="流失员数占比"),
})
member_remain_amount_list_po = ns_3.model('MemberRemainAmountReportListModel', {
    'data': fields.List(fields.Nested(member_remain_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_active_amount_po = ns_3.model('MemberActiveAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'active_member_amount': fields.Integer(readOnly=True, description="活跃会员数"),
    'active_member_amount_proportion': fields.Float(readOnly=True, description="活跃会员数占比"),
    'silent_member_amount': fields.Integer(readOnly=True, description="沉默会员数"),
    'silent_member_amount_proportion': fields.Float(readOnly=True, description="沉默会员数占比"),
    'sleep_member_amount': fields.Integer(readOnly=True, description="睡眠会员数"),
    'sleep_member_amount_proportion': fields.Float(readOnly=True, description="睡眠会员数占比"),
    'pre_lost_member_amount': fields.Integer(readOnly=True, description="预流失会员数"),
    'pre_lost_member_amount_proportion': fields.Float(readOnly=True, description="预流失会员数占比"),
})
member_active_amount_list_po = ns_3.model('MemberActiveAmountReportListModel', {
    'data': fields.List(fields.Nested(member_active_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_time_amount_po = ns_3.model('MemberTimeAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'time': fields.String(readOnly=True, description="入会时长")
})
member_time_amount_list_po = ns_3.model('MemberTimeAmountReportListModel', {
    'data': fields.List(fields.Nested(member_time_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_discount_amount_po = ns_3.model('MemberDiscountAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'discount': fields.String(readOnly=True, description="折扣率")
})
member_discount_amount_list_po = ns_3.model('MemberDiscountAmountReportListModel', {
    'data': fields.List(fields.Nested(member_discount_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_sipo_amount_po = ns_3.model('MemberSipoAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'sales_income_per_order': fields.String(readOnly=True, description="客单价")
})
member_sipo_amount_list_po = ns_3.model('MemberSipoAmountReportListModel', {
    'data': fields.List(fields.Nested(member_sipo_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_frequency_amount_po = ns_3.model('MemberFrequencyAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'frequency': fields.String(readOnly=True, description="累计消费频次")
})
member_frequency_amount_list_po = ns_3.model('MemberFrequencyAmountReportListModel', {
    'data': fields.List(fields.Nested(member_frequency_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_recency_amount_po = ns_3.model('MemberRecencyAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'recency': fields.String(readOnly=True, description="最近一次消费")
})
member_recency_amount_list_po = ns_3.model('MemberRecencyAmountReportListModel', {
    'data': fields.List(fields.Nested(member_recency_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_monetary_amount_po = ns_3.model('MemberMonetaryAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'member_amount': fields.Integer(readOnly=True, description="会员数"),
    'monetary': fields.String(readOnly=True, description="累计消费金额")
})
member_monetary_amount_list_po = ns_3.model('MemberRecencyAmountReportListModel', {
    'data': fields.List(fields.Nested(member_monetary_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
