import unittest
from CodingPractice.excercises.ListComprehension import even_list_comp, odd_list_comp

list_of_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_expected_result = [4, 16, 36, 64, 100]

odd_expected_result = [1, 9, 25, 49, 81]


class ListComprehension(unittest.TestCase):

    def test_even_list_comp(self):
        self.assertEqual(even_expected_result, even_list_comp(list_of_numbers))

    def test_odd_list_comp(self):
        self.assertEqual(odd_expected_result, odd_list_comp(list_of_numbers))


if __name__ == '__main__':
    unittest.main()
