def cic_static_formator(sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    if 'brands' not in payload.keys() or len(payload['brands']) < 1:
        return None
    
    brands = str(payload['brands']).strip('[').strip(']')
    
    return sql.format(brands=brands)
