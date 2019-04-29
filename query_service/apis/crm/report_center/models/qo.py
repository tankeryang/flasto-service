from flask_restplus import fields
from ..views import ns


daily_report_qo = ns.model('CrmDailyReportQO', {
    'brand_code': fields.String(description="品牌编号", enum=['2', '3', '6'], example='2', required=True),
    'channel_type': fields.String(description="经营方式", enum=['自营', '联营'], example='自营', required=True),
    'sales_areas': fields.List(fields.String(description="大区(看全国就传'全国')", example='华南')),
    'cities': fields.List(fields.String(description="城市", example='广州市')),
    'company_names': fields.List(fields.String(description="门店上级公司"), example=['广州赫斯汀服饰有限公司']),
    'store_codes': fields.List(fields.String(description="门店编码", example='1102')),
    'start_date': fields.Date(description="开始日期(yyyy-mm-dd)", example='2018-10-01', required=True),
    'end_date': fields.Date(description="结束日期(yyyy-mm-dd)", example='2018-10-31', required=True)
})

monthly_report_sales_qo = ns.model('CrmMonthlyReportSalesQO', {
    'brand_code': fields.List(fields.String(description="品牌编号"), example=['2', '3', '6'], required=True),
    'channel_type': fields.List(fields.String(description="渠道"), example=['自营', '特许', '官网'], required=True),
    'member_type': fields.List(fields.String(
        description="会员类别",
        enum=[
            '整体会员', '普通会员', 'VIP', '新会员', '新会员-普通会员', '新会员-VIP', '老会员', '老会员-普通会员', '老会员-VIP'
        ]), example=['新会员-VIP', '老会员-VIP'], required=True),
    'kpi': fields.List(fields.String(
        description="kpi",
        enum=[
            'order_fact_amount_with_coupon',
            'member_quantity',
            'order_quantity',
            'order_item_quantity',
            'order_amount',
            'apt',
            'upt',
            'apu',
            'order_discount'
        ]), example=['order_fact_amount_with_coupon', 'apt'], required=True),
    'report_time': fields.String(description="报告时间(格式为: yyyy-mm)", required=True)
})
