import pandas as pd

from query_service.query_api.crm.service import RecruitAnalyseService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.recruit import recruit_analyse_formator

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class RecruitAnalyseServiceImpl(RecruitAnalyseService):
    
    def get_recruit_amount_report_data(self, dto):
        """
        查询招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.STATIC)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_amount_report_data(self, dto):
        """
        查询门店招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.STATIC)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_amount_daily_detail_data(self, dto):
        """
        查询每天招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.DAILY)
        df_result.sort_values(by=['brand', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_amount_daily_detail_data(self, dto):
        """
        查询门店每天招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.DAILY)
        df_result.sort_values(by=['brand', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_amount_monthly_detail_data(self, dto):
        """
        查询每月招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.MONTHLY)
        df_result.sort_values(by=['brand', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_amount_monthly_detail_data(self, dto):
        """
        查询门店每月招募会员详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.all.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.MONTHLY)
        df_result.sort_values(by=['brand', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询有消费会员每日详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.consumed.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.CONSUMED_DAILY)
        df_result.sort_values(by=['brand', 'member_recruit_type', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_consumed_amount_monthly_detail_data(self, dto):
        """
        查询有消费会员每月详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.consumed.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.CONSUMED_MONTHLY)
        df_result.sort_values(by=['brand', 'member_recruit_type', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询门店有消费会员每日详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.consumed.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.CONSUMED_DAILY)
        df_result.sort_values(by=['brand', 'member_recruit_type', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_consumed_amount_monthly_detail_data(self, dto):
        """
        查询门店有消费会员每月详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.consumed.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.CONSUMED_MONTHLY)
        df_result.sort_values(by=['brand', 'member_recruit_type', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_unconsumed_amount_daily_detail_data(self, dto):
        """
        查询未消费会员每日详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.unconsumed.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.UNCONSUMED_DAILY)
        df_result.sort_values(by=['brand', 'member_register_type', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_recruit_unconsumed_amount_monthly_detail_data(self, dto):
        """
        查询未消费会员每月详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.unconsumed.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.UNCONSUMED_MONTHLY)
        df_result.sort_values(by=['brand', 'member_register_type', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_unconsumed_amount_daily_detail_data(self, dto):
        """
        查询门店未消费会员每日详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.unconsumed.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.UNCONSUMED_DAILY)
        df_result.sort_values(by=['brand', 'member_register_type', 'date'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_recruit_unconsumed_amount_monthly_detail_data(self, dto):
        """
        查询门店未消费会员每月详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = recruit_analyse_formator(query_sql.asset.recruit.unconsumed.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.recruit.UNCONSUMED_MONTHLY)
        df_result.sort_values(by=['brand', 'member_register_type', 'year_month'], inplace=True)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict