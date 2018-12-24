import unittest
from CodingPractice.PythonAssignments.excercises.RemovingDuplicates import set_removal, for_loop_removal


class DuplicateRemovalTests(unittest.TestCase):

    def test_set_removal_test(self):
        duplicated_numbers = [1, 2, 3, 4, 5, 5, 6, 4, 2]
        expected_result = {1, 2, 3, 4, 5, 6}
        self.assertEqual(expected_result, set_removal(duplicated_numbers))

    def test_for_loop_removal_tests(self):
        duplicated_numbers = [1, 2, 3, 4, 5, 5, 6, 4, 2]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected_result, for_loop_removal(duplicated_numbers))


if __name__ == '__main__':
    unittest.main()
