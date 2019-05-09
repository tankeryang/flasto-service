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
    'new_svip_member_amount': fields.Integer(readonly=True, description="会员招募-(SVIP会员, 金卡会员)"),
    'new_vip_member_amount': fields.Integer(readonly=True, description="会员招募-(VIP会员, 银卡会员)"),
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


monthly_report_sales_ro = ns.model('CrmMonthlyReportSalesRO', {
    'brand_code': fields.String(readonly=True, description="品牌编码"),
    'brand_name': fields.String(readonly=True, description="品牌名称"),
    'channel_type': fields.String(readonly=True, description="渠道"),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'kpi': fields.String(readonly=True, description="kpi"),
    'mtd': fields.Float(readonly=True, description="实际(MTD)"),
    'mtd_tg': fields.Float(readonly=True, description="目标(MTD)"),
    'mtd_tg_rc': fields.Float(readonly=True, description="达成率(MTD)"),
    'mtd_ly': fields.Float(readonly=True, description="同期(MTD)"),
    'mtd_ly_cp': fields.Float(readonly=True, description="同比(MTD)"),
    'mtd_lm': fields.Float(readonly=True, description="上月(MTD)"),
    'mtd_lm_cp': fields.Float(readonly=True, description="环比(MTD)"),
    'qtd': fields.Float(readonly=True, description="实际(QTD)"),
    'qtd_tg': fields.Float(readonly=True, description="目标(QTD)"),
    'qtd_tg_rc': fields.Float(readonly=True, description="达成率(QTD)"),
    'qtd_ly': fields.Float(readonly=True, description="同期(QTD)"),
    'qtd_ly_cp': fields.Float(readonly=True, description="同比(QTD)"),
    'ytd': fields.Float(readonly=True, description="实际(YTD)"),
    'ytd_tg': fields.Float(readonly=True, description="目标(YTD)"),
    'ytd_tg_rc': fields.Float(readonly=True, description="达成率(YTD)"),
    'ytd_ly': fields.Float(readonly=True, description="同期(YTD)"),
    'ytd_ly_cp': fields.Float(readonly=True, description="同比(YTD)"),
    'report_time': fields.String(readonly=True, description="报告时间(格式为: yyyy-mm)")
})
monthly_report_sales_ro_list = ns.model('CrmMonthlyReportSalesListRO', {
    'data': fields.List(fields.Nested(monthly_report_sales_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

monthly_report_asset_ro = ns.model('CrmMonthlyAssetRO', {
    'brand_code': fields.String(readonly=True, description="品牌编码"),
    'brand_name': fields.String(readonly=True, description="品牌名称"),
    'channel_type': fields.String(readonly=True, description="渠道"),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'member_quantity': fields.Integer(readonly=True, description='会员人数'),
    'year': fields.Integer(readonly=True, description='报告年份'),
    'month': fields.Integer(readonly=True, description='报告月份')
})
monthly_report_asset_ro_list = ns.model('CrmMonthlyReportAssetListRO', {
    'data': fields.List(fields.Nested(monthly_report_asset_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})

monthly_report_active_ro = ns.model('CrmMonthlyActiveRO', {
    'brand_code': fields.String(readonly=True, description="品牌编码"),
    'brand_name': fields.String(readonly=True, description="品牌名称"),
    'channel_type': fields.String(readonly=True, description="渠道"),
    'member_type': fields.String(readonly=True, description="会员类型"),
    'member_quantity': fields.Integer(readonly=True, description='会员人数'),
    'year': fields.Integer(readonly=True, description='报告年份'),
    'month': fields.Integer(readonly=True, description='报告月份')
})
monthly_report_active_ro_list = ns.model('CrmMonthlyReportActiveListRO', {
    'data': fields.List(fields.Nested(monthly_report_active_ro)),
    'success': fields.Boolean(description="查询是否成功"),
    'message': fields.String(description="返回结果信息")
})
