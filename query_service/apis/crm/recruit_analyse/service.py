import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.recruit_analyse import query_sql
from query_service.exts import cache


class RecruitAnalyseService:
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_amount_report_data(cls, qo):
        """
        查询招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.zone.ALL, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
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
    @cache.memoize(timeout=86400)
    def get_store_recruit_amount_report_data(cls, qo):
        """
        查询门店招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.store.ALL, qo)
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
    @cache.memoize(timeout=86400)
    def get_recruit_amount_daily_detail_data(cls, qo):
        """
        查询每天招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.zone.DAILY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_amount_daily_detail_data(cls, qo):
        """
        查询门店每天招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_amount_monthly_detail_data(cls, qo):
        """
        查询每月招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.zone.MONTHLY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_amount_monthly_detail_data(cls, qo):
        """
        查询门店每月招募会员详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.all.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_consumed_amount_daily_detail_data(cls, qo):
        """
        查询有消费会员每日详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.consumed.zone.DAILY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_recruit_type', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_consumed_amount_monthly_detail_data(cls, qo):
        """
        查询有消费会员每月详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.consumed.zone.MONTHLY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_recruit_type', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_consumed_amount_daily_detail_data(cls, qo):
        """
        查询门店有消费会员每日详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.consumed.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_recruit_type', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_consumed_amount_monthly_detail_data(cls, qo):
        """
        查询门店有消费会员每月详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.consumed.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_recruit_type', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_unconsumed_amount_daily_detail_data(cls, qo):
        """
        查询未消费会员每日详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.unconsumed.zone.DAILY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_register_type', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_recruit_unconsumed_amount_monthly_detail_data(cls, qo):
        """
        查询未消费会员每月详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.unconsumed.zone.MONTHLY, qo)
        if sql is None:
            return dict(success=False, message="查询区域参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_register_type', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_unconsumed_amount_daily_detail_data(cls, qo):
        """
        查询门店未消费会员每日详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.unconsumed.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_register_type', 'date'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_recruit_unconsumed_amount_monthly_detail_data(cls, qo):
        """
        查询门店未消费会员每月详情
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.unconsumed.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_register_type', 'year_month'], inplace=True)
            resp = dict(success=True, data=df.to_dict(orient='records'), message="success")
            return resp
