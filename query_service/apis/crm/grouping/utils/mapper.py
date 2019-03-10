from ..const import ComparedType, ParamType
from query_service.resources.apis.crm.grouping.query_sql import (
    MEMBER_INFO,
    COUPON_INFO,
    COUPON_INFO_WITH_AMOUNT,
    CML_CONSUMPTION_INFO,
    MEMBER_GROUPING_DETAIL,
    MEMBER_GROUPING_COUNT,
    COUNT_MEMBER_INFO,
    COUNT_COUPON_INFO,
    COUNT_COUPON_INFO_WITH_AMOUNT,
    COUNT_CML_CONSUMPTION_INFO,
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
        param_type = ParamType.D[column]
        
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


def mapper(payload):
    """
    sql 填充
    :param payload:
    :return:
    """
    sql_list = []
    sql_nick_name_list = []
    mi_condition_sql = ''  # 因为member_info的条件被拆分了, 所以需要单独进行拼接, 之后再format进sql
    join_sql = ''  # 查询会员明细的关联sql
    
    brand_code = payload.pop('brand_code')
    page = payload['page']
    
    for model in payload.keys():
        if model == 'member_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
        
        if model == 'grade_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
        
        if model == 'score_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
        
        if model == 'lst_consumption_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
        
        if model == 'fst_consumption_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
        
        if model == 'coupon_info_model':
            condition_sql = ''
            
            if 'coupon_amount' in payload[model].keys():
                coupon_condition_sql = sql_builder('coupon_amount', payload[model].pop('coupon_amount'))
                
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
                
                sql_nick_name_list.append('ciwa')
                sql_list.append(COUPON_INFO_WITH_AMOUNT.format(
                    brand_code=brand_code, condition_sql=condition_sql, coupon_condition_sql=coupon_condition_sql
                ))
            else:
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
                
                sql_nick_name_list.append('ci')
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
            
            sql_nick_name_list.append('cci')
            sql_list.append(CML_CONSUMPTION_INFO.format(
                brand_code=brand_code,
                start_date=start_date,
                end_date=end_date,
                condition_sql_cml_consumption_store=condition_sql_cml_consumption_store,
                condition_sql=condition_sql
            ))
    
    if mi_condition_sql:
        sql_nick_name_list.append('mi')
        sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=mi_condition_sql))
    
    with_sql = ', '.join(sql_list)
    for nick_name in sql_nick_name_list:
        join_sql += 'INNER JOIN {nick_name} ON mid.member_no = {nick_name}.member_no\n'.format(nick_name=nick_name)
    end = page * 10
    start = end - 9
    
    sql = MEMBER_GROUPING_DETAIL.format(
        brand_code=brand_code,
        with_sql=with_sql,
        join_sql=join_sql,
        start=start,
        end=end
    )
    
    return sql


def count_mapper(payload):
    """
    sql 填充
    :param payload:
    :return:
    """
    sql_list = []
    sql_nick_name_list = []
    mi_condition_sql = ''  # 因为member_info的条件被拆分了, 所以需要单独进行拼接, 之后再format进sql
    join_sql = ''  # 查询会员明细的关联sql

    brand_code = payload.pop('brand_code')

    for model in payload.keys():
        if model == 'member_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
    
        if model == 'grade_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
    
        if model == 'score_info_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
    
        if model == 'lst_consumption_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
    
        if model == 'fst_consumption_model':
            for column in payload[model].keys():
                mi_condition_sql += sql_builder(column, payload[model][column])
    
        if model == 'coupon_info_model':
            condition_sql = ''
        
            if 'coupon_amount' in payload[model].keys():
                coupon_condition_sql = sql_builder('coupon_amount', payload[model].pop('coupon_amount'))
            
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
            
                sql_nick_name_list.append('ciwa')
                sql_list.append(COUPON_INFO_WITH_AMOUNT.format(
                    brand_code=brand_code, condition_sql=condition_sql, coupon_condition_sql=coupon_condition_sql
                ))
            else:
                for column in payload[model].keys():
                    condition_sql += sql_builder(column, payload[model][column])
            
                sql_nick_name_list.append('ci')
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
        
            sql_nick_name_list.append('cci')
            sql_list.append(CML_CONSUMPTION_INFO.format(
                brand_code=brand_code,
                start_date=start_date,
                end_date=end_date,
                condition_sql_cml_consumption_store=condition_sql_cml_consumption_store,
                condition_sql=condition_sql
            ))

    if mi_condition_sql:
        sql_nick_name_list.append('mi')
        sql_list.append(MEMBER_INFO.format(brand_code=brand_code, condition_sql=mi_condition_sql))

    with_sql = ', '.join(sql_list)
    for nick_name in sql_nick_name_list:
        join_sql += 'INNER JOIN {nick_name} ON mid.member_no = {nick_name}.member_no\n'.format(nick_name=nick_name)


    sql = MEMBER_GROUPING_COUNT.format(
        brand_code=brand_code,
        with_sql=with_sql,
        join_sql=join_sql
    )

    return sql
