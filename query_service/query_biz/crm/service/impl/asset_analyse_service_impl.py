import pandas as pd

from query_service.query_api.crm.service import AssetAnalyseService
from query_service.query_biz.crm.db_utils import get_presto_engine
from query_service.query_biz.crm.db_utils.formator.asset import asset_analyse_formator

# resources
import query_service.resources.crm.query_sql as query_sql
import query_service.resources.crm.dtypes as dtypes


class AssetAnalyseServiceImpl(AssetAnalyseService):
    
    def get_member_amount_report_data(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.STATIC)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_amount_report_data(self, dto):
        """
        查询门店当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.STATIC)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_new_old_amount_report_data(self, dto):
        """
        查询新老会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.NEW_OLD, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.NEW_OLD)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_new_old_amount_report_data(self, dto):
        """
        查询门店新老会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.NEW_OLD, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.NEW_OLD)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_level_amount_report_data(self, dto):
        """
        查询会员等级数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.LEVEL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.LEVEL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_level_amount_report_data(self, dto):
        """
        查询门店会员等级数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.LEVEL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.LEVEL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_remain_amount_report_data(self, dto):
        """
        查询会员留存数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.REMAIN, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.REMAIN)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_remain_amount_report_data(self, dto):
        """
        查询门店会员留存数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.REMAIN, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.REMAIN)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_active_amount_report_data(self, dto):
        """
        查询活跃会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.ACTIVE, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.ACTIVE)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_active_amount_report_data(self, dto):
        """
        查询门店活跃会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.ACTIVE, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.ACTIVE)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_frequency_amount_report_data(self, dto):
        """
        查询累计消费频次会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.FREQUENCY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.FREQUENCY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_frequency_amount_report_data(self, dto):
        """
        查询门店累计消费频次会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.FREQUENCY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.FREQUENCY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_recency_amount_report_data(self, dto):
        """
        查询最近一次消费会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.RECENCY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.RECENCY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_recency_amount_report_data(self, dto):
        """
        查询门店最近一次消费会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.RECENCY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.RECENCY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_monetary_amount_report_data(self, dto):
        """
        查询累计消费金额会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.MONETARY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.MONETARY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_monetary_amount_report_data(self, dto):
        """
        查询门店累计消费金额会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.MONETARY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.MONETARY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_time_amount_report_data(self, dto):
        """
        查询入会时长会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.TIME, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.TIME)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_time_amount_report_data(self, dto):
        """
        查询门店入会时长会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.TIME, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.TIME)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_discount_amount_report_data(self, dto):
        """
        查询折扣率会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.DISCOUNT, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.DISCOUNT)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_discount_amount_report_data(self, dto):
        """
        查询门店折扣率会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.DISCOUNT, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.DISCOUNT)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_sipo_amount_report_data(self, dto):
        """
        查询客单价会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.zone.SI_PO, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.SI_PO)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_sipo_amount_report_data(self, dto):
        """
        查询门店客单价会员数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = asset_analyse_formator(query_sql.asset.member.store.SI_PO, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.asset.member.SI_PO)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict