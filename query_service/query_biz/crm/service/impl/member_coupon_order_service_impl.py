import datetime
import pandas as pd
from io import BytesIO
from flask import send_file, make_response, send_from_directory

from query_service.query_api.crm.service.member_coupon_order_service import MemberCouponOrderService
from query_service.query_biz.crm import const
from query_service.query_biz.crm.utils import get_presto_engine
from query_service.query_biz.crm.utils.formator.member_coupon_order import (
    member_coupon_order_formator,
    coupon_denomination_sum_formator,
)

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class MemberCouponOrderServiceImpl(MemberCouponOrderService):
    
    @classmethod
    def get_member_coupon_order_data(cls, dto):
        """
        查询会员-券-订单关联数据
        :param dto:
        :return:
        """
        sql = member_coupon_order_formator(query_sql.member_coupon_order.QUERY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")

        return resp_dict

    @classmethod
    def export_member_coupon_order_data_xlsx(cls, dto):
        """
        导出会员-券-订单关联数据
        :param dto:
        :return:
        """
        sql = member_coupon_order_formator(query_sql.member_coupon_order.EXPORT, dto)

        presto_engine = get_presto_engine()
        con = presto_engine.connect()

        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtype=dtypes.member_coupon_order.EXPORT)
        df_result.columns = const.MemberCouponOrder.DF_RESULT_COLUMNS
        
        now = datetime.datetime.now().strftime('%Y%m%d_%T:%f')
        path = const.ExportFilePath.PATH
        filename = const.MemberCouponOrder.CSV_FILE_NAME + now + '.xlsx'

        # output = BytesIO()
        
        # writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df_result.to_excel(path=path + filename, index=False, encoding='utf_8_sig', engine='xlsxwriter')
        # writer.close()
        
        # output.seek(0)
        
        response = make_response(send_from_directory(path, filename, as_attachment=True))
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        
        # return send_file(output, attachment_filename=filename, as_attachment=True)
        return response

    @classmethod
    def get_coupon_denomination_sum(cls, dto):
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