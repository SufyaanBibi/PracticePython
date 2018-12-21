import unittest
from CodingPractice.PythonAssignments.shoppingcart.bus.OrderBo import OrderBo
from CodingPractice.PythonAssignments.shoppingcart.dao.OrderJsonDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.ProductJsonDao import *


class TestOrderBo(unittest.TestCase):

    def test_00_order_bo_instantiates(self):
        pass

    def test_01_get_order_total_by_order_id(self):
        a = OrderBo(OrderJsonDao(), ProductJsonDao())
        self.assertEqual(1621.2, a.get_order_total_by_order_id(7, 20))

    def test_02_get_order_total_by_cust_id(self):
        pass

    def test_03_get_orders_by_month(self):
        pass

    def test_04_get_order_total_by_month(self):
        pass
