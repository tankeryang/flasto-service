import pandas as pd
from flask import current_app
from pyhive.exc import DatabaseError

from query_service.query_api.crm.service.member_grouping_service import MemberGroupingService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.grouping import member_grouping_formator


class MemberGroupingServiceImpl(MemberGroupingService):
    
    @classmethod
    def get_member_grouping_list(cls, dto):
        """
        查询会员分组列表
        :param dto:
        :return:
        """
        sql_list = member_grouping_formator(dto)
        if sql_list is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        member_list = []
        for sql in sql_list:
            current_app.logger.info("Execute SQL: " + sql)
            
            if len(member_list) == 0:
                try:
                    member_list = pd.read_sql_query(sql=sql, con=con)['member_no'].tolist()
                except (DatabaseError, TypeError) as e:
                    current_app.logger.exception(e)
            else:
                try:
                    result_list = pd.read_sql_query(sql=sql, con=con)['member_no'].tolist()
                except (DatabaseError, TypeError) as e:
                    current_app.logger.exception(e)
                else:
                    member_list = list(set(member_list).intersection(result_list))

        resp_dict = dict(success=True, data=member_list, message="success")

        return resp_dict
