import unittest
from CodingPractice.excercises.CharacterInput import centenary_calculator


class CharacterInputTests(unittest.TestCase):

    def test_for_newborn(self):
        self.assertEqual(2118, centenary_calculator(0, 2018))

    def test_for_basil(self):
        self.assertEqual(2063, centenary_calculator(54, 2018))

    def test_for_sufi(self):
        self.assertEqual(2095, centenary_calculator(22, 2018))

    def test_for_julia(self):
        self.assertEqual(2062, centenary_calculator(55, 2018))


if __name__ == '__main__':
    unittest.main()
