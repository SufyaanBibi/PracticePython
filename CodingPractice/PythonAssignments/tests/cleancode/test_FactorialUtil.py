import unittest
from CodingPractice.PythonAssignments.cleancode.MathsUtils import factorial_util


class TestFactorialUtil(unittest.TestCase):

    def test_00_factorial_5(self):
        expected = 120
        actual = factorial_util(5)
        self.assertEqual(expected, actual)

    def test_01_factorial_0(self):
        expected = 1
        actual = factorial_util(0)
        self.assertEqual(expected, actual)

    def test_02_factorial_20(self):
        expected = 2432902008176640000
        actual = factorial_util(20)
        self.assertEqual(expected, actual)

    def test_03_factorial_1(self):
        expected = 1
        actual = factorial_util(1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
