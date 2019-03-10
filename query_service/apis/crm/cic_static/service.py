import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper
from query_service.apis.utils.db import engine
from query_service.resources.apis.crm.cic_static import query_sql
from query_service.exts import cache


class CicStaticService:
    """
    Cic 首页展示处理逻辑
    """
    @classmethod
    @cache.memoize(timeout=86400)
    def get_cic_static_detail_data(cls, qo):
        """
        查询 cic 首页静态数据
        :param qo:
        :return:
        """
        sql = mapper(query_sql.MAIN_PAGE, qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()
        
        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
