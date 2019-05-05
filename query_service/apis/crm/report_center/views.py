from flask import current_app
from flask_restplus import Resource, Namespace

ns = Namespace('CRM 报表中心', path='/crm/report', description='日报月报api')

from .models import qo, ro
from .service import ReportCenterService
from .utils.validator import (
    DailyReportQOValidator,
    MonthlyReportSalesQOValidator,
    MonthlyReportAssetQOValidator,
)

from query_service.apis.utils.decorator import authorized


@ns.route('/DailyReport')
class CrmDailyReportView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.daily_report_qo)
    @ns.marshal_with(ro.daily_report_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        日报查询
        全国，大区，城市，门店，公司
        """
        res, err = DailyReportQOValidator().load(ns.payload)
        
        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return ReportCenterService.get_daily_report_data(res)


@ns.route('/MonthlyReport/Sales')
class CrmMonthlyReportSalesView(Resource):

    @ns.doc(security='key')
    @ns.expect(qo.monthly_report_sales_qo)
    @ns.marshal_with(ro.monthly_report_sales_ro_list)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        月报-业绩查询
        """
        res, err = MonthlyReportSalesQOValidator().load(ns.payload)

        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return ReportCenterService.get_monthly_report_sales_data(res)


@ns.route('/MonthlyReport/Asset')
class CrmMonthlyReportAssetView(Resource):

    @ns.doc(security='key')
    @ns.expect(qo.monthly_report_asset_qo)
    @ns.marshal_with(ro.monthly_report_asset_ro_list)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        月报-会员资产查询
        """
        res, err = MonthlyReportAssetQOValidator().load(ns.payload)

        if err:
            current_app.logger.error("Err: " + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return ReportCenterService.get_monthly_report_asset_data(res)
