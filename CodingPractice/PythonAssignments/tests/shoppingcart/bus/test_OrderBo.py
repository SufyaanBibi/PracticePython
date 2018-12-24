import unittest
from CodingPractice.PythonAssignments.shoppingcart.bus.OrderBo import OrderBo, OrderIdNonexistent, VatNegative, \
    InvalidMonth
from CodingPractice.PythonAssignments.shoppingcart.dao.OrderJsonDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.ProductJsonDao import *


class TestOrderBo(unittest.TestCase):

    def test_00_order_bo_instantiates(self):
        try:
            a = OrderBo(OrderJsonDao(), ProductJsonDao())
        except Exception:
            self.fail("Insantiation incorrectly raised exception")

    def test_01_get_order_total_by_order_id(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1621.2, a.get_order_total_by_order_id(7, 20))

    def test_02_get_multiple_order_total_by_id(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(204.23999999999998, a.get_order_total_by_order_id(5, 20))

    def test_03_order_id_does_not_exist(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        with self.assertRaises(OrderIdNonexistent) as e:
            a.get_order_total_by_order_id(19, 20)
        self.assertEqual('Order ID 19 does not exist.', e.exception.message)

    def test_04_no_order_lines(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(0, a.get_order_total_by_order_id(8, 20))

    def test_05_vat_is_zero(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1351.0, a.get_order_total_by_order_id(7, 0))

    def test_06_VAT_is_negative(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        with self.assertRaises(VatNegative) as e:
            a.get_order_total_by_order_id(8, -1)
        self.assertEqual('In order ID 8 invalid VAT passed: -1', e.exception.message)

    def test_07_get_order_total_by_cust_id(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1621.2, a.get_order_total_by_customer_id(103, 20))

    def test_08_cust_id_has_no_orders(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(0, a.get_order_total_by_customer_id(70, 20))

    def test_09_cust_has_no_order_lines(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(0, a.get_order_total_by_customer_id(120, 20))

    def test_10_VAT_is_zero(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1351.0, a.get_order_total_by_customer_id(103, 0))

    def test_11_VAT_is_negative(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        with self.assertRaises(VatNegative) as e:
            a.get_order_total_by_customer_id(103, -1)
        self.assertEqual('In customer ID 103 invalid VAT passed: -1', e.exception.message)

    def test_12_get_orders_by_month(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual([OrderDto(8, 120, '2018-06-25 10:55:10', [])], a.get_orders_by_month(6))

    def test_13_get_multiple_orders_by_month(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual([OrderDto(1, 101, "2018-11-25 11:45:15", [OrderLineDto(1, 1, 1),  OrderLineDto(1, 2, 3)]),
                          OrderDto(2, 101, "2018-11-30 11:45:15", [OrderLineDto(2, 1, 1), OrderLineDto(2, 2, 3)]),
                          OrderDto(5, 102, "2018-11-15 10:45:15", [OrderLineDto(5, 5, 1), OrderLineDto(5, 6, 1)])],
                         a.get_orders_by_month(11))

    def test_14_invalid_month(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        with self.assertRaises(InvalidMonth) as e:
            a.get_orders_by_month(45)
        self.assertEqual('Month number 45 is invalid.', e.exception.message)

    def test_15_no_orders_month(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual([], a.get_orders_by_month(1))

    def test_13_get_order_total_by_month(self):
        pass
