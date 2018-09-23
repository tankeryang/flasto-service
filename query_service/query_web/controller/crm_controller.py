from flask_restplus import Resource, Namespace
ns_1 = Namespace('CRM 报表中心', path='/crm', description='日报月报api')
ns_2 = Namespace('CRM 业绩分析', path='/crm', description='业绩分析api')


from datetime import datetime

from query_service.query_biz.crm.service.impl import CrmServiceImpl
from query_service.query_web import api


from query_service.query_api.crm.entity.dto import (
    crm_member_analyse_req_dto_model,
    crm_daily_report_req_dto_model,
)
from query_service.query_api.crm.entity.po import (
    crm_total_income_report_list_model,
    crm_member_nowbefroe_income_report_list_model,
    crm_member_newold_income_report_list_model,
    crm_member_level_income_report_list_model,
    crm_member_muldim_income_report_list_model,
    crm_daily_report_list_model,
)


@ns_1.route('/CrmDailyReport')
class CrmDailyReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_1.expect(crm_daily_report_req_dto_model, validate=True)
    @ns_1.marshal_with(crm_daily_report_list_model)
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        dto = api.payload
        resp_dict = CrmDailyReportController.crm_service.get_daily_report_data(dto)
        
        return resp_dict


@ns_1.route('/CrmDailyReportExcel')
class CrmDailyReportExcelController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_1.expect(crm_daily_report_req_dto_model, validate=True)
    def post(self):
        """
        日报excel表格导出
        格式为: yyyy-MM-dd hh:mm:ss(当前时间) 日报数据.xlsx
        """
        dto = api.payload
        now_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        resp = CrmDailyReportExcelController.crm_service.get_daily_report_excel(now_timestamp, dto)
        
        # 删除服务器的生成文件
        CrmDailyReportExcelController.crm_service.del_local_daily_report_excel(now_timestamp)
        
        return resp


@ns_2.route('/CrmTotalIncomeReport')
class CrmTotalIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(crm_total_income_report_list_model)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        dto = api.payload
        resp_dict = CrmTotalIncomeReportController.crm_service.get_crm_total_income_report_data(dto)
        
        return resp_dict


@ns_2.route('/CrmMemberNowBeforeIncomeReport')
class CrmMemberNowBeforeIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(crm_member_nowbefroe_income_report_list_model)
    def post(self):
        """
        查询会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        dto = api.payload
        resp_dict = CrmMemberNowBeforeIncomeReportController.crm_service.get_crm_member_now_before_income_report_data(dto)
        
        return resp_dict


@ns_2.route('/CrmMemberNewOldIncomeReport')
class CrmMemberNewOldIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(crm_member_newold_income_report_list_model)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        dto = api.payload
        resp_dict = CrmMemberNewOldIncomeReportController.crm_service.get_crm_member_new_old_income_report_data(dto)
        
        return resp_dict


@ns_2.route('/CrmMemberLevelIncomeReport')
class CrmMemberLevelIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(crm_member_level_income_report_list_model)
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        dto = api.payload
        resp_dict = CrmMemberLevelIncomeReportController.crm_service.get_crm_member_level_income_report_data(dto)
        
        return resp_dict


@ns_2.route('/CrmMemberMulDimIncomeReport')
class CrmMemberMulDimIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(crm_member_muldim_income_report_list_model)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        dto = api.payload
        resp_dict = CrmMemberMulDimIncomeReportController.crm_service.get_crm_total_income_report_data(dto)
        
        return resp_dict
