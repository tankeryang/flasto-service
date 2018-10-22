from flask_restplus import fields
from query_service.query_web.crm.controller.asset_analyse_controller import ns_3


asset_analyse_zone_dto = ns_3.model('AssetAnalyseReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True),
    'country': fields.List(fields.String(description="全国", example='中国')),
    'sales_areas': fields.List(fields.String(description="大区", example='华南')),
    'sales_districts': fields.List(fields.String(description="片区", example='暂无数据, 请置空')),
    'provinces': fields.List(fields.String(description="省份", example='广东省')),
    'cities': fields.List(fields.String(description="城市", example='广州市')),
    'sales_modes': fields.List(fields.String(required=True, description="门店类别", example='正价'), required=True),
    'store_types': fields.List(fields.String(required=True, description="门店类型", example='MALL'), required=True),
    'store_levels': fields.List(fields.String(required=True, description="门店等级", example='A'), required=True),
    'channel_types': fields.List(fields.String(required=True, description="经营方式/渠道", example='自营'), required=True),
    'order_channels': fields.List(fields.String(required=True, description="订单类型(线上/线下)", example='线下'), required=True),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-08-10')
})

asset_analyse_store_dto = ns_3.model('AssetAnalyseStoreReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True),
    'store_codes': fields.List(fields.String(description="门店编码", example="1102"), required=True),
    'order_channels': fields.List(fields.String(required=True, description="订单类型(线上/线下)", example='线下'), required=True),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-08-10')
})