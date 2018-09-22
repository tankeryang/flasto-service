import pandas as pd
from query_service.query_api.crm.service import CrmService
from query_service.query_biz.crm.db_utils import (
    get_presto_engine,
    crm_member_income_analyse_format_sql,
    crm_daily_report_format_sql,
)

# resources
from query_service.resources.crm.query_sql import (
    SQL_CRM_TOTAL_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA,
    SQL_CRM_DAILY_REPORT_DATA,
)
from query_service.resources.crm.dtypes import (
    DTYPE_CRM_TOTAL_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA,
    DTYPE_CRM_DAILY_REPORT_DATA,
)


class CrmServiceImpl(CrmService):
    
    def get_daily_report_data(self, dto):
        """
        查询日报
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_daily_report_format_sql(SQL_CRM_DAILY_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_DAILY_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
    
    def get_crm_total_income_report_data(self, dto):
        """
        查询整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(SQL_CRM_TOTAL_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_TOTAL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict

    def get_crm_member_now_before_income_report_data(self, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
    
    def get_crm_member_new_old_income_report_data(self, dto):
        """
        查询新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
    
    def get_crm_member_level_income_report_data(self, dto):
        """
        查询会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
    
    def get_crm_member_mul_dim_income_report_data(self, dto):
        """
        查询多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, data="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
