import unittest
from CodingPractice.PythonAssignments.cleancode.DateUtils import *


class DateCalculatorTests(unittest.TestCase):

    def test_00_number_of_days_between(self):
        start = '2018/11/09'
        end = '2018/11/30'
        self.assertEqual(21, number_of_days_between(start, end))

    def test_01_num_of_days_between_different_years(self):
        start = "1999/11/09"
        end = "2018/11/30"
        self.assertEqual(6961, number_of_days_between(start, end))

    def test_02_num_of_days_between_different_months(self):
        start = '1873/05/08'
        end = '2018/11/09'
        self.assertEqual(53145, number_of_days_between(start, end))

    def test_03_same_day(self):
        start = '2018/11/09'
        end = '2018/11/09'
        self.assertEqual(0, number_of_days_between(start, end))

    def test_04_past_day_count(self):
        start = '2018/12/25'
        end = '2018/11/09'
        self.assertEqual(-46, number_of_days_between(start, end))


if __name__ == '__main__':
    unittest.main()
