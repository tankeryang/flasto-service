import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.asset_analyse import query_sql
from query_service.exts import cache


class AssetAnalyseService:
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_amount_report_data(cls, qo):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.ALL, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info(sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_amount_report_data(cls, qo):
        """
        查询门店当前会员，有消费会员，未消费会员人数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_new_old_amount_report_data(cls, qo):
        """
        查询新老会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.NEW_OLD, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_new_old_amount_report_data(cls, qo):
        """
        查询门店新老会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.NEW_OLD, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_level_amount_report_data(cls, qo):
        """
        查询会员等级数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.LEVEL, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_level_amount_report_data(cls, qo):
        """
        查询门店会员等级数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.LEVEL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_remain_amount_report_data(cls, qo):
        """
        查询会员留存数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.REMAIN, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_remain_amount_report_data(cls, qo):
        """
        查询门店会员留存数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.REMAIN, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_active_amount_report_data(cls, qo):
        """
        查询活跃会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.ACTIVE, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_active_amount_report_data(cls, qo):
        """
        查询门店活跃会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.ACTIVE, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_frequency_amount_report_data(cls, qo):
        """
        查询累计消费频次会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.FREQUENCY, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_frequency_amount_report_data(cls, qo):
        """
        查询门店累计消费频次会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.FREQUENCY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_recency_amount_report_data(cls, qo):
        """
        查询最近一次消费会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.RECENCY, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_recency_amount_report_data(cls, qo):
        """
        查询门店最近一次消费会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.RECENCY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_monetary_amount_report_data(cls, qo):
        """
        查询累计消费金额会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.MONETARY, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_monetary_amount_report_data(cls, qo):
        """
        查询门店累计消费金额会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.MONETARY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_time_amount_report_data(cls, qo):
        """
        查询入会时长会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.TIME, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_time_amount_report_data(cls, qo):
        """
        查询门店入会时长会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.TIME, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_discount_amount_report_data(cls, qo):
        """
        查询折扣率会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.DISCOUNT, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_discount_amount_report_data(cls, qo):
        """
        查询门店折扣率会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.DISCOUNT, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_sipo_amount_report_data(cls, qo):
        """
        查询客单价会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.zone.SI_PO, qo)
        if sql is None:
            return dict(success=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_sipo_amount_report_data(cls, qo):
        """
        查询门店客单价会员数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.store.SI_PO, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            resp_dict = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp_dict
