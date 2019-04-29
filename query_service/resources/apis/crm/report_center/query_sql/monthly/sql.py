MONTHLY_SALES = """
    SELECT
        brand_code,
        brand_name,
        channel_type,
        mr_member_type AS member_type,
        CASE kpi
            WHEN 'order_fact_amount_with_coupon' THEN '消费金额'
            WHEN 'member_quantity' THEN '会员人数'
            WHEN 'order_quantity' THEN '单数'
            WHEN 'order_item_quantity' THEN '件数'
            WHEN 'order_amount' THEN '吊牌价'
            WHEN 'apt' THEN 'APT'
            WHEN 'upt' THEN 'UPT'
            WHEN 'apu' THEN '件单价'
            WHEN 'order_discount' THEN '折扣'
        ELSE NULL END AS kpi,
        CASE kpi
            WHEN 'order_fact_amount_with_coupon' THEN 1
            WHEN 'member_quantity' THEN 2
            WHEN 'order_quantity' THEN 3
            WHEN 'order_item_quantity' THEN 4
            WHEN 'order_amount' THEN 5
            WHEN 'apt' THEN 6
            WHEN 'upt' THEN 7
            WHEN 'apu' THEN 8
            WHEN 'order_discount' THEN 9
        ELSE NULL END AS kpi_num,
        mtd,
        mtd_tg,
        mtd_tg_rc,
        mtd_ly,
        mtd_ly_cp,
        mtd_lm,
        mtd_lm_cp,
        qtd,
        qtd_tg,
        qtd_tg_rc,
        qtd_ly,
        qtd_ly_cp,
        ytd,
        ytd_tg,
        ytd_tg_rc,
        ytd_ly,
        ytd_ly_cp,
        year_month AS report_time
    FROM ads_crm.monthly_report_sales
    WHERE brand_code IN ({brand_codes})
        AND channel_type IN ({channel_types})
        AND mr_member_type IN ({mr_member_types})
        ANd kpi IN ({kpis})
        AND year_month = '{year_month}'
"""