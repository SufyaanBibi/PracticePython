import unittest

from CodingPractice.PythonAssignments.cleancode.CountItemsInList import count_items_in_list


class CountItemsInListTests(unittest.TestCase):

    def test_return_zero_for_empty_list(self):
        self.assertEqual(0, count_items_in_list([]))

    def test_non_empty_list(self):
        self.assertEqual(5, count_items_in_list([0, 1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
