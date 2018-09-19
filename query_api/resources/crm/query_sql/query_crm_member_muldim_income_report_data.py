SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA = """
    SELECT DISTINCT
        matl.member_newold_type,
        matl.member_level_type,
        cast(IF(sm.si IS NOT NULL, sm.si, 0) AS DECIMAL(10, 3))  AS sales_income,
        cast(IF(IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 100.00 / IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0), 0) AS DECIMAL(10, 2)) AS sales_income_proportion,
        cast(IF(sm.ca IS NOT NULL, sm.ca, 0) AS INTEGER) AS customer_amount,
        cast(IF(sm.oa IS NOT NULL, sm.oa, 0) AS INTEGER) AS order_amount,
        cast(IF(IF(sm.ca IS NOT NULL, sm.ca, 0) != 0, IF(sm.oa IS NOT NULL, sm.oa, 0) / IF(sm.ca IS NOT NULL, sm.ca, 0), 0) AS INTEGER) AS consumption_frequency,
        cast(IF(IF(sm.oa IS NOT NULL, sm.oa, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 10000.0 / IF(sm.oa IS NOT NULL, sm.oa, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_order,
        cast(IF(IF(sm.siq IS NOT NULL, sm.siq, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 10000.0 / IF(sm.siq IS NOT NULL, sm.siq, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_item,
        cast(IF(IF(sm.oa IS NOT NULL, sm.oa, 0) != 0, IF(sm.siq IS NOT NULL, sm.siq, 0) / IF(sm.oa IS NOT NULL, sm.oa, 0), 0) AS INTEGER) AS sales_item_per_order,
        cast(IF(IF(lyst.si IS NOT NULL, lyst.si, 0) != 0, (IF(sm.si IS NOT NULL, sm.si, 0) - IF(lyst.si IS NOT NULL, lyst.si, 0)) * 100.0 / IF(lyst.si IS NOT NULL, lyst.si, 0), 0) AS DECIMAL(10, 2)) AS sales_income_growth
    FROM (
        SELECT DISTINCT
            {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_newold_type, member_level_type
        FROM cdm_crm.member_analyse_type_label
        WHERE member_type = '会员' AND member_newold_type IN ('新会员', '老会员') AND member_level_type IN ('普通会员', 'VIP会员')
    ) matl
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_newold_type, member_level_type,
        sum(mab.order_fact_amount) * 1.0 / 10000  AS si,
        count(distinct member_no)                 AS ca,
        count(distinct mab.outer_order_no)        AS oa,
        sum(mab.order_item_quantity)              AS siq
        FROM cdm_crm.member_analyse_base mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_newold_type, member_level_type
    ) sm
    ON matl.{zone} = sm.{zone}
    AND matl.order_channel = sm.order_channel
    AND matl.sales_mode = sm.sales_mode
    AND matl.store_type = sm.store_type
    AND matl.store_level = sm.store_level
    AND matl.channel_type = sm.channel_type
    AND matl.member_newold_type = sm.member_newold_type
    AND matl.member_level_type = sm.member_level_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
        sum(mab.order_fact_amount) *1.0 / 10000 AS ttsi
        FROM cdm_crm.member_analyse_base mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        AND member_type = '会员'
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ) smtt
    ON matl.{zone} = smtt.{zone}
    AND matl.order_channel = smtt.order_channel
    AND matl.sales_mode = smtt.sales_mode
    AND matl.store_type = smtt.store_type
    AND matl.store_level = smtt.store_level
    AND matl.channel_type = smtt.channel_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_newold_type, member_level_type,
        sum(mab.order_fact_amount) * 1.0 / 10000  AS si
        FROM cdm_crm.member_analyse_base mab
        WHERE date(mab.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(mab.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_newold_type, member_level_type
    ) lyst
    ON matl.{zone} = lyst.{zone}
    AND matl.order_channel = lyst.order_channel
    AND matl.sales_mode = lyst.sales_mode
    AND matl.store_type = lyst.store_type
    AND matl.store_level = lyst.store_level
    AND matl.channel_type = lyst.channel_type
    AND matl.member_newold_type = lyst.member_newold_type
    AND matl.member_level_type = lyst.member_level_type
    
    WHERE matl.{zone} IN ({zones})
    AND matl.order_channel IN ({order_channels})
    AND matl.sales_mode IN ({sales_modes})
    AND matl.store_type IN ({store_types})
    AND matl.store_level IN ({store_levels})
    AND matl.channel_type IN ({channel_types})
"""