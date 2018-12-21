import unittest
from CodingPractice.PythonAssignments.shoppingcart.bus.OrderBo import OrderBo, OrderIdNonexistent
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

    def test_03_vat_is_zero(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1351.0, a.get_order_total_by_order_id(7, 0))

    def test_04_order_id_does_not_exist(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        with self.assertRaises(OrderIdNonexistent) as e:
            a.get_order_total_by_order_id(19, 20)
        self.assertEqual('Order ID 19 does not exist.', e.exception.message)

    def test_02_get_order_total_by_cust_id(self):
        pass

    def test_03_get_orders_by_month(self):
        pass

    def test_04_get_order_total_by_month(self):
        pass
