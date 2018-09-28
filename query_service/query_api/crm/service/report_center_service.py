from abc import ABCMeta, abstractclassmethod


class ReportCenterService:
    
    __metaclass__ = ABCMeta
    
    @abstractclassmethod
    def get_daily_report_data(self, dto):
        """
        日报查询
        :param dto: restplus.Api.payload
        :return:
        """
        pass
