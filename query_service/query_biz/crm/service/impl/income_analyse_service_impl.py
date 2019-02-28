import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from query_service.query_api.crm.service import IncomeAnalyseService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.income import income_analyse_formator
from query_service.query_web.libs.cache import cache

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class IncomeAnalyseServiceImpl(IncomeAnalyseService):
    
    @classmethod
    @cache.memoize(timeout=7200)
    def get_total_income_report_data(cls, dto):
        """
        查询整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_total_income_report_data(cls, dto):
        """
        查询门店整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_total_daily_income_detail_data(cls, dto):
        """
        查询整体每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.DAILY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_total_daily_income_detail_data(cls, dto):
        """
        查询门店整体每日收入取数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.DAILY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_total_monthly_income_detail_data(cls, dto):
        """
        查询整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.MONTHLY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_total_monthly_income_detail_data(cls, dto):
        """
        查询门店整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.MONTHLY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_now_before_income_report_data(cls, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.now_before.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.now_before.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_now_before_income_report_data(cls, dto):
        """
        查询门店会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.now_before.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.now_before.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_new_old_income_report_data(cls, dto):
        """
        查询新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_new_old_income_report_data(cls, dto):
        """
        查询门店新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_new_old_daily_income_detail_data(cls, dto):
        """
        查询新老会员每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_new_old_daily_income_detail_data(cls, dto):
        """
        查询门店新老会员每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_new_old_monthly_income_detail_data(cls, dto):
        """
        查询新老会员每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_new_old_monthly_income_detail_data(cls, dto):
        """
        查询门店新老会员每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_level_income_report_data(cls, dto):
        """
        查询会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_level_income_report_data(cls, dto):
        """
        查询门店会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_level_daily_income_detail_data(cls, dto):
        """
        查询会员等级每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_level_daily_income_detail_data(cls, dto):
        """
        查询门店会员等级每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_level_monthly_income_detail_data(cls, dto):
        """
        查询会员等级每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_level_monthly_income_detail_data(cls, dto):
        """
        查询门店会员等级每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_mul_dim_income_report_data(cls, dto):
        """
        查询多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_mul_dim_income_report_data(cls, dto):
        """
        查询门店多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_mul_dim_daily_income_detail_data(cls, dto):
        """
        查询多维度每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_mul_dim_daily_income_detail_data(cls, dto):
        """
        查询门店多维度每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_mul_dim_monthly_income_detail_data(cls, dto):
        """
        查询多维度每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_mul_dim_monthly_income_detail_data(cls, dto):
        """
        查询门店多维度每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'member_newold_type', 'member_level_type', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_register_proportion_report_data(cls, dto):
        """
        查询登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_register_proportion_report_data(cls, dto):
        """
        查询门店登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.ALL)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_daily_register_proportion_detail_data(cls, dto):
        """
        查询每日登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_daily_register_proportion_detail_data(cls, dto):
        """
        查询门店每日登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.DAILY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone', 'date'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_member_monthly_register_proportion_detail_data(cls, dto):
        """
        查询每月登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict

    @classmethod
    @cache.memoize(timeout=7200)
    def get_store_member_monthly_register_proportion_detail_data(cls, dto):
        """
        查询门店每月登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.MONTHLY)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df_result.sort_values(by=['brand', 'zone', 'year_month'], inplace=True)
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict