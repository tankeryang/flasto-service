from flask_restplus import fields
from ..views import ns

cic_static_qo = ns.model('CicStaticQO', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True)
})
