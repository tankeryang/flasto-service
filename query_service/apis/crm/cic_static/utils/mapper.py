def mapper(sql, payload):
    """
    payload 参数校验
    query_sql 参数填充
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    brands = str(payload['brands']).strip('[').strip(']')
    
    return sql.format(brands=brands)
