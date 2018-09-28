import unittest

from CodingPractice.PythonAssignments.cleancode.CountItemsInList import list_length


class CountItemsInListTests(unittest.TestCase):

    def test_return_zero_for_empty_list(self):
        self.assertEqual(0, list_length([]))

    def test_non_empty_list(self):
        self.assertEqual(6, list_length([0, 1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
