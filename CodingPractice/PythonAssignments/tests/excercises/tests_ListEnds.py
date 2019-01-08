import unittest
from CodingPractice.PythonAssignments.excercises.ListEnds import *


class HeadsAndTails(unittest.TestCase):

    def test_heads_and_tails_numbers(self):
        l = [5, 10, 15, 20, 25]
        expected_result = [5, 25]
        self.assertEqual(expected_result, head_and_tail_of_list(l))

    def test_heads_and_tails_words(self):
        l = ['cat', 'dog', 'bird', 'fish']
        expected_result = ['cat', 'fish']
        self.assertEqual(expected_result, head_and_tail_of_list(l))

    def test_slice_first_element(self):
        n = [5, 10, 15, 20, 25]
        expected_result = 5
        self.assertEqual(expected_result, first_element_alone(n))

    def test_return_all_elements_but_first(self):
        e = [5, 10, 15, 20, 25]
        expected_result = [10, 15, 20, 25]
        self.assertEqual(expected_result, slice_elements(e))


if __name__ == '__main__':
    unittest.main()
