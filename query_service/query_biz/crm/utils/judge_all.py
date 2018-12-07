from query_service.query_biz.crm.const import QueryField


def judge_all(query_param, query_field):
    """
    解析 '全部' 参数
    :param query_param:
    :param query_field:
    :return:
    """
    if query_param == QueryField.ALL:
        return str(list(query_field)).strip('[').strip(']')
    else:
        return str([query_param]).strip('[').strip(']')