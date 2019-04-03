class ComparedType:
    """比较常量"""
    D = {
        'n': {
            'lt': 'AND {column} < {condition}\n',
            'gt': 'AND {column} > {condition}\n',
            'eq': 'AND {column} = {condition}\n',
            'bt': 'AND {column} >= {condition_1} AND {column} <= {condition_2}\n'
        },
        's': {
            'lt': "AND {column} < '{condition}'\n",
            'gt': "AND {column} > '{condition}'\n",
            'eq': "AND {column} = '{condition}'\n",
            'bt': "AND {column} >= '{condition_1}' AND {column} <= '{condition_2}'\n"
        },
        'd': {
            'lt': "AND {column} < DATE('{condition}')\n",
            'gt': "AND {column} > DATE('{condition}')\n",
            'eq': "AND {column} = DATE('{condition}')\n",
            'bt': "AND {column} >= DATE('{condition_1}') AND {column} <= DATE('{condition_2}')\n"
        }
    }
    N = "AND {column} IN ({condition})"


class ParamType:
    """会员分组参数常量标识 (n:数字/s:字符)"""
    D = {
        'member_birthday': 's',
        'member_birthday_month': 'n',
        'member_gender': 's',
        'member_age': 'n',
        'member_status': 'n',
        'member_register_date': 'd',
        'member_manage_store': 's',
        'member_register_store': 'd',
        'member_reg_source': 's',
        'member_is_batch_mobile': 'n',
        'member_is_batch_weixin': 'n',
        'member_is_batch_taobao': 'n',
        'member_grade_id': 'n',
        'member_grade_expiration_date': 'd',
        'member_score': 'n',
        'member_will_score': 'n',
        'lst_consumption_date': 'd',
        'lst_consumption_gap': 'n',
        'lst_consumption_store': 's',
        'lst_consumption_item_quantity': 'n',
        'lst_consumption_amount': 'n',
        'lst_consumption_amount_include_coupon': 'n',
        'fst_consumption_date': 'd',
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


class CSV:
    """导出csv参数"""
    COLUMNS = [
        '经营方式',
        '区域',
        '城市',
        '管理门店',
        '管理导购',
        '会员状态',
        '会员编号',
        '会员编码',
        '会员卡号',
        '会员手机号',
        '会员姓名',
        '会员性别',
        '会员等级',
        '等级到期时间',
        '到账积分',
        '未到账积分',
        '微信ID',
        '会员生日',
        '入会日期',
        '最近消费日期',
        '最近回访日期',
        '注册来源'
    ]
    
    FILE_NAME = 'member_grouping_detail_'
