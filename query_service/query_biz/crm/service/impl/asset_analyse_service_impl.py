import pandas as pd

from query_service.query_api.crm.service import AssetAnalyseService
from query_service.query_biz.crm.db_utils import (
    get_presto_engine,
    member_analyse_formator,
)

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class AssetAnalyseServiceImpl(AssetAnalyseService):
    
    def get_member_amount_detail(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = member_analyse_formator(query_sql.asset.STATIC, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.STATIC)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict
