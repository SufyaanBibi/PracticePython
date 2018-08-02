import unittest
from CodingPractice.excercises.ListOverlap \
    import list_overlap, using_language_1, using_sets, difference, union

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

expected_result = [1, 2, 3, 5, 8, 13]

result = {21, 34, 55, 89}

set_result = set(expected_result)

set_union = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 89, 34, 55}


class ListOverlap(unittest.TestCase):

    def test_hand_rolled_code(self):
        self.assertEqual(expected_result, list_overlap(a, b))

    def test_using_language_sets(self):
        self.assertEqual(set_result, using_language_1(a, b))

    def test_using_itersection(self):
        self.assertEqual(set_result, using_sets(a, b))

    def test_difference(self):
        self.assertEqual(result, difference(a, b))

    def test_union(self):
        self.assertEqual(set_union, union(a,b))


if __name__ == '__main__':
    unittest.main()
