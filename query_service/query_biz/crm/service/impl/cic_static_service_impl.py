import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from query_service.query_api.crm.service import CicStaticService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.cic_static import cic_static_formator
from query_service.query_web.libs import cache

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class CicStaticServiceImpl(CicStaticService):
    
    @classmethod
    @cache.memoize(timeout=7200)
    def get_cic_static_detail_data(cls, dto):
        """
        查询cic首页静态数据详情
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = cic_static_formator(query_sql.cic_static.MAIN_PAGE, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        current_app.logger.info("Execute SQL: " + sql)
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        try:
            df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.cic_static.MAIN_PAGE)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
        else:
            resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
            return resp_dict
