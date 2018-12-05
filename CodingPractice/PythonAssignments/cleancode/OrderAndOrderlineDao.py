from abc import ABC, abstractmethod
import json
from CodingPractice.PythonAssignments.cleancode.OrderAndOrderlineDto import OrderDto, OrderLinesDto


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


class OrderJsonDao(OrderDao):

    @staticmethod
    def _get_file_path(fn):
        import os
        return os.path.join(os.path.dirname(__file__), fn)

    @staticmethod
    def _get_json(file_name):
        fn = OrderJsonDao._get_file_path(file_name)
        with open(fn, 'r') as f:
            return json.load(f)

    @staticmethod
    def _create_order(o):
        return OrderDto(o["order_id"], o["customer_id"], o["order_timestamp"], o["order_lines"])

    @staticmethod
    def make_orders_from_json(j):
        orders = []
        for order in j["order_lines"]:
            orders.append(OrderJsonDao._create_order(order))
        return orders

    def get_orders(self):
        jf = OrderJsonDao._get_json('orders.json')
        return OrderJsonDao.make_orders_from_json(jf)

    def get_order_by_order_id(self, order_id):
        orders = self.get_orders()
        return [order for order in orders if order_id == order.get_order_id()][0]

    def get_orders_by_customer_id(self, cust_id):
        return

    def get_orders_by_product_id(self, product_id):
        return
