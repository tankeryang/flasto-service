def member_coupon_order_formator(sql, payload):
    """
    sql 填充
    :param sql:
    :param payload:
    :return:
    """
    condition_sql = ''
    for key in payload.keys():
        condition_sql += "\tAND {key} IN ({values})\n".format(key=key, values=str(payload[key]).strip('[').strip(']'))
    
    return sql.format(condition_sql=condition_sql)
