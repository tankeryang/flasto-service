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
