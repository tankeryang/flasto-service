from flask_restplus import fields
from query_service.query_web.crm.controller.income_analyse_controller import ns_2


income_analyse_zone_dto = ns_2.model('MemberAnalyseReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True),
    'country': fields.List(fields.String(description="全国", example='中国')),
    'sales_areas': fields.List(fields.String(description="大区", example='华南')),
    'sales_districts': fields.List(fields.String(description="片区", example='暂无数据, 请置空')),
    'provinces': fields.List(fields.String(description="省份", example='广东省')),
    'cities': fields.List(fields.String(description="城市", example='广州市')),
    'sales_modes': fields.List(fields.String(description="门店类别", example='正价', enum=['全部', '正价', '长特', '短特']), required=True),
    'store_types': fields.List(fields.String(description="门店类型", example='MALL', enum=['全部', 'MALL', '百货', '专卖店']), required=True),
    'store_levels': fields.List(fields.String(description="门店等级", example='A', enum=['全部', 'I', 'A', 'B', 'C', 'D']), required=True),
    'channel_types': fields.List(fields.String(description="经营方式/渠道", example='自营', enum=['全部', '自营', '联营', '特许']), required=True),
    'order_channels': fields.List(fields.String(description="订单类型(线上/线下)", example='线下', enum=['全部', '线上', '线下']), required=True),
    'trade_source': fields.List(fields.String(description="订单渠道(FPOS/IPOS/OMIS/官网/其他)", example='FPOS', enum=['全部', 'FPOS', 'IPOS', 'OMIS', '官网', '其他']), required=True),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-11-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-11-30')
})


income_analyse_store_dto = ns_2.model('MemberAnalyseStoreReqDtoModel', {
    'brands': fields.List(fields.String(description="品牌名", example="FivePlus"), required=True),
    'store_codes': fields.List(fields.String(description="门店编码", example="1102"), required=True),
    'order_channels': fields.List(fields.String(description="订单类型(线上/线下)", example='线下', enum=['全部', '线上', '线下']), required=True),
    'trade_source': fields.List(fields.String(description="订单渠道(FPOS/IPOS/OMIS/官网/其他)", example='FPOS', enum=['全部', 'FPOS', 'IPOS', 'OMIS', '官网', '其他']), required=True),
    'start_date': fields.Date(required=True, description="开始日期(yyyy-mm-dd)", example='2018-11-01'),
    'end_date': fields.Date(required=True, description="结束日期(yyyy-mm-dd)", example='2018-11-30')
})
