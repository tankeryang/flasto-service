from flask_restplus import fields
from query_service.query_web.crm.controller.crm_controller import ns_3


member_amount_po = ns_3.model('CrmMemberAmountDetailModel', {
    'brand': fields.String(readOnly=True, description="品牌名"),
    'zone': fields.String(readOnly=True, description="查询范围"),
    'register_member_amount': fields.Integer(readOnly=True, description="当前全部会员"),
    'consumed_member_amount': fields.Integer(readOnly=True, description="有消费会员"),
    'unconsumed_member_amount': fields.Integer(readOnly=True, description="未消费会员")
})
member_amount_list_po = ns_3.model('MemberAmountDetailListModel', {
    'data': fields.List(fields.Nested(member_amount_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})