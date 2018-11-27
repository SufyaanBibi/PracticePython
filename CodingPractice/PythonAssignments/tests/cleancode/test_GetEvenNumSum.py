import unittest
from CodingPractice.PythonAssignments.cleancode.MathsUtils import get_even_num_sum


class TestGetEvenNumberSum(unittest.TestCase):

    def test_00_even_number_sum(self):
        self.assertEqual(9, get_even_num_sum([1, 2, 3, 4, 5]))

    def test_01_empty_list(self):
        self.assertEqual(0, get_even_num_sum([]))

    def test_02_one_element(self):
        self.assertEqual(1, get_even_num_sum([1]))


if __name__ == '__main__':
    unittest.main()
