import unittest
from CodingPractice.excercises.SecondLargestNumber import second_largest_element


class SecondLargestElementTests(unittest.TestCase):

    def test_second_largest_element(self):
        list_of_numbers = [1, 3, 5, 9, 3, 8]
        self.assertEqual(8, second_largest_element(list_of_numbers))

    def test_negative_list(self):
        list_of_numbers = [-1, -3, -5, -9, - 3, -8]
        self.assertEqual(-3, second_largest_element(list_of_numbers))

    def test_one_one(self):
        list_of_numbers = [1, 1]
        self.assertEqual(1, second_largest_element(list_of_numbers))

    def test_empty_list(self):
        list_of_numbers = []
        self.assertEqual(None, second_largest_element(list_of_numbers))

    def test_None(self):
        list_of_numbers = None
        self.assertEqual(None, second_largest_element(list_of_numbers))


if __name__ == '__main__':
    unittest.main()
