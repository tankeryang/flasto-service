import time
from datetime import datetime, timedelta

from query_service.query_biz.crm.const import DurationType
from query_service.query_biz.crm.const import QueryField
from query_service.query_biz.crm.utils.judge_all import judge_all


def income_analyse_formator(sql, static_sql, payload):
    """
    payload 参数校验
    sql 参数填充
    :param static_sql: 静态查询sql
    :param sql: sql字符串
    :param payload: restplus.Api.payload 传入参数
    :return: 填充参数后的sql
    """
    
    if 'store_codes' not in payload.keys():
        
        if 'brands' not in payload.keys() or len(payload['brands']) < 1:
            return None
        elif 'cities' in payload.keys() and len(payload['cities']) > 0:
            zone = 'city'
            zones = str(payload['cities']).strip('[').strip(']')
        elif 'provinces' in payload.keys() and len(payload['provinces']) > 0:
            zone = 'province'
            zones = str(payload['provinces']).strip('[').strip(']')
        elif 'sales_areas' in payload.keys() and len(payload['sales_areas']) > 0:
            zone = 'sales_area'
            zones = str(payload['sales_areas']).strip('[').strip(']')
        elif 'sales_districts' in payload.keys() and len(payload['sales_districts']) > 0:
            zone = 'sales_district'
            zones = str(payload['sales_district']).strip('[').strip(']')
        elif 'country' in payload.keys() and len(payload['country']) > 0:
            zone = 'country'
            zones = str(payload['country']).strip('[').strip(']')
        else:
            return None

        brands = str(payload['brands']).strip('[').strip(']')
        order_channels = str([payload['order_channels']]).strip('[').strip(']')
        sales_modes = str([payload['sales_modes']]).strip('[').strip(']')
        store_types = str([payload['store_types']]).strip('[').strip(']')
        store_levels = str([payload['store_levels']]).strip('[').strip(']')
        channel_types = str([payload['channel_types']]).strip('[').strip(']')
        start_date = payload['start_date']
        end_date = payload['end_date']
        
        # 判断是否查询静态数据
        end_date_datetime = datetime.strptime(payload['end_date'], '%Y-%m-%d')
        # 年
        if payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                and payload['start_date'] == time.strftime('%Y-01-01', time.localtime()):
            return static_sql.format(
                brands=brands, zone=zone, zones=zones, duration_type=DurationType.YEARLY,
                order_channels=order_channels, sales_modes=sales_modes,
                store_types=store_types, store_levels=store_levels, channel_types=channel_types,
                start_date=start_date, end_date=end_date
            )
        # 月
        elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                and payload['start_date'] == time.strftime('%Y-%m-01', time.localtime()):
            return static_sql.format(
                brands=brands, zone=zone, zones=zones, duration_type=DurationType.MONTHLY,
                order_channels=order_channels, sales_modes=sales_modes,
                store_types=store_types, store_levels=store_levels, channel_types=channel_types,
                start_date=start_date, end_date=end_date
            )
        # 周
        elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                and payload['start_date'] == (end_date_datetime - timedelta(days=end_date_datetime.weekday())).strftime('%Y-%m-%d'):
            return static_sql.format(
                brands=brands, zone=zone, zones=zones, duration_type=DurationType.WEEKLY,
                order_channels=order_channels, sales_modes=sales_modes,
                store_types=store_types, store_levels=store_levels, channel_types=channel_types,
                start_date=start_date, end_date=end_date
            )
        # 日
        elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                and payload['start_date'] == time.strftime('%Y-%m-%d', time.localtime()):
            return static_sql.format(
                brands=brands, zone=zone, zones=zones, duration_type=DurationType.DAILY,
                order_channels=order_channels, sales_modes=sales_modes,
                store_types=store_types, store_levels=store_levels, channel_types=channel_types,
                start_date=start_date, end_date=end_date
            )
        # 动态查询
        else:
            order_channels = judge_all(payload['order_channels'], QueryField.ORDER_CHANNELS)
            sales_modes = judge_all(payload['sales_modes'], QueryField.SALES_MODES)
            store_types = judge_all(payload['store_types'], QueryField.STORE_TYPES)
            store_levels = judge_all(payload['store_levels'], QueryField.STORE_LEVELS)
            channel_types = judge_all(payload['channel_types'], QueryField.CHANNEL_TYPES)
        
            return sql.format(
                brands=brands, zone=zone, zones=zones,
                order_channels=order_channels, sales_modes=sales_modes,
                store_types=store_types, store_levels=store_levels, channel_types=channel_types,
                start_date=start_date, end_date=end_date,
            )

    # 门店查询
    else:
        zone = 'store_code'
        # 如果只有一个门店编码，可以进行判断是否查询静态数据
        if 'store_codes' in payload.keys() and len(payload['store_codes']) == 1:
            zones = str(payload['store_codes']).strip('[').strip(']')
            
            if 'brands' not in payload.keys() or len(payload['brands']) < 1:
                return None
        
            brands = str(payload['brands']).strip('[').strip(']')
            order_channels = str([payload['order_channels']]).strip('[').strip(']')
        
            # 判断是否查询静态数据
            end_date = datetime.strptime(payload['end_date'], '%Y-%m-%d')
            # 年
            if payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                    and payload['start_date'] == time.strftime('%Y-01-01', time.localtime()):
                return static_sql.format(
                    brands=brands, zone=zone, zones=zones,
                    order_channels=order_channels, duration_type=DurationType.YEARLY
                )
            # 月
            elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                    and payload['start_date'] == time.strftime('%Y-%m-01', time.localtime()):
                return static_sql.format(
                    brands=brands, zone=zone, zones=zones,
                    order_channels=order_channels, duration_type=DurationType.MONTHLY
                )
            # 周
            elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                    and payload['start_date'] == (end_date - timedelta(days=end_date.weekday())).strftime('%Y-%m-%d'):
                return static_sql.format(
                    brands=brands, zone=zone, zones=zones,
                    order_channels=order_channels, duration_type=DurationType.WEEKLY
                )
            # 日
            elif payload['end_date'] == time.strftime('%Y-%m-%d', time.localtime()) \
                    and payload['start_date'] == time.strftime('%Y-%m-%d', time.localtime()):
                return static_sql.format(
                    brands=brands, zone=zone, zones=zones,
                    order_channels=order_channels, duration_type=DurationType.DAILY
                )
            # 动态查询
            else:
                order_channels = judge_all(payload['order_channels'], QueryField.ORDER_CHANNELS)
                start_date = payload['start_date']
                end_date = payload['end_date']
                return sql.format(
                    brands=brands, zone=zone, zones=zones,
                    order_channels=order_channels, start_date=start_date, end_date=end_date
                )
                
        # 否则直接动态查询
        elif 'store_codes' in payload.keys() and len(payload['store_codes']) > 1:
            if 'brands' not in payload.keys() or len(payload['brands']) < 1:
                return None
            elif 'store_codes' in payload.keys() and len(payload['store_codes']) > 0:
                zones = str(payload['store_codes']).strip('[').strip(']')
            else:
                return None
        
            brands = str(payload['brands']).strip('[').strip(']')
            order_channels = judge_all(payload['order_channels'], QueryField.ORDER_CHANNELS)
            start_date = payload['start_date']
            end_date = payload['end_date']
            return sql.format(
                brands=brands, zone=zone, zones=zones,
                order_channels=order_channels, start_date=start_date, end_date=end_date
            )
        
        else:
            return None
