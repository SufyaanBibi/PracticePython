import unittest
from CodingPractice.PythonAssignments.cleancode.StringUtils import sorted_string


class TestSortedString(unittest.TestCase):

    def test_00_sorted_string(self):
        self.assertEqual('abzAX', sorted_string('aXzAb'))

    def test_01_empty_string(self):
        self.assertEqual('', sorted_string(''))

    def test_02_string_with_numbers(self):
        self.assertEqual('123abzAX', sorted_string('a1bz3AX2'))


if __name__ == '__main__':
    unittest.main()
