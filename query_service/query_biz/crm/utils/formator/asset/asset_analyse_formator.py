def asset_analyse_formator(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    if 'store_codes' not in payload.keys():
        
        if 'brands' not in payload.keys() or len(payload['brands']) < 1:
            return None
        elif 'cities' in payload.keys() and len(payload['cities']) > 0:
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif 'province' in payload.keys() and (payload['provinces']) > 0:
            zone = 'province'
            zones = str(payload['provinces']).strip('[').strip(']')
        elif 'sales_areas' in payload.keys() and len(payload['sales_areas']) > 0:
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif 'sales_districts' in payload.keys() and len(payload['sales_districts']) > 0:
            zone = 'sales_district'
            zones = str(payload['sales_district']).strip('[').strip(']')
        elif 'country' in payload.keys() and len(payload['country']) > 0:
            zone = 'country'
            zones = str(payload['country']).strip('[').strip(']')
        else:
            return None
        
        brands = str(payload['brands']).strip('[').strip(']')
        order_channels = str(payload['order_channels']).strip('[').strip(']')
        sales_modes = str(payload['sales_modes']).strip('[').strip(']')
        store_types = str(payload['store_types']).strip('[').strip(']')
        store_levels = str(payload['store_levels']).strip('[').strip(']')
        channel_types = str(payload['channel_types']).strip('[').strip(']')
        end_date = payload['end_date']
        
        return sql.format(
            brands=brands, zone=zone, zones=zones, end_date=end_date,
            order_channels=order_channels, sales_modes=sales_modes, store_types=store_types,
            store_levels=store_levels, channel_types=channel_types
        )
    
    else:
        
        if len(payload['brands']) < 1:
            return None
        elif len(payload['store_codes']) > 0:
            zones = str(payload['store_codes']).strip('[').strip(']')
        else:
            return None
        
        brands = str(payload['brands']).strip('[').strip(']')
        order_channels = str(payload['order_channels']).strip('[').strip(']')
        end_date = payload['end_date']
        
        return sql.format(
            brands=brands, zones=zones, order_channels=order_channels, end_date=end_date
        )
