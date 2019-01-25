import pandas as pd

from query_service.query_api.crm.service.member_grouping_service import MemberGroupingService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.grouping import member_grouping_formator


class MemberGroupingServiceImpl(MemberGroupingService):
    
    def get_member_grouping_list(self, dto):
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
            print(sql)
            if len(member_list) == 0:
                member_list = pd.read_sql_query(sql=sql, con=con)['member_no'].tolist()
            else:
                result_list = pd.read_sql_query(sql=sql, con=con)['member_no'].tolist()
                member_list = list(set(member_list).intersection(result_list))

        resp_dict = dict(success=True, data=member_list, message="success")

        return resp_dict
