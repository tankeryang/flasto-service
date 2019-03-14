import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.report_center import query_sql


class ReportCenterService:
    """
    日报处理逻辑
    """
    @classmethod
    def get_daily_report_data(cls, qo):
        """
        查询日报
        :param qo:
        :return:
        """
        sql = mapper(query_sql.DAILY, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
    
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            df.sort_values(by=['sales_area_num', 'city', 'store_code', 'member_type_num'], inplace=True)
            return dict(success=True, data=df.to_dict(orient='records'), message="success")