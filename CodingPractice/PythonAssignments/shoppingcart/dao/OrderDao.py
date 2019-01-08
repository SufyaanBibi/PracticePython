from abc import ABC, abstractmethod


class OrderDao(ABC):

    @abstractmethod
    def get_orders(self):
        return

    @abstractmethod
    def get_order_by_order_id(self, order_id):
        return

    @abstractmethod
    def get_orders_by_customer_id(self, cust_id):
        return

    @abstractmethod
    def get_orders_by_product_id(self, product_id):
        return
