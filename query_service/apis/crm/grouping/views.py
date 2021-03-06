from flask import current_app
from flask_restplus import Resource, Namespace

ns = Namespace('CRM 会员分组', path='/crm/grouping', description='会员分组api')

from .models import qo, ro
from .service import GroupingService
from .utils.validator import (
    MemberGroupingDetailQOValidator,
    MemberGroupingCommonQOValidator,
)

from query_service.apis.utils.decorator import authorized


@ns.route('/MemberGroupingDetail')
class MemberGroupingDetailView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_grouping_detail_qo)
    @ns.marshal_with(ro.member_grouping_detail_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询分组会员详情
        :return:
        """
        res, err = MemberGroupingDetailQOValidator().load(ns.payload)
        
        if err:
            current_app.logger.error("Err" + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return GroupingService.get_member_grouping_detail(res)


@ns.route('/MemberGroupingCount')
class MemberGroupingCountView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_grouping_common_qo)
    @ns.marshal_with(ro.member_grouping_count_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询分组会员总数
        :return:
        """
        res, err = MemberGroupingCommonQOValidator().load(ns.payload)
        
        if err:
            current_app.logger.error("Err" + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return GroupingService.get_member_grouping_count(res)


@ns.route('/MemberGroupingCsv')
class MemberGroupingCsvView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_grouping_common_qo)
    @ns.marshal_with(ro.member_grouping_csv_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        导出分组会员详情csv
        :return:
        """
        res, err = MemberGroupingCommonQOValidator().load(ns.payload)
        
        if err:
            current_app.logger.error("Err" + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return GroupingService.get_member_grouping_detail_csv(res)


@ns.route('/MemberGroupingNoList')
class MemberGroupingNoListView(Resource):
    
    @ns.doc(security='key')
    @ns.expect(qo.member_grouping_common_qo)
    @ns.marshal_with(ro.member_grouping_no_list_ro)
    @ns.response(401, "Token authorized error")
    @ns.response(404, "Not Found")
    @authorized
    def post(self):
        """
        查询分组会员编号列表
        :return:
        """
        res, err = MemberGroupingCommonQOValidator().load(ns.payload)
    
        if err:
            current_app.logger.error("Err" + str(err))
            return dict(success=False, message=err)
        else:
            current_app.logger.info("Param: " + str(res))
            return GroupingService.get_member_grouping_no_list(res)
