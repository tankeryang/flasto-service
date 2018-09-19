SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA = """
    WITH mab AS (
        SELECT DISTINCT
            maba.{zone},
            maba.order_channel,
            maba.brand_code,
            maba.store_code,
            maba.sales_mode,
            maba.store_type,
            maba.store_level,
            maba.channel_type,
            maba.outer_order_no,
            maba.member_no,
            maba.member_grade_id,
            maba.member_type,
            mabb.member_nowbefore_type,
            maba.order_item_quantity,
            maba.order_amount,
            maba.order_fact_amount,
            maba.member_register_time,
            maba.last_grade_change_time,
            maba.order_deal_time
        FROM cdm_crm.member_analyse_base maba
        LEFT JOIN (
            SELECT DISTINCT
                date(member_register_time) member_register_date,
                IF(
                    year(member_register_time) = year(date('{end_date}')),
                    IF(month(member_register_time) = month(date('{end_date}')), '当月会员', '当年会员'),
                    IF(year(member_register_time) < year(date('{end_date}')), '往年会员', NULL)
                ) member_nowbefore_type
            FROM cdm_crm.member_analyse_base
        ) mabb
        ON date(maba.member_register_time) = mabb.member_register_date
    )
    
    SELECT DISTINCT
        matl2.member_type AS member_type,
        cast(IF(sm2.si IS NOT NULL, sm2.si, 0) AS DECIMAL(10, 3))  AS sales_income,
        cast(IF(IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0) != 0, IF(sm2.si IS NOT NULL, sm2.si, 0) * 100.00 / IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0), 0) AS DECIMAL(10, 2)) AS sales_income_proportion,
        cast(IF(sm2.ca IS NOT NULL, sm2.ca, 0) AS INTEGER) AS customer_amount,
        cast(IF(sm2.oa IS NOT NULL, sm2.oa, 0) AS INTEGER) AS order_amount,
        cast(IF(IF(sm2.ca IS NOT NULL, sm2.ca, 0) != 0, IF(sm2.oa IS NOT NULL, sm2.oa, 0) / IF(sm2.ca IS NOT NULL, sm2.ca, 0), 0) AS INTEGER) AS consumption_frequency,
        cast(IF(IF(sm2.oa IS NOT NULL, sm2.oa, 0) != 0, IF(sm2.si IS NOT NULL, sm2.si, 0) * 10000.0 / IF(sm2.oa IS NOT NULL, sm2.oa, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_order,
        cast(IF(IF(sm2.siq IS NOT NULL, sm2.siq, 0) != 0, IF(sm2.si IS NOT NULL, sm2.si, 0) * 10000.0 / IF(sm2.siq IS NOT NULL, sm2.siq, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_item,
        cast(IF(IF(sm2.oa IS NOT NULL, sm2.oa, 0) != 0, IF(sm2.siq IS NOT NULL, sm2.siq, 0) / IF(sm2.oa IS NOT NULL, sm2.oa, 0), 0) AS INTEGER) AS sales_item_per_order
    FROM (
        SELECT DISTINCT
            {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
        FROM cdm_crm.member_analyse_type_label
    ) matl2
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
        sum(mab.order_fact_amount) * 1.0 / 10000                  AS si,
        IF(member_type = '会员', count(distinct member_no), NULL)  AS ca,
        count(distinct mab.outer_order_no)                        AS oa,
        sum(mab.order_item_quantity)                              AS siq
        FROM mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
    ) sm2
    ON matl2.{zone} = sm2.{zone}
    AND matl2.order_channel = sm2.order_channel
    AND matl2.sales_mode = sm2.sales_mode
    AND matl2.store_type = sm2.store_type
    AND matl2.store_level = sm2.store_level
    AND matl2.channel_type = sm2.channel_type
    AND matl2.member_type = sm2.member_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
        sum(mab.order_fact_amount) *1.0 / 10000 AS ttsi
        FROM mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ) smtt
    ON matl2.{zone} = smtt.{zone}
    AND matl2.order_channel = smtt.order_channel
    AND matl2.sales_mode = smtt.sales_mode
    AND matl2.store_type = smtt.store_type
    AND matl2.store_level = smtt.store_level
    AND matl2.channel_type = smtt.channel_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type,
        sum(mab.order_fact_amount) * 1.0 / 10000  AS si
        FROM mab
        WHERE date(mab.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(mab.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_type
    ) lyst2
    ON matl2.{zone} = lyst2.{zone}
    AND matl2.order_channel = lyst2.order_channel
    AND matl2.sales_mode = lyst2.sales_mode
    AND matl2.store_type = lyst2.store_type
    AND matl2.store_level = lyst2.store_level
    AND matl2.channel_type = lyst2.channel_type
    AND matl2.member_type = lyst2.member_type
    
    WHERE matl2.{zone} IN ({zones})
    AND matl2.order_channel IN ({order_channels})
    AND matl2.sales_mode IN ({sales_modes})
    AND matl2.store_type IN ({store_types})
    AND matl2.store_level IN ({store_levels})
    AND matl2.channel_type IN ({channel_types})
    AND matl2.member_type = '会员'
    
    UNION
    
    SELECT DISTINCT matl.member_nowbefore_type AS member_type,
    cast(IF(sm.si IS NOT NULL, sm.si, 0) AS DECIMAL(10, 3)) AS sales_income,
    cast(IF(IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 100.00 / IF(smtt.ttsi IS NOT NULL, smtt.ttsi, 0), 0) AS DECIMAL(10, 2)) AS sales_income_proportion,
    cast(IF(sm.ca IS NOT NULL, sm.ca, 0) AS INTEGER) AS customer_amount,
    cast(IF(sm.oa IS NOT NULL, sm.oa, 0) AS INTEGER) AS order_amount,
    cast(IF(IF(sm.ca IS NOT NULL, sm.ca, 0) != 0, IF(sm.oa IS NOT NULL, sm.oa, 0) / IF(sm.ca IS NOT NULL, sm.ca, 0), 0) AS INTEGER) AS consumption_frequency,
    cast(IF(IF(sm.oa IS NOT NULL, sm.oa, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 10000.0 / IF(sm.oa IS NOT NULL, sm.oa, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_order,
    cast(IF(IF(sm.siq IS NOT NULL, sm.siq, 0) != 0, IF(sm.si IS NOT NULL, sm.si, 0) * 10000.0 / IF(sm.siq IS NOT NULL, sm.siq, 0), 0) AS DECIMAL(10, 2)) AS sales_income_per_item,
    cast(IF(IF(sm.oa IS NOT NULL, sm.oa, 0) != 0, IF(sm.siq IS NOT NULL, sm.siq, 0) / IF(sm.oa IS NOT NULL, sm.oa, 0), 0) AS INTEGER) AS sales_item_per_order
    FROM (
        SELECT DISTINCT
        {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type
        FROM cdm_crm.member_analyse_type_label
    ) matl
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type,
        sum(mab.order_fact_amount) * 1.0 / 10000 AS si,
        count(distinct mab.member_no)            AS ca,
        count(distinct mab.outer_order_no)       AS oa,
        sum(mab.order_item_quantity)             AS siq
        FROM mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type
    ) sm
        ON matl.{zone} = sm.{zone}
        AND matl.order_channel = sm.order_channel
        AND matl.sales_mode = sm.sales_mode
        AND matl.store_type = sm.store_type
        AND matl.store_level = sm.store_level
        AND matl.channel_type = sm.channel_type
        AND matl.member_nowbefore_type = sm.member_nowbefore_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
        sum(mab.order_fact_amount) * 1.0 / 10000 AS ttsi
        FROM mab
        WHERE date(mab.order_deal_time) <= date('{end_date}')
        AND date(mab.order_deal_time) >= date('{start_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ) smtt
    ON matl.{zone} = smtt.{zone}
    AND matl.order_channel = smtt.order_channel
    AND matl.sales_mode = smtt.sales_mode
    AND matl.store_type = smtt.store_type
    AND matl.store_level = smtt.store_level
    AND matl.channel_type = smtt.channel_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type,
        sum(mab.order_fact_amount) * 1.0 / 10000  AS si
        FROM mab
        WHERE date(mab.order_deal_time) <= date(date('{end_date}') - interval '1' year)
        AND date(mab.order_deal_time) >= date(date('{start_date}') - interval '1' year)
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type, member_nowbefore_type
    ) lyst
    ON matl.{zone} = lyst.{zone}
    AND matl.order_channel = lyst.order_channel
    AND matl.sales_mode = lyst.sales_mode
    AND matl.store_type = lyst.store_type
    AND matl.store_level = lyst.store_level
    AND matl.channel_type = lyst.channel_type
    AND matl.member_nowbefore_type = lyst.member_nowbefore_type
    
    WHERE matl.{zone} IN ({zones})
    AND matl.order_channel IN ({order_channels})
    AND matl.sales_mode IN ({sales_modes})
    AND matl.store_type IN ({store_types})
    AND matl.store_level IN ({store_levels})
    AND matl.channel_type IN ({channel_types})
"""