class MemberType:
    """member_type 常量"""
    TOTAL = 'total'
    NOW_BEFORE = 'now_before'
    NEW_OLD = 'new_old'
    LEVEL = 'level'
    MUL_DIM = 'mul_dim'


class DurationType:
    """Duration Type 常量"""
    YEARLY = str(['yearly']).strip('[').strip(']')
    MONTHLY = str(['monthly']).strip('[').strip(']')
    WEEKLY = str(['weekly']).strip('[').strip(']')
    DAILY = str(['daily']).strip('[').strip(']')


class QueryType:
    """query type 常量"""
    ALL = 'all'
    DETAIL = 'detail'


class QueryField:
    """查询范围常量"""
    ALL = '全部'
    ORDER_CHANNELS = {'', '线上', '线下'}
    SALES_MODES = {'', '正价', '长特', '短特'}
    STORE_TYPES = {'', 'MALL', '百货', '专卖店'}
    STORE_LEVELS = {'', 'I', 'A', 'B', 'C', 'D'}
    CHANNEL_TYPES = {'', '自营', '联营', '特许'}
