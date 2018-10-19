from query_service.query_biz.crm.db_utils.validator import validator
import query_service.query_api.crm.entity.dto.report_center as dto


def daily_report_formator(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充后的sql字符串
    """
    
    # 校验参数
    necessary_param = dto.daily_report_dto.keys()
    
    if not validator(necessary_param, payload):
        return None
    else:
        if len(payload['store_codes']) > 0:
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'cmail.city'
            cmail_store_code = 'cmail.store_code'
            zone_index = 'sales_area, city, store_code'
            zone = 'store_code'
            zones = str(payload['store_codes']).strip('[').strip(']')
        elif len(payload['cities']) > 0:
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'cmail.city'
            cmail_store_code = 'NULL'
            zone_index = 'sales_area, city'
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif len(payload['sales_areas']) > 0 and payload['sales_areas'][0] != '全国':
            cmail_sales_area = 'cmail.sales_area'
            cmail_city = 'NULL'
            cmail_store_code = 'NULL'
            zone_index = 'sales_area'
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif len(payload['sales_areas']) > 0 and payload['sales_areas'][0] == '全国':
            cmail_sales_area = 'cmail.country'
            cmail_city = 'NULL'
            cmail_store_code = 'NULL'
            zone_index = 'country'
            zone = 'country'
            zones = str(['中国']).strip('[').strip(']')
        else:
            return None
        
        start_date = payload['start_date']
        end_date = payload['end_date']
        
        return sql.format(
            cmail_sales_area=cmail_sales_area, cmail_city=cmail_city, cmail_store_code=cmail_store_code,
            zone_index=zone_index, zone=zone, zones=zones, start_date=start_date, end_date=end_date
        )
