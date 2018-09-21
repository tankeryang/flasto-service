from flask_restplus import Resource, Namespace
from query_service.query_biz.crm.service.impl import CrmServiceImpl
from query_service.query_web import api

ns = Namespace('crm', description='crm 业绩分析模块 api')

from query_service.query_api.crm.entity.dto import crm_member_analyse_req_dto_model
from query_service.query_api.crm.entity.po import (
    crm_total_income_report_list_model,
    crm_member_nowbefroe_income_report_list_model,
    crm_member_newold_income_report_list_model,
    crm_member_level_income_report_list_model,
    crm_member_muldim_income_report_list_model,
)


@ns.route('/CrmTotalIncomeReport')
class CrmTotalIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_total_income_report_list_model)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        dto = api.payload
        resp_dict = CrmTotalIncomeReportController.crm_service.get_crm_total_income_report_data(dto)
        
        return resp_dict


@ns.route('/CrmMemberNowBeforeIncomeReport')
class CrmMemberNowBeforeIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_nowbefroe_income_report_list_model)
    def post(self):
        """
        查询会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        dto = api.payload
        resp_dict = CrmMemberNowBeforeIncomeReportController.crm_service.get_crm_member_now_before_income_report_data(dto)
        
        return resp_dict


@ns.route('/CrmMemberNewOldIncomeReport')
class CrmMemberNewOldIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_newold_income_report_list_model)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        dto = api.payload
        resp_dict = CrmMemberNewOldIncomeReportController.crm_service.get_crm_member_new_old_income_report_data(dto)
        
        return resp_dict


@ns.route('/CrmMemberLevelIncomeReport')
class CrmMemberLevelIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_level_income_report_list_model)
    def post(self):
        """
        查询会员等级收入分析
        会员。普通会员，VIP会员
        """
        dto = api.payload
        resp_dict = CrmMemberLevelIncomeReportController.crm_service.get_crm_member_level_income_report_data(dto)
        
        return resp_dict


@ns.route('/CrmMemberMulDimIncomeReport')
class CrmMemberMulDimIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns.expect(crm_member_analyse_req_dto_model)
    @ns.marshal_with(crm_member_muldim_income_report_list_model)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, 老会员} 老会员:{普通会员, 老会员}
        """
        dto = api.payload
        resp_dict = CrmMemberMulDimIncomeReportController.crm_service.get_crm_total_income_report_data(dto)
        
        return resp_dict
