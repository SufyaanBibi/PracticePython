import unittest
from CodingPractice.PythonAssignments.shoppingcart.dao.json.OrderJsonDao import *


class TestOrderJsonDao(unittest.TestCase):
    
    def setUp(self):
        import os
        dirname = os.path.dirname(__file__)
        fp = os.path.join(dirname, '../../resources/orders.json')
        self._orderDao = OrderJsonDao(fp)

    def test_00_get_orders(self):
        
        e = self._orderDao.get_orders()
        self.assertEqual(6, len(e))

    def test_01_get_order_by_order_id(self):
        order_lines = OrderLineDto(order_id=7, product_id=3, qty=10)
        order = OrderDto(order_id=7, customer_id=103, order_timestamp="2018-12-01 10:45:15",
                         postage=1, order_lines=[order_lines])
        e = self._orderDao.get_order_by_order_id(7)
        self.assertEqual(order, e)

    def test_02_get_multiple_orders_by_cust_id(self):
        order_lines_1 = OrderLineDto(order_id=1, product_id=1, qty=1)
        order_lines_2 = OrderLineDto(order_id=1, product_id=2, qty=3)
        order_1 = OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                           postage=1, order_lines=[order_lines_1, order_lines_2])
        order_lines_3 = OrderLineDto(order_id=2, product_id=1, qty=1)
        order_lines_4 = OrderLineDto(order_id=2, product_id=2, qty=3)
        order_2 = OrderDto(order_id=2, customer_id=101, order_timestamp="2018-11-30 11:45:15",
                           postage=2, order_lines=[order_lines_3, order_lines_4])
        
        e = self._orderDao.get_orders_by_customer_id(101)
        self.assertEqual([order_1, order_2], e)

    def test_03_get_single_order_by_cust_id(self):
        order_lines = OrderLineDto(order_id=7, product_id=3, qty=10)
        order = OrderDto(order_id=7, customer_id=103, order_timestamp="2018-12-01 10:45:15",
                         postage=1, order_lines=[order_lines])
        
        e = self._orderDao.get_orders_by_customer_id(103)
        self.assertEqual([order], e)

    def test_04_get_order_by_product_id(self):
        order_lines = OrderLineDto(order_id=7, product_id=3, qty=10)
        order = OrderDto(order_id=7, customer_id=103, order_timestamp="2018-12-01 10:45:15",
                         postage=1, order_lines=[order_lines])
        e = self._orderDao.get_orders_by_product_id(3)
        self.assertEqual([order], e)

    def test_05_get_multiple_orders_by_product_id(self):
        order_lines_1 = OrderLineDto(order_id=1, product_id=1, qty=1)
        order_lines_2 = OrderLineDto(order_id=1, product_id=2, qty=3)
        order_1 = OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                           postage=1, order_lines=[order_lines_1, order_lines_2])
        order_lines_3 = OrderLineDto(order_id=2, product_id=1, qty=1)
        order_lines_4 = OrderLineDto(order_id=2, product_id=2, qty=3)
        order_2 = OrderDto(order_id=2, customer_id=101, order_timestamp="2018-11-30 11:45:15",
                           postage=2, order_lines=[order_lines_3, order_lines_4])
        e = self._orderDao.get_orders_by_product_id(1)
        self.assertEqual([order_1, order_2], e)

    def test_06_order_id_does_not_exist(self):
        e = self._orderDao.get_order_by_order_id(9000)
        self.assertEqual(None, e)

    def test_07_customer_id_does_not_exist(self):
        e = self._orderDao.get_orders_by_customer_id(9000)
        self.assertEqual(None, e)

    def test_08_MethodNotImplementedException_raised_on_create_order(self):
        with self.assertRaises(MethodNotImplementedException) as e:
            self._orderDao.create_order(None)
        self.assertEqual('create_order called on OrderJsonDao', e.exception._message)

    def test_09_MethodNotImplementedException_raised_on_delete_order(self):
        with self.assertRaises(MethodNotImplementedException) as e:
            self._orderDao.delete_order(None)
        self.assertEqual('delete_order called on OrderJsonDao', e.exception._message)

    def test_10_MethodNotImplementedException_raised_on_update_order(self):
        with self.assertRaises(MethodNotImplementedException) as e:
            self._orderDao.update_order(None, None)
        self.assertEqual('update_order called on OrderJsonDao', e.exception._message)


if __name__ == '__main__':
    unittest.main()
