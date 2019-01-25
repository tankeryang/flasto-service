from flask_restplus import fields
from query_service.query_web.crm.controller.member_grouping_controller import ns_5


member_grouping_list_po = ns_5.model('MemberGroupingListModel', {
    'data': fields.List(fields.String(readonly=True, description="会员编号列表")),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
