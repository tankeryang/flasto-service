from marshmallow import Schema, fields
from query_service.apis.utils.fields import EnumString, StringDate


class IncomeAnalyseZoneQOValidator(Schema):
    brands = fields.List(fields.String(description="品牌名"), required=True)
    country = fields.List(fields.String(description="全国"))
    sales_areas = fields.List(fields.String(description="大区"))
    sales_districts = fields.List(fields.String(description="片区"))
    provinces = fields.List(fields.String(description="省份"))
    cities = fields.List(fields.String(description="城市"))
    sales_modes = fields.List(EnumString(description="门店类别", enum=['全部', '正价', '长特', '短特']), required=True)
    store_types = fields.List(EnumString(description="门店类型", enum=['全部', 'MALL', '百货', '专卖店']), required=True)
    store_levels = fields.List(EnumString(description="门店等级", enum=['全部', 'I', 'A', 'B', 'C', 'D']), required=True)
    channel_types = fields.List(EnumString(description="经营方式/渠道",  enum=['全部', '自营', '联营', '特许']), required=True)
    order_channels = fields.List(EnumString(description="订单类型(线上/线下)", enum=['全部', '线上', '线下']), required=True)
    trade_source = fields.List(EnumString(
        description="订单渠道(FPOS/IPOS/OMIS/官网/其他)", enum=['全部', 'FPOS', 'IPOS', 'OMIS', '官网', '其他']
    ), required=True)
    start_date = StringDate(description="开始日期(yyyy-mm-dd)", required=True)
    end_date = StringDate(description="结束日期(yyyy-mm-dd)", required=True)


class IncomeAnalyseStoreQOValidator(Schema):
    brands = fields.List(fields.String(description="品牌名"), required=True)
    store_codes = fields.List(fields.String(description="门店编码"), required=True)
    order_channels = fields.List(EnumString(description="订单类型(线上/线下)", enum=['全部', '线上', '线下']), required=True)
    trade_source = fields.List(EnumString(
        description="订单渠道(FPOS/IPOS/OMIS/官网/其他)", enum=['全部', 'FPOS', 'IPOS', 'OMIS', '官网', '其他']
    ), required=True)
    start_date = StringDate(description="开始日期(yyyy-mm-dd)", required=True)
    end_date = StringDate(description="结束日期(yyyy-mm-dd)", required=True)
