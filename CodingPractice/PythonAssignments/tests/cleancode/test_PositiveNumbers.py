import unittest
from CodingPractice.PythonAssignments.cleancode.MathsUtils import positive_numbers


class TestPositiveNumbers(unittest.TestCase):

    def test_00_positive_numbers(self):
        expected = [1, 2, 3, 4, 5]
        actual = positive_numbers([-2, -1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)

    def test_01_no_numbers(self):
        expected = []
        actual = positive_numbers([])
        self.assertEqual(expected, actual)

    def test_02_all_negative(self):
        expected = []
        actual = positive_numbers([-1, -2, -10, -20, -45])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
