from abc import ABCMeta, abstractmethod


class IncomeAnalyseService:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_total_income_report_data(self, dto):
        """
        查询整体收入分析
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_total_income_report_data(self, dto):
        """
        查询门店整体收入分析
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_total_daily_income_detail_data(self, dto):
        """
        查询整体收入每日趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_total_daily_income_detail_data(self, dto):
        """
        查询门店整体收入每日趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_total_monthly_income_detail_data(self, dto):
        """
        查询整体收入每月趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_total_monthly_income_detail_data(self, dto):
        """
        查询门店整体收入每月趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_now_before_income_report_data(self, dto):
        """
        查询会员，当月，当年，往年收入分析
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_now_before_income_report_data(self, dto):
        """
        查询门店会员，当月，当年，往年收入分析
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_new_old_income_report_data(self, dto):
        """
        查询新老会员收入分析
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_new_old_income_report_data(self, dto):
        """
        查询门店新老会员收入分析
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_new_old_daily_income_detail_data(self, dto):
        """
        查询新老会员每日收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_new_old_daily_income_detail_data(self, dto):
        """
        查询门店新老会员每日收入趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_new_old_monthly_income_detail_data(self, dto):
        """
        查询新老会员每月收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_new_old_monthly_income_detail_data(self, dto):
        """
        查询门店新老会员每月收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_level_income_report_data(self, dto):
        """
        查询会员等级收入分析
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_level_income_report_data(self, dto):
        """
        查询门店会员等级收入分析
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_level_daily_income_detail_data(self, dto):
        """
        查询会员等级每日收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_level_daily_income_detail_data(self, dto):
        """
        查询门店会员等级每日收入趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_level_monthly_income_detail_data(self, dto):
        """
        查询会员等级每月收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_level_monthly_income_detail_data(self, dto):
        """
        查询门店会员等级每月收入趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_mul_dim_income_report_data(self, dto):
        """
        查询多维度收入分析
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_mul_dim_income_report_data(self, dto):
        """
        查询门店多维度收入分析
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_mul_dim_daily_income_detail_data(self, dto):
        """
        查询多维度每日收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_mul_dim_daily_income_detail_data(self, dto):
        """
        查询门店多维度每日收入趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_mul_dim_monthly_income_detail_data(self, dto):
        """
        查询多维度每月收入趋势
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_mul_dim_monthly_income_detail_data(self, dto):
        """
        查询门店多维度每月收入趋势
        :param dto: member_analyse.store.dto
        :return:
        """
        pass

    @abstractmethod
    def get_member_register_proportion_report_data(self, dto):
        """
        查询登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass

    @abstractmethod
    def get_store_member_register_proportion_report_data(self, dto):
        """
        查询门店登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass


    @abstractmethod
    def get_member_daily_register_proportion_detail_data(self, dto):
        """
        查询每日登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass


    @abstractmethod
    def get_store_member_daily_register_proportion_detail_data(self, dto):
        """
        查询门店每日登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass


    @abstractmethod
    def get_member_monthly_register_proportion_detail_data(self, dto):
        """
        查询每月登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass


    @abstractmethod
    def get_store_member_monthly_register_proportion_detail_data(self, dto):
        """
        查询门店每月登记率
        :param dto: member_analyse.zone.dto
        :return:
        """
        pass


