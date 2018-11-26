import unittest
from CodingPractice.PythonAssignments.cleancode.StringUtils import is_lower_case


class TestAllLowerCase(unittest.TestCase):

    def test_00_is_lower(self):
        self.assertTrue(is_lower_case('ABcdE'))

    def test_01_is_not_lower(self):
        self.assertFalse(is_lower_case('ABCDE'))

    def test_02_empty_string(self):
        self.assertFalse(is_lower_case(''))


if __name__ == '__main__':
    unittest.main()
