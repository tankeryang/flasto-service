MONTHLY_SALES = """
    SELECT
        brand_code,
        brand_name,
        channel_type,
        mr_member_type AS member_type,
        kpi,
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
    WHERE
        brand_code IN ({brand_codes})
        channel_type IN ({channel_types})
        mr_member_type IN ({mr_member_types})
        kpi IN ({kpis})
        year_month = '{year_month}'
"""