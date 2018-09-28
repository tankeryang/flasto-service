from flask_restplus import fields
from query_service.query_web.crm.controller.income_analyse_controller import ns_2

STORE_DTO = ns_2.model('MemberAnalyseStoreReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True),
    'store_codes': fields.List(fields.String(description="门店编码", example="1102"), required=True),
    'order_channels': fields.List(fields.String(required=True, description="订单类型(线上/线下)", example='线下'), required=True),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-01-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-08-10')
})
