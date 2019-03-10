from flask_restplus import fields
from ..views import ns

daily_report_ro = ns.model('CrmDailyReportRO', {
    'sales_area': fields.String(readonly=True, description="区域"),
    'city': fields.String(readonly=True, description="城市"),
    'store_code': fields.String(readonly=True, description="门店"),
    'company_name': fields.String(readonly=True, description="上级公司名"),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'sales_amount': fields.Float(readonly=True, description="销售金额"),
    'sales_amount_proportion': fields.Float(readonly=True, description="销售金额占比"),
    'sales_amount_proportion_total': fields.Float(readonly=True, description="销售金额占比汇总"),
    'last_year_same_time_sales_amount': fields.Float(readonly=True, description="去年同期销售金额"),
    'like_for_like_sales_growth': fields.Float(readonly=True, description="销售同比增长"),
    'sales_item_quantity': fields.Integer(readonly=True, description="销售件数"),
    'discount_rate': fields.Float(readonly=True, description="折扣"),
    'member_amount': fields.Integer(readonly=True, description="消费会员"),
    'past_12_month_remain_member_amount': fields.Integer(readonly=True, description="上月存量"),
    'second_trade_rate': fields.Float(readonly=True, description="回头率"),
    'new_vip_member_amount': fields.Integer(readonly=True, description="会员招募-VIP"),
    'new_normal_member_amount': fields.Integer(readonly=True, description="会员招募-普通会员"),
    'upgraded_member_amount': fields.Integer(readonly=True, description="会员升级"),
    'store_amount': fields.Integer(readonly=True, description="店铺数"),
    'member_amount_per_store': fields.Float(readonly=True, description="店均消费总数"),
    'sales_amount_per_member': fields.Float(readonly=True, description="人均销售金额"),
    'sales_item_quantity_per_member': fields.Float(readonly=True, description="人均销售件数"),
    'su_per_member': fields.Float(readonly=True, description="人均SU"),
    'order_amount_per_member': fields.Float(readonly=True, description="人均次"),
})
daily_report_list_ro = ns.model('CrmDailyReportListRO', {
    'data': fields.List(fields.Nested(daily_report_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
