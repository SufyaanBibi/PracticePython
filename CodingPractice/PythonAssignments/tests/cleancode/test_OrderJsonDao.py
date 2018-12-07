import unittest
from CodingPractice.PythonAssignments.cleancode.OrderAndOrderlineDao import *


class TestOrderJsonDao(unittest.TestCase):

    def test_00_get_orders(self):
        o = OrderJsonDao()
        e = o.get_orders()
        self.assertEqual(4, len(e))

    def test_01_get_order_by_order_id(self):
        order_lines = OrderLineDto(7, 3, 10)
        order = OrderDto(7, 103, "2018-12-01 10:45:15", [order_lines])
        o = OrderJsonDao()
        e = o.get_order_by_order_id(7)
        self.assertEqual(order, e)

    def test_02_get_multiple_orders_by_cust_id(self):
        order_lines_1 = OrderLineDto(1, 1, 1)
        order_lines_2 = OrderLineDto(1, 2, 3)
        order_1 = OrderDto(1, 101, "2018-11-25 11:45:15", [order_lines_1, order_lines_2])
        order_lines_3 = OrderLineDto(2, 1, 1)
        order_lines_4 = OrderLineDto(2, 2, 3)
        order_2 = OrderDto(2, 101, "2018-11-30 11:45:15", [order_lines_3, order_lines_4])
        o = OrderJsonDao()
        e = o.get_orders_by_customer_id(101)
        self.assertEqual([order_1, order_2], e)

    def test_03_get_single_order_by_cust_id(self):
        order_lines = OrderLineDto(7, 3, 10)
        order = OrderDto(7, 103, "2018-12-01 10:45:15", [order_lines])
        o = OrderJsonDao()
        e = o.get_orders_by_customer_id(103)
        self.assertEqual([order], e)

    def test_03_get_order_by_product_id(self):
        order_lines = OrderLineDto(7, 3, 10)
        order = OrderDto(7, 103, "2018-12-01 10:45:15", [order_lines])
        o = OrderJsonDao()
        e = o.get_orders_by_product_id(3)
        self.assertEqual([order], e)

    def test_04_get_multiple_orders_by_product_id(self):
        order_lines_1 = OrderLineDto(1, 1, 1)
        order_lines_2 = OrderLineDto(1, 2, 3)
        order_1 = OrderDto(1, 101, "2018-11-25 11:45:15", [order_lines_1, order_lines_2])
        order_lines_3 = OrderLineDto(2, 1, 1)
        order_lines_4 = OrderLineDto(2, 2, 3)
        order_2 = OrderDto(2, 101, "2018-11-30 11:45:15", [order_lines_3, order_lines_4])
        o = OrderJsonDao()
        e = o.get_orders_by_product_id(1)
        self.assertEqual([order_1, order_2], e)

    def test_05_order_id_does_not_exist(self):
        o = OrderJsonDao()
        e = o.get_order_by_order_id(9000)
        self.assertEqual(None, e)

    def test_06_customer_id_does_not_exist(self):
        o = OrderJsonDao()
        e = o.get_orders_by_customer_id(9000)
        self.assertEqual(None, e)


if __name__ == '__main__':
    unittest.main()
