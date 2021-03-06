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

    def test_05_weekend_start(self):
        start = '2018/11/03'
        end = '2018/11/13'
        self.assertEqual(6, weekdays_in_range(start, end))

    def test_06_start_day_weekend_no_week_days(self):
        start = '2018/11/03'
        end = '2018/11/04'
        self.assertEqual(0, weekdays_in_range(start, end))

    def test_07_isoweekday_func(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = isoweek_day_list(1, 7)
        self.assertEqual(expected, actual)

    def test_08_isoweekday_func(self):
        expected = [6, 7, 1, 2, 3, 4, 5, 6, 7]
        actual = isoweek_day_list(6, 9)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
