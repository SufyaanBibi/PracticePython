import unittest
from CodingPractice.PythonAssignments.cleancode.StringUtils import num_of_strings_greater_than_n


class TestNumOfStringsGreaterThanN(unittest.TestCase):

    def test_00_str_greater_than_three(self):
        expected = 2
        actual = num_of_strings_greater_than_n(3, ['abc', 'xyz', 'abacd', '1221'])
        self.assertEqual(expected, actual)

    def test_01_no_str_greater_than(self):
        expected = 0
        actual = num_of_strings_greater_than_n(3, ['ab', 'x', 'a', '12'])
        self.assertEqual(expected, actual)

    def test_02_empty_lst(self):
        expected = 0
        actual = num_of_strings_greater_than_n(2, [])
        self.assertEqual(expected, actual)

    def test_03_when_n_is_0(self):
        expected = 4
        actual = num_of_strings_greater_than_n(0, ['abc', 'xyz', 'abacd', '1221'])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
