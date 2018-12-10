from CodingPractice.PythonAssignments.shoppingcart.OrderDao import OrderDao
from CodingPractice.PythonAssignments.shoppingcart.OrderDto import OrderDto, OrderLineDto
import json


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
    def _create_order_line(order_line):
        return OrderLineDto(order_line["order_id"], order_line["product_id"], order_line["qty"])

    @staticmethod
    def _create_order(order, order_lines):
        return OrderDto(order["order_id"], order["customer_id"], order["order_timestamp"], order_lines)

    @staticmethod
    def _make_orders_from_json(j):
        orders = []
        for order in j["orders"]:
            order_lines = []
            for order_line in order["order_lines"]:
                order_lines.append(OrderJsonDao._create_order_line(order_line))
            orders.append(OrderJsonDao._create_order(order, order_lines))
        return orders

    def get_orders(self):
        jf = OrderJsonDao._get_json('orders.json')
        return OrderJsonDao._make_orders_from_json(jf)

    def get_order_by_order_id(self, order_id):
        orders = self.get_orders()
        odr = [order for order in orders if order_id == order.get_order_id()]
        if odr:
            return odr[0]

    def get_orders_by_customer_id(self, cust_id):
        orders = self.get_orders()
        odr = [order for order in orders if cust_id == order.get_customer_id()]
        if odr:
            return odr

    def get_orders_by_product_id(self, product_id):
        orders = self.get_orders()
        return [order for order in orders
                for order_line in order.get_order_lines()
                if product_id == order_line.get_product_id()]
