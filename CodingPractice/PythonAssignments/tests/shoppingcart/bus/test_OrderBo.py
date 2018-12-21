import unittest
from CodingPractice.PythonAssignments.shoppingcart.bus.OrderBo import OrderBo, OrderIdNonexistent, VatNegative
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

    def test_08_get_orders_by_month(self):
        pass

    def test_09_get_order_total_by_month(self):
        pass
