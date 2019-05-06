from marshmallow import Schema, fields
from query_service.apis.utils.fields import EnumString, StringDate


class DailyReportQOValidator(Schema):
    brand_code = EnumString(description="品牌编号", enum=['2', '3', '6'], required=True)
    channel_type = EnumString(description="经营方式", enum=['自营', '联营'], required=True)
    sales_areas = fields.List(fields.String(description="大区(看全国就传'全国')"))
    cities = fields.List(fields.String(description="城市"))
    company_names = fields.List(fields.String(description="门店上级公司"))
    store_codes = fields.List(fields.String(description="门店编码"))
    start_date = StringDate(description="开始日期(yyyy-mm-dd)", required=True)
    end_date = StringDate(description="结束日期(yyyy-mm-dd)", required=True)


class MonthlyReportSalesQOValidator(Schema):
    brand_code = fields.List(fields.String(description="品牌编码"), required=True)
    channel_type = fields.List(fields.String(description="渠道"), required=True)
    member_type = fields.List(fields.String(description="会员类型"), required=True)
    report_time = fields.String(description="报告时间", required=True)


class MonthlyReportAssetQOValidator(Schema):
    brand_code = fields.List(fields.String(description="品牌编码"), required=True)
    channel_type = fields.List(fields.String(description="渠道"), required=True)
    member_type = fields.List(fields.String(description="会员类型"), required=True)
    report_time = fields.String(description="报告时间", required=True)


class MonthlyReportActiveQOValidator(Schema):
    brand_code = fields.List(fields.String(description="品牌编码"), required=True)
    channel_type = fields.List(fields.String(description="渠道"), required=True)
    report_time = fields.String(description="报告时间", required=True)
