from .valid_req_dto import valid_req_dto
import query_service.query_api.crm.entity.dto as dto


def crm_member_income_analyse_format_sql(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    # 校验参数
    necessary_param = dto.crm_member_analyse_req_dto_model.keys()
    
    if not valid_req_dto(necessary_param, payload):
        return None
    else:
        if len(payload['store_codes']) > 0:
            zone = 'store_code'
            zones = str(payload['store_codes']).strip('[').strip(']')
        elif len(payload['cities']) > 0:
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif len(payload['provinces']) > 0:
            zone = 'province'
            zones = str(payload['provinces']).strip('[').strip(']')
        elif len(payload['sales_areas']) > 0:
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif len(payload['sales_districts']) > 0:
            zone = 'sales_district'
            zones = str(payload['sales_district']).strip('[').strip(']')
        elif len(payload['country']) > 0:
            zone = 'country'
            zones = str(payload['country']).strip('[').strip(']')
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


def crm_daily_report_format_sql(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充后的sql字符串
    """
    
    # 校验参数
    necessary_param = dto.crm_daily_report_req_dto_model.keys()
    
    if not valid_req_dto(necessary_param, payload):
        return None
    elif len(payload['start_date']) == 0 or len(payload['end_date']) == 0:
        return None
    else:
        if len(payload['store_codes']) > 0:
            mtl_sales_area = 'mtl.sales_area'
            mtl_city = 'mtl.city'
            mtl_store_code = 'mtl.store_code'
            zone_index = 'sales_area, city, store_code'
            zone = 'store_code'
            zones = str(payload['store_codes']).strip('[').strip(']')
        elif len(payload['cities']) > 0:
            mtl_sales_area = 'mtl.sales_area'
            mtl_city = 'mtl.city'
            mtl_store_code = 'NULL'
            zone_index = 'sales_area, city'
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif len(payload['sales_areas']) > 0 and payload['sales_areas'][0] != '全国':
            mtl_sales_area = 'mtl.sales_area'
            mtl_city = 'NULL'
            mtl_store_code = 'NULL'
            zone_index = 'sales_area'
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif len(payload['sales_areas']) > 0 and payload['sales_areas'][0] == '全国':
            mtl_sales_area = 'mtl.country'
            mtl_city = 'NULL'
            mtl_store_code = 'NULL'
            zone_index = 'country'
            zone = 'country'
            zones = str(['中国']).strip('[').strip(']')
        else:
            return None
        
        start_date = payload['start_date']
        end_date = payload['end_date']
        
        return sql.format(
            mtl_sales_area=mtl_sales_area, mtl_city=mtl_city, mtl_store_code=mtl_store_code,
            zone_index=zone_index, zone=zone, zones=zones, start_date=start_date, end_date=end_date
        )
