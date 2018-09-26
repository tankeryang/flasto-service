from abc import ABCMeta, abstractclassmethod


class CrmService:
    
    __metaclass__ = ABCMeta
    
    @abstractclassmethod
    def get_daily_report_data(self, dto):
        """
        日报查询
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_daily_report_excel(self, timestamp, dto):
        """
        日报excel导出
        :param timestamp: 当前查询时间
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def del_local_daily_report_excel(self, timestamp):
        """
        删除服务器上的excel文件
        :param timestamp: 生成时间
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_total_income_report_data(self, dto):
        """
        查询整体收入分析
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_total_daily_income_detail_data(self, dto):
        """
        查询整体收入每日趋势
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_total_monthly_income_detail_data(self, dto):
        """
        查询整体收入每月趋势
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_member_now_before_income_report_data(self, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_member_new_old_income_report_data(self, dto):
        """
        查询新老会员收入分析
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_member_level_income_report_data(self, dto):
        """
        查询会员等级收入分析
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_member_mul_dim_income_report_data(self, dto):
        """
        查询多维度收入分析
        :param dto:restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_crm_member_amount_detail(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
