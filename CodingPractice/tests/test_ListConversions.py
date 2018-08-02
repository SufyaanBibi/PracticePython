import unittest
from CodingPractice.excercises.ListConversions import comprehension_conversion, map_conversion


a = ['1', '2', '3']

i = [1, 2, 3]


class TestListConversions(unittest.TestCase):

    def test_comprehension_conversion(self):
        self.assertEqual(i, comprehension_conversion(a))

    def test_map_conversion(self):
        self.assertEqual(i, map_conversion(a))


if __name__ == '__main__':
    unittest.main()