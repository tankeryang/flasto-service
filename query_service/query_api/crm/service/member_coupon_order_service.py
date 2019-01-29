from abc import ABCMeta, abstractmethod


class MemberCouponOrderService:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_member_coupon_order_data(self, dto):
        """
        查询会员-券-订单关联数据
        :param dto: member_coupon_order.dto
        :return:
        """
        pass
    
    
    @abstractmethod
    def export_member_coupon_order_data_csv(self, dto):
        """
        导出会员-券-订单关联数据
        :param dto: member_coupon_order
        :return:
        """
        pass
    
    
    @abstractmethod
    def get_coupon_denomination_sum(self, dto):
        """
        查询订单使用现金券总面额
        :param dto:
        :return:
        """
        pass
