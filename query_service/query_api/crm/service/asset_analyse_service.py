from abc import ABCMeta, abstractclassmethod


class AssetAnalyseService:
    
    __metaclass__ = ABCMeta
    
    @abstractclassmethod
    def get_member_amount_report_data(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_amount_report_data(self, dto):
        """
        查询门店当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_new_old_amount_report_data(self, dto):
        """
        查询新老会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_new_old_amount_report_data(self, dto):
        """
        查询门店新老会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_level_amount_report_data(self, dto):
        """
        查询会员等级数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_level_amount_report_data(self, dto):
        """
        查询门店会员等级数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_remain_amount_report_data(self, dto):
        """
        查询会员留存数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_remain_amount_report_data(self, dto):
        """
        查询门店会员留存数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_active_amount_report_data(self, dto):
        """
        查询活跃会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_active_amount_report_data(self, dto):
        """
        查询门店活跃会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_frequency_amount_report_data(self, dto):
        """
        查询累计消费频次会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_frequency_amount_report_data(self, dto):
        """
        查询门店累计消费频次会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_recency_amount_report_data(self, dto):
        """
        查询最近一次消费会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_recency_amount_report_data(self, dto):
        """
        查询门店最近一次消费会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_monetary_amount_report_data(self, dto):
        """
        查询累计消费金额会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_monetary_amount_report_data(self, dto):
        """
        查询门店累计消费金额会员数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_time_amount_report_data(self, dto):
        """
        查询入会时长会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_time_amount_report_data(self, dto):
        """
        查询门店入会时长会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_discount_amount_report_data(self, dto):
        """
        查询折扣率会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_discount_amount_report_data(self, dto):
        """
        查询门店折扣率会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_member_sipo_amount_report_data(self, dto):
        """
        查询客单价会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_sipo_amount_report_data(self, dto):
        """
        查询门店客单价会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_recruit_amount_report_data(self, dto):
        """
        查询招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_recruit_amount_report_data(self, dto):
        """
        查询门店招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_recruit_amount_daily_detail_data(self, dto):
        """
        查询每天招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_recruit_amount_daily_detail_data(self, dto):
        """
        查询门店每天招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_recruit_amount_monthly_detail_data(self, dto):
        """
        查询每月招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_recruit_amount_monthly_detail_data(self, dto):
        """
        查询门店每月招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询有消费会员每日详情
        :param dto:
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询门店有消费会员每日详情
        :param dto:
        :return:
        """
