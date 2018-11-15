import unittest
from CodingPractice.PythonAssignments.cleancode.AllNumbersGreaterThanUtil import *


class GreaterThanNumberUtilTest(unittest.TestCase):

    def test_00_all_numbers_greater_than(self):
        self.assertTrue(all_numbers_greater_than(15, [16, 17, 99]))

    def test_01_not_all_numbers_greater_than(self):
        self.assertFalse(all_numbers_greater_than(17, [16, 17, 99]))

    def test_02_not_all_numbers_greater_than(self):
        self.assertFalse(all_numbers_greater_than(16, [17, 16, 99]))


if __name__ == '__main__':
    unittest.main()
