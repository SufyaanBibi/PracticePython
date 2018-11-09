import unittest

from CodingPractice.PythonAssignments.cleancode.DateUtils import *


class DateCalculatorTests(unittest.TestCase):

    def test_number_of_datys_between(self):
        start = "2018/11/09"
        end = "2018/11/30"
        self.assertEqual( 21, number_of_days_between(start, end))


if __name__ == '__main__':
    unittest.main()