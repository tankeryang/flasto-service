from abc import ABCMeta, abstractclassmethod


class AssetAnalyseService:
    
    __metaclass__ = ABCMeta
    
    @abstractclassmethod
    def get_member_amount_detail(self, dto):
        """
        查询当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
    
    @abstractclassmethod
    def get_store_member_amount_detail(self, dto):
        """
        查询门店当前会员，有消费会员，未消费会员人数
        :param dto: restplus.Api.payload
        :return:
        """
        pass
