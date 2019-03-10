import datetime

import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from query_service.apis.crm.coupon import const
from .utils.mapper import member_coupon_order_mapper, coupon_denomination_sum_mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.coupon import query_sql, dtypes


class CouponService:
    
    @classmethod
    def get_member_coupon_order_data(cls, qo):
        """
        查询会员-券-订单关联数据
        :param qo:
        :return:
        """
        sql = member_coupon_order_mapper(query_sql.QUERY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    def export_member_coupon_order_data_csv(cls, qo):
        """
        导出会员-券-订单关联数据
        :param qo:
        :return:
        """
        sql = member_coupon_order_mapper(query_sql.EXPORT, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con).astype(dtype=dtypes.EXPORT)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.columns = const.MemberCouponOrder.DF_RESULT_COLUMNS
            
            now = datetime.datetime.now().strftime('%Y%m%d_%T:%f')
            dir_path = current_app.config['TMP_PATH']
            filename = const.MemberCouponOrder.CSV_FILE_NAME + now + '.csv'
            file_url = current_app.config['FILE_SERVER_URL_PREFIX'] + filename
            
            df.to_csv(dir_path + filename, index=False, encoding='utf_8_sig')
            resp = dict(success=True, data=file_url, message="success")
            
            return resp
    
    @classmethod
    def get_coupon_denomination_sum(cls, qo):
        """
        查询扣券金额
        :param qo:
        :return:
        """
        sql = coupon_denomination_sum_mapper(query_sql.COUPON_DEMONINATION_SUM, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp

