import pandas as pd

from query_service.query_api.crm.service.member_coupon_order_service import MemberCouponOrderService
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.member_coupon_order import (
    member_coupon_order_formator,
    coupon_denomination_sum_formator,
)


# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class MemberCouponOrderServiceImpl(MemberCouponOrderService):

    def get_member_coupon_order_data(self, dto):
        """
        查询会员-券-订单关联数据
        :param dto:
        :return:
        """
        sql = member_coupon_order_formator(query_sql.member_coupon_order.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.member_coupon_order.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict


    def get_coupon_denomination_sum(self, dto):
        """
        查询订单使用现金券总面额
        :param dto:
        :return:
        """
        sql = coupon_denomination_sum_formator(query_sql.member_coupon_order.COUPON_DEMONINATION_SUM, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.member_coupon_order.COUPON_DENOMINATION_SUM)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict
