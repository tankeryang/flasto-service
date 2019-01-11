from query_service.query_biz.crm.const import ComparedType, MemberGroupingParamType


def sql_builder(column, condition):
    """
    构建 AND sql 语句
    :param column: payload.keys
    :param condition: payload.values
    :return: condition sql
    """
    if isinstance(condition, dict):
        compared_type = list(condition.keys())[0]
        param_type = MemberGroupingParamType.D[column]
        
        if compared_type == 'bt':
            return ComparedType.D[param_type][compared_type].format(
                column=column, condition_1=condition[compared_type][0], condition_2=condition[compared_type][1]
            )
        else:
            return ComparedType.D[param_type][compared_type].format(column=column, condition=condition)
    else:
        if isinstance(condition, list):
            return ComparedType.N.format(column=column, condition=str(condition).strip('[').strip(']'))
        else:
            return ComparedType.N.format(column=column, condition=str([condition]).strip('[').strip(']'))

def member_grouping_formator(sql, payload):
    """
    sql 填充
    :param sql:
    :param payload:
    :return:
    """
    if 'brand_code' not in payload.keys() or len(payload['brand_code']) == 0:
        return None
    
    brand_code = payload['brand_code']
    
    