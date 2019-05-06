import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import dr_mapper, mr_sales_mapper, mr_asset_mapper, mr_active_mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.report_center import query_sql
from query_service.exts import cache


class ReportCenterService:

    @classmethod
    def get_daily_report_data(cls, qo):
        """
        查询日报
        :param qo:
        :return:
        """
        sql = dr_mapper(query_sql.daily.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
    
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df.sort_values(by=['sales_area_num', 'city', 'company_name', 'store_code', 'member_type_num'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")

    @classmethod
    def get_monthly_report_sales_data(cls, qo):
        """
        月报-业绩 查询
        :param qo:
        :return:
        """
        sql = mr_sales_mapper(query_sql.monthly.MONTHLY_SALES, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()

        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df.sort_values(by=['brand_code', 'channel_type', 'member_type', 'kpi_num'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")

    @classmethod
    def get_monthly_report_asset_data(cls, qo):
        """
        月报-会员资产 查询
        :param qo:
        :return:
        """
        sql = mr_asset_mapper(query_sql.monthly.MONTHLY_ASSET, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()

        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df.sort_values(by=['brand_code', 'channel_type', 'member_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")

    @classmethod
    def get_monthly_report_active_data(cls, qo):
        """
        月报-有效会员 查询
        :param qo:
        :return:
        """
        sql = mr_active_mapper(query_sql.monthly.MONTHLY_ACTIVE, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()

        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df.sort_values(by=['brand_code', 'channel_type'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
