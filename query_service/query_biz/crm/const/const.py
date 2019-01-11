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
    TRADE_SOURCE = {'', 'FPOS', 'IPOS', 'OMIS', '官网', '其他'}
    SALES_MODES = {'', '正价', '长特', '短特'}
    STORE_TYPES = {'', 'MALL', '百货', '专卖店'}
    STORE_LEVELS = {'', 'I', 'A', 'B', 'C', 'D'}
    CHANNEL_TYPES = {'', '自营', '联营', '特许'}


class ComparedType:
    """比较常量"""
    D = {
        'n': {
            'lt': 'AND {column} < {condition}',
            'gt': 'AND {column} > {condition}',
            'eq': 'AND {column} = {condition}',
            'bt': 'AND {column} > {condition_1} AND {column} < {condition_2}'
        },
        's': {
            'lt': "AND '{column}' < '{condition}'",
            'gt': "AND '{column}' > '{condition}'",
            'eq': "AND '{column}' = '{condition}'",
            'bt': "AND '{column}' > '{condition_1}' AND '{column}' < '{condition_2}'"
        }
    }
    N = "AND {column} IN ({condition})"


class MemberGroupingParamType:
    """会员分组参数常量标识 (n:数字/s:字符)"""
    D = {
        'member_birthday': 's',
        'member_birthday_month': 'n',
        'member_gender': 's',
        'member_age': 'n',
        'member_status': 'n',
        'member_register_date': 's',
        'member_manage_store': 's',
        'member_register_store': 's',
        'member_reg_source': 's',
        'member_is_batch_mobile': 'n',
        'member_is_batch_weixin': 'n',
        'member_is_batch_taobao': 'n',
        'member_grade_id': 'n',
        'member_grade_expiration_date': 's',
        'member_score': 'n',
        'member_will_score': 'n',
        'lst_consumption_date': 's',
        'lst_consumption_gap': 'n',
        'lst_consumption_store': 's',
        'lst_consumption_item_quantity': 'n',
        'lst_consumption_amount': 'n',
        'lst_consumption_amount_include_coupon': 'n',
        'fst_consumption_date': 's',
        'fst_consumption_gap': 'n',
        'fst_consumption_store': 's',
        'fst_consumption_item_quantity': 'n',
        'fst_consumption_amount': 'n',
        'fst_consumption_amount_include_coupon': 'n',
        'coupon_amount': 'n',
        'coupon_template_no': 's',
        'coupon_status': 's',
        'coupon_category': 's',
        'coupon_discount': 'n',
        'coupon_denomination': 'n',
        'coupon_type_detail': 's',
        'coupon_batch_date': 's',
        'coupon_start_date': 's',
        'coupon_end_date': 's',
        'cml_consumption_store': 's',
        'cml_consumption_times': 'n',
        'cml_consumption_item_quantity': 'n',
        'cml_consumption_days': 'n',
        'cml_consumption_months': 'n',
        'cml_consumption_amount': 'n',
        'cml_consumption_amount_include_coupon': 'n',
        'cml_return_times': 'n',
        'cml_return_amount': 'n',
        'cml_avg_discount': 'n',
        'cml_avg_discount_include_coupon': 'n',
        'cml_avg_sales_amount_per_order': 'n',
        'cml_avg_sales_item_per_order': 'n',
        'cml_avg_sales_amount_per_item': 'n'
    }