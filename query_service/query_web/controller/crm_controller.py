from flask_restplus import Resource, Namespace
ns_1 = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')
ns_2 = Namespace('CRM 业绩分析', path='/crm/income', description='业绩分析api')
ns_3 = Namespace('CRM 客户资产', path='/crm/asset', description='客户资产api')


from datetime import datetime

from query_service.query_biz.crm.service.impl import CrmServiceImpl

import query_service.query_api.crm.entity.dto as dto
import query_service.query_api.crm.entity.po as po


@ns_1.route('/DailyReport')
class CrmDailyReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_1.expect(dto.crm_daily_report_req_dto_model, validate=True)
    @ns_1.marshal_with(po.crm_daily_report_list_model)
    def post(self):
        """
        日报查询
        全国，大区，城市，门店
        """
        resp_dict = CrmDailyReportController.crm_service.get_daily_report_data(ns_1.payload)
        
        return resp_dict


@ns_1.route('/DailyReportExcel')
class CrmDailyReportExcelController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_1.expect(dto.crm_daily_report_req_dto_model, validate=True)
    def post(self):
        """
        日报excel表格导出
        格式为: yyyy-MM-dd hh:mm:ss(当前时间) 日报数据.xlsx
        """
        now_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        resp = CrmDailyReportExcelController.crm_service.get_daily_report_excel(now_timestamp, ns_1.payload)
        
        # 删除服务器的生成文件
        CrmDailyReportExcelController.crm_service.del_local_daily_report_excel(now_timestamp)
        
        return resp


@ns_2.route('/TotalIncomeReport')
class CrmTotalIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_total_income_report_list_model)
    def post(self):
        """
        查询整体收入分析
        整体，会员，非会员
        """
        resp_dict = CrmTotalIncomeReportController.crm_service.get_crm_total_income_report_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/TotalDailyIncomeDetail')
class CrmTotalDailyIncomeDetailController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_total_daily_income_detail_list_model)
    def post(self):
        """
        查询整体收入每日趋势
        整体销售收入，同比，日期
        """
        resp_dict = CrmTotalDailyIncomeDetailController.crm_service.get_crm_total_daily_income_detail_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/TotalMonthlyIncomeDetail')
class CrmTotalMonthlyIncomeDetailController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_total_monthly_income_detail_list_model)
    def post(self):
        """
        查询整体收入每月趋势
        整体销售收入，同比，月份
        """
        resp_dict = CrmTotalMonthlyIncomeDetailController.crm_service\
            .get_crm_total_monthly_income_detail_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/MemberNowBeforeIncomeReport')
class CrmMemberNowBeforeIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_member_nowbefore_income_report_list_model)
    def post(self):
        """
        查询会员收入分析
        会员，当月会员，当年会员，往年会员
        """
        resp_dict = CrmMemberNowBeforeIncomeReportController\
            .crm_service.get_crm_member_now_before_income_report_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/MemberNewOldIncomeReport')
class CrmMemberNewOldIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_member_newold_income_report_list_model)
    def post(self):
        """
        查询新老会员收入分析
        会员，新会员，老会员
        """
        resp_dict = CrmMemberNewOldIncomeReportController.crm_service\
            .get_crm_member_new_old_income_report_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/MemberLevelIncomeReport')
class CrmMemberLevelIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_member_level_income_report_list_model)
    def post(self):
        """
        查询会员等级收入分析
        会员，普通会员，VIP会员
        """
        resp_dict = CrmMemberLevelIncomeReportController.crm_service\
            .get_crm_member_level_income_report_data(ns_2.payload)
        
        return resp_dict


@ns_2.route('/MemberMulDimIncomeReport')
class CrmMemberMulDimIncomeReportController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_2.expect(dto.crm_member_analyse_req_dto_model, validate=True)
    @ns_2.marshal_with(po.crm_member_muldim_income_report_list_model)
    def post(self):
        """
        查询多维度收入分析
        新会员: {普通会员, VIP会员} 老会员:{普通会员, VIP会员}
        """
        resp_dict = CrmMemberMulDimIncomeReportController.crm_service\
            .get_crm_member_mul_dim_income_report_data(ns_2.payload)
        
        return resp_dict


@ns_3.route('/MemberAmountDetail')
class CrmMemberAmountDetailController(Resource):
    
    crm_service = CrmServiceImpl()
    
    @ns_3.expect(dto.crm_member_analyse_req_dto_model)
    @ns_3.marshal_with(po.crm_member_amount_detail_list_model)
    def post(self):
        """
        查询会员计数详情
        当前全部会员，有消费会员，未消费会员
        """
        resp_dict = CrmMemberAmountDetailController.crm_service.get_crm_member_amount_detail(ns_3.payload)
        
        return resp_dict