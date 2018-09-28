import os
import pandas as pd
from io import BytesIO
from flask import make_response, send_file

from query_service.query_api.crm.service import CrmService
from query_service.query_biz.crm.db_utils import (
    get_presto_engine,
    crm_member_income_analyse_format_sql,
    crm_daily_report_format_sql,
)

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes
import query_service.resources.crm.excel_header as header


class CrmServiceImpl(CrmService):
    
    def get_daily_report_data(self, dto):
        """
        查询日报
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_daily_report_format_sql(query_sql.SQL_CRM_DAILY_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_DAILY_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_daily_report_excel(self, timestamp, dto):
        """
        日报excel导出
        :param timestamp: 当前查询时间
        :param dto: restplus.Api.payload
        :return: excel
        """
        sql = crm_daily_report_format_sql(query_sql.SQL_CRM_DAILY_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_DAILY_REPORT_DATA)
        df_result.columns = header.HEADER_CRM_DAILY_REPORT_EXCEL
        
        output = BytesIO()
        df_result.to_excel(
            "{timestamp} 日报数据.xlsx".format(timestamp=timestamp)
        )
        output.seek(0)
        
        resp = make_response(send_file(
            output,
            attachment_filename="{timestamp} 日报数据.xlsx".format(timestamp=timestamp),
            as_attachment=True
        ))
        
        return resp

    def del_local_daily_report_excel(self, timestamp):
        """
        删除服务器上的excel文件
        :param timestamp: 生成时间
        :return:
        """
        file_name = "{timestamp} 日报数据.xlsx".format(timestamp=timestamp)
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            pass

    def get_crm_total_income_report_data(self, dto):
        """
        查询整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_TOTAL_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_store_total_income_report_data(self, dto):
        """
        查询门店整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_STORE_TOTAL_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    def get_crm_total_daily_income_detail_data(self, dto):
        """
        查询整体每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_TOTAL_DAILY_INCOME_DETAIL_DATA, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_DAILY_INCOME_DETAIL_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_store_total_daily_income_detail_data(self, dto):
        """
        查询门店整体每日收入取数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_STORE_TOTAL_DAILY_INCOME_DETAIL_DATA, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_DAILY_INCOME_DETAIL_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    def get_crm_total_monthly_income_detail_data(self, dto):
        """
        查询整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_TOTAL_MONTHLY_INCOME_DETAIL_DATA, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_MONTHLY_INCOME_DETAIL_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    def get_crm_store_total_monthly_income_detail_data(self, dto):
        """
        查询门店整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_STORE_TOTAL_MONTHLY_INCOME_DETAIL_DATA, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_TOTAL_MONTHLY_INCOME_DETAIL_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    def get_crm_member_now_before_income_report_data(self, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_member_new_old_income_report_data(self, dto):
        """
        查询新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_member_level_income_report_data(self, dto):
        """
        查询会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_member_mul_dim_income_report_data(self, dto):
        """
        查询多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_crm_member_register_proportion_report_data(self, dto):
        """
        查询登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_REGISTER_PROPORTION_REPORT_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_CRM_MEMBER_REGISTER_PROPORTION_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    def get_crm_member_amount_detail(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = crm_member_income_analyse_format_sql(query_sql.SQL_CRM_MEMBER_AMOUNT_DETAIL_DATA, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.DTYPE_MEMBER_AMOUNT_DETAIL_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict
