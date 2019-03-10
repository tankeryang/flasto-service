def sql_builder(query_key, query_value):
    """
    构建 AND sql
    :param query_key:
    :param query_value:
    :return:
    """
    if query_key in ['coupon_batch_date', 'coupon_start_date', 'coupon_end_date', 'coupon_used_date']:
        return "AND {column} >= '{condition_from}' AND {column} <= '{condition_to}'\n".format(
            column=query_key, condition_from=query_value[0], condition_to=query_value[1]
        )
    if query_key == 'member_no_or_mobile':
        return "AND (member_no IN ({condition}) OR member_mobile IN ({condition}))\n".format(
            condition=str(query_value).strip('[').strip(']')
        )
    else:
        return "AND {column} IN ({condition})\n".format(
            column=query_key, condition=str(query_value).strip('[').strip(']')
        )


def member_coupon_order_mapper(sql, payload):
    """
    sql 填充
    :param sql:
    :param payload:
    :return:
    """
    condition_sql = ''
    for key in payload.keys():
        condition_sql += sql_builder(key, payload[key])
    
    return sql.format(condition_sql=condition_sql)


def coupon_denomination_sum_mapper(sql, payload):
    """
    sql 填充
    :param sql:
    :param payload:
    :return:
    """
    outer_order_no = str(payload['outer_order_no']).strip('[').strip(']')
    
    return sql.format(outer_order_no=outer_order_no)
