def dr_mapper(sql, payload):
    """
    日报 sql mapper
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充后的sql字符串
    """
    if 'company_names' in payload.keys() and len(payload['company_names']) > 0:
        cmail_sales_area = 'NULL'
        cmail_city = 'NULL'
        cmail_company_name = 'cmail.company_name'
        cmail_store_code = 'NULL'
        zone_index = 'company_name'
        zone = 'company_name'
        zones = str(payload['company_names']).strip('[').strip(']')
    else:
        if 'store_codes' in payload.keys() and len(payload['store_codes']) > 0:
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'cmail.city'
            cmail_company_name = 'cmail.company_name'
            cmail_store_code = 'cmail.store_code'
            zone_index = 'sales_area, city, company_name, store_code'
            zone = 'store_code'
            zones = str(payload['store_codes']).strip('[').strip(']')
        elif 'cities' in payload.keys() and len(payload['cities']) > 0:
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'cmail.city'
            cmail_company_name = 'NULL'
            cmail_store_code = 'NULL'
            zone_index = 'sales_area, city'
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif 'sales_areas' in payload.keys() and len(payload['sales_areas']) > 0 and payload['sales_areas'][0] != '全国':
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'NULL'
            cmail_company_name = 'NULL'
            cmail_store_code = 'NULL'
            zone_index = 'sales_area'
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif 'sales_areas' in payload.keys() and len(payload['sales_areas']) > 0 and payload['sales_areas'][0] == '全国':
            cmail_sales_area = 'cmail.country'
            cmail_city = 'NULL'
            cmail_company_name = 'NULL'
            cmail_store_code = 'NULL'
            zone_index = 'country'
            zone = 'country'
            zones = str(['中国']).strip('[').strip(']')
        else:
            return None
    
    brand_code = payload['brand_code']
    channel_type = payload['channel_type']
    start_date = payload['start_date']
    end_date = payload['end_date']
    
    return sql.format(
        brand_code=brand_code,
        channel_type=channel_type,
        cmail_sales_area=cmail_sales_area,
        cmail_city=cmail_city,
        cmail_company_name=cmail_company_name,
        cmail_store_code=cmail_store_code,
        zone_index=zone_index, zone=zone, zones=zones,
        start_date=start_date, end_date=end_date
    )


def mr_sales_mapper(sql, payload):
    """
    月报 sql mapper
    :param sql:
    :param payload:
    :return:
    """
    brand_codes = str(payload['brand_code']).strip('[').strip(']')
    channel_types = str(payload['channel_type']).strip('[').strip(']')
    mr_member_types = str(payload['member_type']).strip('[').strip(']')
    kpis = str(payload['kpi']).strip('[').strip(']')
    year_month = payload['report_time']

    return sql.format(
        brand_codes=brand_codes,
        channel_types=channel_types,
        mr_member_types=mr_member_types,
        kpis=kpis,
        year_month=year_month
    )
