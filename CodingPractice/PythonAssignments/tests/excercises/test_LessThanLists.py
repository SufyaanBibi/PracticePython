import unittest
from CodingPractice.PythonAssignments.excercises.LessThanLists import finding_less_than, list_comp


class LessThanTests(unittest.TestCase):

    def test_for_positive_numbers(self):
        list_of_numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(expected_result, finding_less_than(list_of_numbers, 5))

    def test_for_negative_numbers(self):
        list_of_numbers = [-5, -3, -10, -8]
        expected_result = [-5, -10, -8]
        self.assertEqual(expected_result, finding_less_than(list_of_numbers, -4))

    def test_list_comp_on_positive_numbers(self):
        list_of_numbers = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4]
        self.assertEqual(expected_result, list_comp(list_of_numbers, 5))

    def test_list_comp_on_negative_numbers(self):
        list_of_numbers = [-5, -3, -10, -8]
        expected_result = [-5, -10, -8]
        self.assertEqual(expected_result, list_comp(list_of_numbers, -4))


if __name__ == '__main__':
    unittest.main()
