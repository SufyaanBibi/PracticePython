import unittest
from CodingPractice.PythonAssignments.cleancode.OrderAndOrderlineDao import *


class TestOrderJsonDao(unittest.TestCase):

    def test_00_get_orders(self):
        o = OrderJsonDao()
        e = o.get_orders()
        print(e)


if __name__ == '__main__':
    unittest.main()
