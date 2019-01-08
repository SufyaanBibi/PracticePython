from CodingPractice.PythonAssignments.shoppingcart.dao.JsonFileReader import JsonFileReader
from CodingPractice.PythonAssignments.shoppingcart.dao.OrderDao import OrderDao
from CodingPractice.PythonAssignments.shoppingcart.domain.OrderDto import OrderDto, OrderLineDto


class OrderJsonDao(OrderDao, JsonFileReader):

    @staticmethod
    def _create_order_line(order_line):
        return OrderLineDto(order_line["order_id"], order_line["product_id"], order_line["qty"])

    @staticmethod
    def _create_order(order, order_lines):
        return OrderDto(order["order_id"], order["customer_id"], order["order_timestamp"], order["postage_class"],
                        order_lines)

    @staticmethod
    def _make_orders_from_json(j):
        orders = []
        for order in j["orders"]:
            order_lines = []
            for order_line in order["order_lines"]:
                order_lines.append(OrderJsonDao._create_order_line(order_line))
            orders.append(OrderJsonDao._create_order(order, order_lines))
        return orders

    def __init__(self, json_file_path):
        self._json_file_path = json_file_path

    def get_orders(self):
        jf = OrderJsonDao._get_json(self._json_file_path)
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
