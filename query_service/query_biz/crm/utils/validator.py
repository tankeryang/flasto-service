def validator(ns_param, payload):
    """
    api 参数校验
    :param payload: restplus.Api.payload
    :param ns_param: dict necessary param
    :return: boolean
    """

    param = set(payload.keys())
    ns_param = set(ns_param)
    
    if len(ns_param) != len(param) \
            or len(ns_param.difference(param)) != 0 \
            or len(param.difference(ns_param)) != 0:
        return False
    else:
        return True
