from query_service.query_biz.crm.const import QueryField
from query_service.query_biz.crm.utils.judge_all import judge_all


def recruit_analyse_formator(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """

    # 区域查询
    if 'store_codes' not in payload.keys():
        if 'brands' not in payload.keys() or len(payload['brands']) < 1:
            return None
        elif 'cities' in payload.keys() and len(payload['cities']) > 0:
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif 'provinces' in payload.keys() and len(payload['provinces']) > 0:
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
        order_channels = judge_all(payload['order_channels'], QueryField.ORDER_CHANNELS)
        sales_modes = judge_all(payload['sales_modes'], QueryField.SALES_MODES)
        store_types = judge_all(payload['store_types'], QueryField.STORE_TYPES)
        store_levels = judge_all(payload['store_levels'], QueryField.STORE_LEVELS)
        channel_types = judge_all(payload['channel_types'], QueryField.CHANNEL_TYPES)
        start_date = payload['start_date']
        end_date = payload['end_date']
    
        return sql.format(
            brands=brands, zone=zone, zones=zones,
            order_channels=order_channels, sales_modes=sales_modes,
            store_types=store_types, store_levels=store_levels, channel_types=channel_types,
            start_date=start_date, end_date=end_date
        )

    # 门店查询
    elif 'store_codes' in payload.keys():
        if 'brands' not in payload.keys() or len(payload['brands']) < 1:
            return None
    
        zone = 'store_code'
        zones = str(payload['store_codes']).strip('[').strip(']')
        brands = str(payload['brands']).strip('[').strip(']')
        order_channels = judge_all(payload['order_channels'], QueryField.ORDER_CHANNELS)
        start_date = payload['start_date']
        end_date = payload['end_date']
    
        return sql.format(
            brands=brands, zone=zone, zones=zones,
            order_channels=order_channels, start_date=start_date, end_date=end_date
        )
