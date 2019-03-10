import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from .utils.mapper import mapper, count_mapper
from query_service.apis.utils.db import engine
from query_service.exts import cache


class GroupingService:
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_grouping_detail(cls, qo):
        """
        查询会员分组详情, 带分页
        :param qo:
        :return:
        """
        sql = mapper(qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()

        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            return dict(success=True, data=df.to_dict(orient='records'), message="success")
    
    @classmethod
    @cache.memoize(timeout=86400)
    def get_member_grouping_count(cls, qo):
        """
        查询分组总人数
        :param qo:
        :return:
        """
        sql = count_mapper(qo)
        current_app.logger.info("Execute SQL: " + sql)
        con = engine().connect()

        try:
            df = pd.read_sql_query(sql=sql, con=con)
        except (DatabaseError, TypeError) as e:
            current_app.logger.exception(e)
            return dict(success=False, message="Internal Server Error")
        else:
            return dict(success=True, data=df['total'], message="success")
