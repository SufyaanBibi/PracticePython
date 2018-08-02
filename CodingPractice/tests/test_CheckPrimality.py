import unittest
from CodingPractice.excercises.CheckPrimality import *


class IsPrimeTests(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(11))

    def test_is_two(self):
        self.assertTrue(is_prime(2))

    def test_is_three(self):
        self.assertTrue(is_prime(3))

    def test_is_div_by_two(self):
        self.assertFalse(is_prime(4))

    def test_is_not_prime(self):
        self.assertFalse(is_prime(42))

    def test_big_number(self):
        self.assertTrue(is_prime(16769023))

    def test_1298074214633706835075030044377088(self):
        self.assertFalse(is_prime(1298074214633706835075030044377088))

    @unittest.skip("Runs for over a minute")
    def test_1073676287(self):
        self.assertTrue(is_prime(1073676287))


if __name__ == '__main__':
    unittest.main()
