from query_service.apis.utils.const import QueryField


def judge_all(query_param, query_field):
    """
    解析 '全部' 参数
    :param query_param:
    :param query_field:
    :return:
    """
    if QueryField.ALL in query_param:
        return str(list(query_field)).strip('[').strip(']')
    else:
        return str(query_param).strip('[').strip(']')