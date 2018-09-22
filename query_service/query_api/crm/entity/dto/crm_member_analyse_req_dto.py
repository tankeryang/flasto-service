from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns_1


crm_member_analyse_req_dto_model = ns_1.model('CrmMemberAnalyseReqDtoModel', {
    'sales_modes': fields.List(fields.String(description="门店类别", example='正价'), required=True),
    'store_types': fields.List(fields.String(description="门店类型", example='MALL'), required=True),
    'store_levels': fields.List(fields.String(description="门店等级", example='A'), required=True),
    'channel_types': fields.List(fields.String(description="经营方式/渠道", example='自营'), required=True),
    'order_channels': fields.List(fields.String(description="订单类型(线上/线下)", example='线下'), required=True),
    'country': fields.List(fields.String(description="全国", example='全国')),
    'sales_areas': fields.List(fields.String(description="大区", example='华东')),
    'sales_districts': fields.List(fields.String(description="片区", example='暂无数据')),
    'provinces': fields.List(fields.String(description="省份", example='广东省')),
    'cities': fields.List(fields.String(description="城市", example='广州市')),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-01-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-08-10')
})