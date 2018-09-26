SQL_CRM_MEMBER_AMOUNT_DETAIL_DATA = """
    SELECT DISTINCT
        cast(COALESCE(SUM(mrac.ma), 0) AS INTEGER) AS member_register_cumulative_amount,
        cast(COALESCE(SUM(mcac.ma), 0) AS INTEGER) AS member_consumed_cumulative_amount,
        cast(COALESCE(SUM(mrac.ma - mcac.ma), 0) AS INTEGER) AS member_unconsumed_cumulative_amount
    FROM (
        SELECT DISTINCT
            {zone}, order_channel, sales_mode, store_type, store_level, channel_type
        FROM cdm_crm.member_analyse_type_label
    ) matl
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
        COALESCE(SUM(mra.member_amount), 0) AS ma
        FROM cdm_crm.member_register_amount mra
        WHERE mra.date < date('{end_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ) mrac
    ON matl.{zone} = mrac.{zone}
    AND matl.order_channel = mrac.order_channel
    AND matl.sales_mode = mrac.sales_mode
    AND matl.store_type = mrac.store_type
    AND matl.store_level = mrac.store_level
    AND matl.channel_type = mrac.channel_type
    
    LEFT JOIN (
        SELECT {zone}, order_channel, sales_mode, store_type, store_level, channel_type,
        count(distinct mab.member_no) AS ma
        FROM cdm_crm.member_analyse_base mab
        WHERE date(mab.order_deal_time) < date('{end_date}')
        GROUP BY {zone}, order_channel, sales_mode, store_type, store_level, channel_type
    ) mcac
    ON matl.{zone} = mcac.{zone}
    AND matl.order_channel = mcac.order_channel
    AND matl.sales_mode = mcac.sales_mode
    AND matl.store_type = mcac.store_type
    AND matl.store_level = mcac.store_level
    AND matl.channel_type = mcac.channel_type
    
    WHERE matl.{zone} IN ({zones})
    AND matl.order_channel IN ({order_channels})
    AND matl.sales_mode IN ({sales_modes})
    AND matl.store_type IN ({store_types})
    AND matl.store_level IN ({store_levels})
    AND matl.channel_type IN ({channel_types})
"""