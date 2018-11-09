from abc import ABCMeta, abstractmethod


class RecruitAnalyseService:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_recruit_amount_report_data(self, dto):
        """
        查询招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_store_recruit_amount_report_data(self, dto):
        """
        查询门店招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_amount_daily_detail_data(self, dto):
        """
        查询每天招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_store_recruit_amount_daily_detail_data(self, dto):
        """
        查询门店每天招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_amount_monthly_detail_data(self, dto):
        """
        查询每月招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_store_recruit_amount_monthly_detail_data(self, dto):
        """
        查询门店每月招募会员数，有消费会员数，未消费会员数
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询有消费会员每日详情
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_consumed_amount_monthly_detail_data(self, dto):
        """
        查询有消费会员每月详情
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_store_recruit_consumed_amount_daily_detail_data(self, dto):
        """
        查询门店有消费会员每日详情
        :param dto:
        :return:
        """

    @abstractmethod
    def get_store_recruit_consumed_amount_monthly_detail_data(self, dto):
        """
        查询门店有消费会员每月详情
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_unconsumed_amount_daily_detail_data(self, dto):
        """
        查询未消费会员每日详情
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_recruit_unconsumed_amount_monthly_detail_data(self, dto):
        """
        查询未消费会员每月详情
        :param dto:
        :return:
        """

    @abstractmethod
    def get_store_recruit_unconsumed_amount_daily_detail_data(self, dto):
        """
        查询门店未消费会员每日详情
        :param dto:
        :return:
        """
        pass

    @abstractmethod
    def get_store_recruit_unconsumed_amount_monthly_detail_data(self, dto):
        """
        查询门店未消费会员每月详情
        :param dto:
        :return:
        """
        pass
