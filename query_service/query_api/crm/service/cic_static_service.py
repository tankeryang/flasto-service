from abc import ABCMeta, abstractclassmethod


class CicStaticService:
    
    __metaclass__ = ABCMeta
    
    @abstractclassmethod
    def get_cic_static_detail_data(self, dto):
        """
        获取cic首页静态显示数据
        :param dto:
        :return:
        """
        pass
