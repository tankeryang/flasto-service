def valid_crm_member_income_analyse_dto(payload):
    """
    crm 业绩分析 api 参数校验
    :param payload: restplus.Api.payload
    :return: boolean
    """
    necessary_param = {
        'sales_modes', 'store_types', 'store_levels', 'channel_types', 'order_channels',
        'country', 'sales_areas', 'sales_districts', 'provinces', 'cities',
        'start_date', 'end_date'
    }
    param = set(payload.keys())
    
    if len(necessary_param) != len(param) \
            or len(necessary_param.difference(param)) != 0 \
            or len(param.difference(necessary_param)) != 0:
        return False
    else:
        return True
