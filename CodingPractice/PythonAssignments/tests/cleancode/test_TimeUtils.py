import unittest
from CodingPractice.PythonAssignments.cleancode.TimeUtils import *


class TimeUtilsTests(unittest.TestCase):

    def test_00_get_date_time_function(self):
        expected = datetime(2018, 11, 14, 11, 42, 00)
        actual = get_date_time('2018/11/14 11:42:00')
        self.assertEqual(expected, actual)

    def test_01_hours_between_two_times(self):
        start = '2018/11/13 11:42:01'
        end = '2018/11/14 12:42:01'
        self.assertEqual(25, hours_between_util(start, end))

    def test_02_hours_between_two_times_on_different_days(self):
        start = '2018/11/13 11:42:01'
        end = '2018/11/14 11:42:01'
        self.assertEqual(24, hours_between_util(start, end))

    def test_03_hours_between_two_times(self):
        start = '2018/11/13 11:42:01'
        end = '2018/11/13 12:42:01'
        self.assertEqual(1, hours_between_util(start, end))

    def test_04_no_hour_passed(self):
        start = '2018/11/13 11:00:00'
        end = '2018/11/13 11:42:01'
        self.assertEqual(0, hours_between_util(start, end))

    def test_05_end_before_start(self):
        start = '2018/11/14 11:42:01'
        end = '2018/11/13 11:42:01'
        self.assertEqual(-24, hours_between_util(start, end))

    def test_06_seconds_between(self):
        start = '2018/11/13 11:00:00'
        end = '2018/11/13 11:00:05'
        self.assertEqual(5, seconds_between_util(start, end))

    def test_07_seconds_between(self):
        start = '2018/11/13 11:00:00'
        end = '2018/11/14 11:00:05'
        self.assertEqual(86405, seconds_between_util(start, end))

    def test_08_seconds_end_before_start(self):
        start = '2018/11/14 11:00:05'
        end = '2018/11/13 11:00:00'
        self.assertEqual(-86405, seconds_between_util(start, end))


if __name__ == '__main__':
    unittest.main()
