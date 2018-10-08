import pandas as pd

from query_service.query_api.crm.service import (
    ReportCenterService,
    IncomeAnalyseService,
    AssetAnalyseService,
)
from query_service.query_biz.crm.db_utils import (
    get_presto_engine,
    daily_report_formator,
    income_analyse_formator,
    asset_analyse_formator,
)

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


class IncomeAnalyseServiceImpl(IncomeAnalyseService):
    
    def get_total_income_report_data(self, dto):
        """
        查询整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_total_income_report_data(self, dto):
        """
        查询门店整体收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_total_daily_income_detail_data(self, dto):
        """
        查询整体每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.DAILY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_total_daily_income_detail_data(self, dto):
        """
        查询门店整体每日收入取数
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.DAILY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_total_monthly_income_detail_data(self, dto):
        """
        查询整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.zone.MONTHLY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_total_monthly_income_detail_data(self, dto):
        """
        查询门店整体每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.total.store.MONTHLY, dto)
        if sql is None:
            return dict(sucess=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.total.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_now_before_income_report_data(self, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.now_before.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.now_before.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_now_before_income_report_data(self, dto):
        """
        查询门店会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.now_before.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.now_before.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_new_old_income_report_data(self, dto):
        """
        查询新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_new_old_income_report_data(self, dto):
        """
        查询门店新老会员收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_new_old_daily_income_detail_data(self, dto):
        """
        查询新老会员每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_new_old_daily_income_detail_data(self, dto):
        """
        查询门店新老会员每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_new_old_monthly_income_detail_data(self, dto):
        """
        查询新老会员每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_new_old_monthly_income_detail_data(self, dto):
        """
        查询门店新老会员每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.new_old.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.new_old.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_level_income_report_data(self, dto):
        """
        查询会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_level_income_report_data(self, dto):
        """
        查询门店会员等级收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_level_daily_income_detail_data(self, dto):
        """
        查询会员等级每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_level_daily_income_detail_data(self, dto):
        """
        查询门店会员等级每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_level_monthly_income_detail_data(self, dto):
        """
        查询会员等级每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_level_monthly_income_detail_data(self, dto):
        """
        查询门店会员等级每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.level.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.level.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_mul_dim_income_report_data(self, dto):
        """
        查询多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_mul_dim_income_report_data(self, dto):
        """
        查询门店多维度收入分析
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_mul_dim_daily_income_detail_data(self, dto):
        """
        查询多维度每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_mul_dim_daily_income_detail_data(self, dto):
        """
        查询门店多维度每日收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_mul_dim_monthly_income_detail_data(self, dto):
        """
        查询多维度每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_store_member_mul_dim_monthly_income_detail_data(self, dto):
        """
        查询门店多维度每月收入趋势
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.mul_dim.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.mul_dim.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict
    
    def get_member_register_proportion_report_data(self, dto):
        """
        查询登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
        
        return resp_dict

    def get_store_member_register_proportion_report_data(self, dto):
        """
        查询门店登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.ALL, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.ALL)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
    
        return resp_dict

    def get_member_daily_register_proportion_detail_data(self, dto):
        """
        查询每日登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
    
        return resp_dict

    def get_store_member_daily_register_proportion_detail_data(self, dto):
        """
        查询门店每日登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.DAILY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.DAILY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
    
        return resp_dict

    def get_member_monthly_register_proportion_detail_data(self, dto):
        """
        查询每月登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.zone.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
    
        return resp_dict

    def get_store_member_monthly_register_proportion_detail_data(self, dto):
        """
        查询门店每月登记率
        :param dto: restplus.Api.payload
        :return: response dict
        """
        sql = income_analyse_formator(query_sql.income.member.register_proportion.store.MONTHLY, dto)
        if sql is None:
            return dict(success=False, message="参数错误")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(dtypes.income.member.register_proportion.MONTHLY)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'), message="success")
    
        return resp_dict


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
