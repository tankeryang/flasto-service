from flask_restplus import fields
from query_service.query_web.crm.controller.cic_static_controller import ns_0


cic_static_po = ns_0.model('CicStaticDetailModel', {
    'brand': fields.String(readonly=True, description="品牌名"),
    'register_member_amount': fields.Integer(readonly=True, description="新增会员数"),
    'rma_compared_with_ydst': fields.Float(readonly=True, description="日环比"),
    'rma_compared_with_lwst': fields.Float(readonly=True, description="周环比"),
    'rma_compared_with_lmst': fields.Float(readonly=True, description="月环比"),
})
cic_static_list_po = ns_0.model('CicStaticDetailListModel', {
    'data': fields.List(fields.Nested(cic_static_po)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})