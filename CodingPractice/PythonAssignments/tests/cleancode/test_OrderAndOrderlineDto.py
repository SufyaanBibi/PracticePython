import unittest
from CodingPractice.PythonAssignments.cleancode.OrderAndOrderlineDto import *


class OrderDtoTest(unittest.TestCase):

    def test_00_construct_OrderDto(self):
        a = OrderLinesDto(1, 2, 3)
        b = OrderDto(1, 101, "2018-11-25 11:45:15", a)
        self.assertEqual(1, b.get_order_id())

    def test_01_equality_operator(self):
        a = OrderLinesDto(1, 2, 3)
        b = OrderDto(1, 101, "2018-11-25 11:45:15", a)
        c = OrderLinesDto(1, 2, 3)
        d = OrderDto(1, 101, "2018-11-25 11:45:15", c)
        self.assertEqual(b, d)

    def test_02_getter_functions_order_lines_dto(self):
        a = OrderLinesDto(1, 2, 3)
        self.assertEqual(1, a.get_order_id())
        self.assertEqual(2, a.get_product_id())
        self.assertEqual(3, a.get_qty())


if __name__ == '__main__':
    unittest.main()
