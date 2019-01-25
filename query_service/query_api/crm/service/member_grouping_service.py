from abc import ABCMeta, abstractmethod


class MemberGroupingService:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_member_grouping_list(self, dto):
        """
        查询会员分组列表
        :param dto: member_grouping.dto
        :return:
        """
        pass
