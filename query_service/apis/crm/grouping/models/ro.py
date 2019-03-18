from flask_restplus import fields
from ..views import ns


member_grouping_count_ro = ns.model('MemberGroupingCountRO', {
    'data': fields.Integer(readonly=True, description="分组总数"),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_grouping_csv_ro = ns.model('MemberGroupingCsvRO', {
    'data': fields.String(readonly=True, description="生成csv url"),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})


member_grouping_detail_ro = ns.model('MemberGroupingDetailRO', {
    'member_no': fields.String(readonly=True, description='会员编号'),
    'member_name': fields.String(readonly=True, description='会员姓名'),
    'member_wechat_id': fields.String(readonly=True, description='会员微信名'),
    'member_mobile': fields.String(readonly=True, description='会员手机号'),
    'member_grade_name': fields.String(readonly=True, description='会员等级名'),
    'member_first_order_time': fields.String(readonly=True, description='会员最近购买时间'),
    'member_reg_source': fields.String(readonly=True, description='会员注册渠道')
})
member_grouping_detail_list_ro = ns.model('MemberGroupingDetailListRO', {
    'data': fields.List(fields.Nested(member_grouping_detail_ro), readonly=True, description="会员详情列表"),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

member_grouping_no_list_ro = ns.model('MemberGroupingNoListRO', {
    'data': fields.List(fields.String(readonly=True, description="会员编号"), readonly=True, description="会员编号列表"),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})