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
