import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.income_analyse import query_sql
from query_service.exts import cache


class IncomeAnalyseService:
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_total_income_report_data(cls, qo):
        """
        查询整体收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.zone.ALL, qo)
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
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_total_income_report_data(cls, qo):
        """
        查询门店整体收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_total_daily_income_detail_data(cls, qo):
        """
        查询整体每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.zone.DAILY, qo)
        if sql is None:
            return dict(sucess=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_total_daily_income_detail_data(cls, qo):
        """
        查询门店整体每日收入取数
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_total_monthly_income_detail_data(cls, qo):
        """
        查询整体每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.zone.MONTHLY, qo)
        if sql is None:
            return dict(sucess=False, message="区域查询参数错误")
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_total_monthly_income_detail_data(cls, qo):
        """
        查询门店整体每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.total.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_new_old_income_report_data(cls, qo):
        """
        查询新老会员收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.zone.ALL, qo)
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
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_new_old_income_report_data(cls, qo):
        """
        查询门店新老会员收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_new_old_daily_income_detail_data(cls, qo):
        """
        查询新老会员每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.zone.DAILY, qo)
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
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_new_old_daily_income_detail_data(cls, qo):
        """
        查询门店新老会员每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_new_old_monthly_income_detail_data(cls, qo):
        """
        查询新老会员每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.zone.MONTHLY, qo)
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
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_new_old_monthly_income_detail_data(cls, qo):
        """
        查询门店新老会员每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.new_old.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_level_income_report_data(cls, qo):
        """
        查询会员等级收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.zone.ALL, qo)
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
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_level_income_report_data(cls, qo):
        """
        查询门店会员等级收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_level_daily_income_detail_data(cls, qo):
        """
        查询会员等级每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.zone.DAILY, qo)
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
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_level_daily_income_detail_data(cls, qo):
        """
        查询门店会员等级每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_level_monthly_income_detail_data(cls, qo):
        """
        查询会员等级每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.zone.MONTHLY, qo)
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
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_level_monthly_income_detail_data(cls, qo):
        """
        查询门店会员等级每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.level.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_mul_dim_income_report_data(cls, qo):
        """
        查询多维度收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.zone.ALL, qo)
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
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_mul_dim_income_report_data(cls, qo):
        """
        查询门店多维度收入分析
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_mul_dim_daily_income_detail_data(cls, qo):
        """
        查询多维度每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.zone.DAILY, qo)
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
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_mul_dim_daily_income_detail_data(cls, qo):
        """
        查询门店多维度每日收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_mul_dim_monthly_income_detail_data(cls, qo):
        """
        查询多维度每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.zone.MONTHLY, qo)
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
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_mul_dim_monthly_income_detail_data(cls, qo):
        """
        查询门店多维度每月收入趋势
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.mul_dim.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_register_proportion_report_data(cls, qo):
        """
        查询登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.zone.ALL, qo)
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
            df.sort_values(by=['brand', 'zone'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_register_proportion_report_data(cls, qo):
        """
        查询门店登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.store.ALL, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'zone'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_daily_register_proportion_detail_data(cls, qo):
        """
        查询每日登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.zone.DAILY, qo)
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
            df.sort_values(by=['brand', 'zone', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_daily_register_proportion_detail_data(cls, qo):
        """
        查询门店每日登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.store.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'zone', 'date'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_monthly_register_proportion_detail_data(cls, qo):
        """
        查询每月登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.zone.MONTHLY, qo)
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
            df.sort_values(by=['brand', 'zone', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_store_member_monthly_register_proportion_detail_data(cls, qo):
        """
        查询门店每月登记率
        :param qo: restplus.Api.payload
        :return: response dict
        """
        sql = mapper(query_sql.member.register_proportion.store.MONTHLY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            df.sort_values(by=['brand', 'zone', 'year_month'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
