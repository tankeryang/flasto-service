def format_sql(sql, payload):
    
    if len(payload['cities']) > 0:
        zone = 'city'
        zones = str(payload['cities']).strip('[').strip(']')
    elif len(payload['provinces']) > 0:
        zone = 'province'
        zones = str(payload['provinces']).strip('[').strip(']')
    elif len(payload['sales_areas']) > 0:
        zone = 'sales_area'
        zones = str(payload['sales_areas']).strip('[').strip(']')
    elif len(payload['country']) == 1 and payload['country'].__getitem__(0) == '全国':
        zone = 'country'
        zones = str(['中国']).strip('[').strip(']')
    else:
        return None
    
    order_channels = str(payload['order_channels']).strip('[').strip(']')
    sales_modes = str(payload['sales_modes']).strip('[').strip(']')
    store_types = str(payload['store_types']).strip('[').strip(']')
    store_levels = str(payload['store_levels']).strip('[').strip(']')
    channel_types = str(payload['channel_types']).strip('[').strip(']')
    start_date = payload['start_date']
    end_date = payload['end_date']
    
    return sql.format(
        zone=zone, zones=zones, start_date=start_date, end_date=end_date,
        order_channels=order_channels, sales_modes=sales_modes, store_types=store_types,
        store_levels=store_levels, channel_types=channel_types
    )