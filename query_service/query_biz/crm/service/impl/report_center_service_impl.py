import pandas as pd

from query_service.query_api.crm.service import ReportCenterService
from query_service.query_biz.crm.db_utils import get_presto_engine
from query_service.query_biz.crm.db_utils.formator.report_center import daily_report_formator

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class ReportCenterServiceImpl(ReportCenterService):
    
    def get_daily_report_data(self, dto):
        """
        查询日报
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = daily_report_formator(query_sql.report_center.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.report_center.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict