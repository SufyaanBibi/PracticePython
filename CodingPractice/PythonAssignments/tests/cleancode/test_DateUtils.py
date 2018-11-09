import unittest
from CodingPractice.PythonAssignments.cleancode.DateUtils import *


class DateCalculatorTests(unittest.TestCase):

    def test_00_number_of_days_between(self):
        start = '2018/11/09'
        end = '2018/11/30'
        self.assertEqual(21, number_of_days_between(start, end))

    def test_01_num_of_days_between(self):
        start = "1999/11/09"
        end = "2018/11/30"
        self.assertEqual(6961, number_of_days_between(start, end))


if __name__ == '__main__':
    unittest.main()
