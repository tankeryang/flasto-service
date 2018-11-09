from abc import ABCMeta, abstractmethod


class CicStaticService:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_cic_static_detail_data(self, dto):
        """
        获取cic首页静态显示数据
        :param dto:
        :return:
        """
        pass
