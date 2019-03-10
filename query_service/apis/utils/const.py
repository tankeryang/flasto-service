class QueryField:
    """查询范围常量"""
    ALL = '全部'
    ORDER_CHANNELS = {'', '线上', '线下'}
    TRADE_SOURCE = {'', 'FPOS', 'IPOS', 'OMIS', '官网', '其他'}
    SALES_MODES = {'', '正价', '长特', '短特'}
    STORE_TYPES = {'', 'MALL', '百货', '专卖店'}
    STORE_LEVELS = {'', 'I', 'A', 'B', 'C', 'D'}
    CHANNEL_TYPES = {'', '自营', '联营', '特许'}
