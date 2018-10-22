from flask_restplus import fields
from query_service.query_web.crm.controller.cic_static_controller import ns_0


cic_static_dto = ns_0.model('CicStaticReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True)
})
