from query_service.query_biz.crm.db_utils.validator import validator
import query_service.query_api.crm.entity.dto.cic_static as dto


def cic_static_formator(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    necessary_param = dto.cic_static_dto.keys()
    if not validator(necessary_param, payload):
        return None
    
    if len(payload['brands']) < 1:
        return None
    
    brands = str(payload['brands']).strip('[').strip(']')
    
    return sql.format(brands=brands)
