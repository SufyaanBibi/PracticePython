import unittest
from CodingPractice.excercises.OddorEven import is_even


class IsEvenTests(unittest.TestCase):

    def test_two_is_even(self):
        self.assertEqual(True, is_even(2))

    def test_three_is_not_even(self):
        self.assertEqual(False, is_even(3))

    def test_zero(self):
        self.assertEqual(True, is_even(0))

    def test_negative_two(self):
        self.assertEqual(True, is_even(-2))

    def test_negative_zero(self):
        self.assertEqual(True, is_even(-0))


if __name__ == '__main__':
    unittest.main()
