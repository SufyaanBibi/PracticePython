import unittest
from CodingPractice.PythonAssignments.shoppingcart.domain.OrderDto import *


class OrderDtoTest(unittest.TestCase):

    def test_00_construct_OrderDto(self):
        a = OrderLineDto(order_id=1, product_id=2, qty=3)
        c = OrderLineDto(order_id=12, product_id=21, qty=34)
        b = OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                     postage=1, order_lines=[a, c])
        self.assertEqual(1, b.get_order_id())
        self.assertEqual(101, b.get_customer_id())
        self.assertEqual("2018-11-25 11:45:15", b.get_order_timestamp())
        self.assertEqual(1, b.get_postage())
        self.assertEqual([a, c], b.get_order_lines())

    def test_01_equality_operator(self):
        a = OrderLineDto(order_id=1, product_id=2, qty=3)
        c = OrderLineDto(order_id=1, product_id=2, qty=3)
        b = OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                     postage=1, order_lines=[a, c])
        d = OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                     postage=1, order_lines=[a, c])
        self.assertEqual(b, d)

    def test_02_getter_functions_order_lines_dto(self):
        a = OrderLineDto(order_id=1, product_id=2, qty=3)
        self.assertEqual(1, a.get_order_id())
        self.assertEqual(2, a.get_product_id())
        self.assertEqual(3, a.get_qty())


if __name__ == '__main__':
    unittest.main()
