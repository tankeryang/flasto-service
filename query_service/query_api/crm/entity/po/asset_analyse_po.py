from flask_restplus import fields
from query_service.query_web.crm.controller.crm_controller import ns_3


member_amount_po = ns_3.model('MemberAmountReportModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'register_member_amount': fields.Integer(readOnly=True, description="当前全部会员数"),
    'rma_compared_with_ystd': fields.Float(readOnly=True, description="当前全部会员数环比(昨日/前日)"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员数"),
    'consumed_member_amount_proportion': fields.Float(readOnly=True, description="有消费会员数占比"),
    'cma_compared_with_ystd': fields.Float(readOnly=True, description="有消费会员数环比(昨日/前日)"),
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
