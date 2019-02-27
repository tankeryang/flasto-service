from query_service.query_biz.crm.const import ComparedType, MemberGroupingParamType
from query_service.resources.crm.query_sql.grouping import (
    MEMBER_INFO,
    COUPON_INFO,
    COUPON_INFO_WITH_AMOUNT,
    CML_CONSUMPTION_INFO,
)


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
            return ComparedType.D[param_type][compared_type].format(column=column, condition=condition[compared_type])
    else:
        if isinstance(condition, list):
            return ComparedType.N.format(column=column, condition=str(condition).strip('[').strip(']'))
        else:
            return ComparedType.N.format(column=column, condition=str([condition]).strip('[').strip(']'))


def member_grouping_formator(payload):
    """
    sql 填充
    :param payload:
    :return:
    """
    sql_list = []
    if 'brand_code' not in payload.keys() or len(payload['brand_code']) == 0:
        return None
    
    brand_code = payload.pop('brand_code')
    
    for model in payload.keys():
        if model == 'member_info_model':
            condition_sql = ''
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=condition_sql))
        
        if model == 'grade_info_model':
            condition_sql = ''
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=condition_sql))
        
        if model == 'score_info_model':
            condition_sql = ''
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=condition_sql))
        
        if model == 'lst_consumption_model':
            condition_sql = ''
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=condition_sql))

        if model == 'fst_consumption_model':
            condition_sql = ''
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=condition_sql))
        
        if model == 'coupon_info_model':
            condition_sql = ''
            if 'coupon_amount' in payload[model].keys():
                coupon_condition_sql = sql_builder('coupon_amount', payload[model].pop('coupon_amount'))
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
                sql_list.append(COUPON_INFO_WITH_AMOUNT.format(
                    brand_code=brand_code, condition_sql=condition_sql, coupon_condition_sql=coupon_condition_sql
                ))
            else:
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
                sql_list.append(COUPON_INFO.format(brand_code=brand_code, condition_sql=condition_sql))
        
        if model == 'cml_consumption_model':
            condition_sql = ''
            condition_sql_cml_consumption_store = ''

            cml_consumption_date = payload[model].pop('cml_consumption_date')['bt']
            start_date = cml_consumption_date[0]
            end_date = cml_consumption_date[1]
            
            if 'cml_consumption_store' in payload[model].keys():
                condition_sql_cml_consumption_store = "AND cml_consumption_store IN ({cml_consumption_stores})".format(
                    cml_consumption_stores=str(payload[model].pop('cml_consumption_store')).strip('[').strip(']'))
            for column in payload[model].keys():
                condition_sql += sql_builder(column, payload[model][column])
            sql_list.append(CML_CONSUMPTION_INFO.format(
                brand_code=brand_code, start_date=start_date, end_date=end_date,
                condition_sql_cml_consumption_store=condition_sql_cml_consumption_store, condition_sql=condition_sql
            ))
    
    return sql_list
