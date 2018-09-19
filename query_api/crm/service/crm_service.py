import pandas as pd
from flask_restplus import Resource, Namespace
# import query sql
from query_api.resources.crm.query_sql import (
    SQL_CRM_MEMBER_TOTAL_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA,
    SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA,
)
# import pandas dtype
from query_api.resources.crm.dtypes import (
    DTYPE_CRM_MEMBER_TOTAL_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA,
    DTYPE_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA,
)
# import sql util
from query_api.crm.db_utils import format_sql, get_presto_engine
# import api object
from query_api import api

# define namespace
ns = Namespace('crm', description="Crm - presto查询服务api")

# import po dto
from query_api.crm.entity.dto import crm_member_analyse_req_dto_model
from query_api.crm.entity.po import (
    crm_member_total_income_report_list_model,
    crm_member_nowbefroe_income_report_list_model,
    crm_member_newold_income_report_list_model,
    crm_member_level_income_report_list_model,
    crm_member_muldim_income_report_list_model,
)


@ns.route('/CrmMemberTotalIncomeReport')
@ns.response(404, "非法查询参数")
@ns.doc(id="查询整体收入分析")
class CrmMemberTotalIncomeReportApi(Resource):
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_total_income_report_list_model)
    def post(self):
        dto = api.payload
        sql = format_sql(SQL_CRM_MEMBER_TOTAL_INCOME_REPORT_DATA, dto)
        if sql is None:
            ns.abort(404, "非法查询")

        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_TOTAL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict


@ns.route('/CrmMemberNowBeforeIncomeReport')
@ns.response(404, "非法查询参数")
@ns.doc(id="查询当月当年往年会员收入分析")
class CrmMemberNowBeforeIncomeReportApi(Resource):
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_nowbefroe_income_report_list_model)
    def post(self):
        dto = api.payload
        sql = format_sql(SQL_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA, dto)
        if sql is None:
            ns.abort(404, "非法查询")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_NOWBEFORE_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
    
        return resp_dict


@ns.route('/CrmMemberNewOldIncomeReport')
@ns.response(404, "非法查询参数")
@ns.doc(id="查询新老会员收入分析")
class CrmMemberNewOldIncomeReportApi(Resource):
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_newold_income_report_list_model)
    def post(self):
        dto = api.payload
        sql = format_sql(SQL_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA, dto)
        if sql is None:
            ns.abort(404, "非法查询")
    
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
    
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_NEWOLD_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
    
        return resp_dict


@ns.route('/CrmMemberLevelIncomeReport')
@ns.response(404, "非法查询参数")
@ns.doc(id="查询会员等级收入分析")
class CrmMemberLevelIncomeReportApi(Resource):
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_level_income_report_list_model)
    def post(self):
        dto = api.payload
        sql = format_sql(SQL_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA, dto)
        if sql is None:
            ns.abort(404, "非法查询")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_LEVEL_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict


@ns.route('/CrmMemberMulDimIncomeReport')
@ns.response(404, "非法查询参数")
@ns.doc(id="查询会员多维度收入分析")
class CrmMemberMulDimIncomeReportApi(Resource):
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_muldim_income_report_list_model)
    def post(self):
        dto = api.payload
        sql = format_sql(SQL_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA, dto)
        if sql is None:
            ns.abort(404, "非法查询")
        
        presto_engine = get_presto_engine()
        con = presto_engine.connect()
        
        df_result = pd.read_sql_query(sql=sql, con=con).astype(DTYPE_CRM_MEMBER_MULDIM_INCOME_REPORT_DATA)
        resp_dict = dict(success=True, data=df_result.to_dict(orient='records'))
        
        return resp_dict
