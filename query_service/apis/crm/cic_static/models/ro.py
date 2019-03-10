from flask_restplus import fields
from ..views import ns


cic_static_ro = ns.model('CicStaticRO', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'register_member_amount': fields.Integer(readonly=True, description="新增会员数"),
    'rma_compared_with_ydst': fields.Float(readonly=True, description="日环比"),
    'rma_compared_with_lwst': fields.Float(readonly=True, description="周环比"),
    'rma_compared_with_lmst': fields.Float(readonly=True, description="月环比"),
})
cic_static_list_ro = ns.model('CicStaticDetailListRO', {
    'data': fields.List(fields.Nested(cic_static_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
