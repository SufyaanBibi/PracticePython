import unittest
from CodingPractice.OOPPractice.assignments.BoundedSet import *


class TestBoundedSet(unittest.TestCase):

    def test_set_boundries(self):
        a = BoundedSet(1, 10)
        a.put(3)
        self.assertEqual({3}, a.get())

    def test_out_of_bounds(self):
        a = BoundedSet(1, 10)
        a.put(0)
        self.assertEqual(set(), a.get())

    def test_equal_to_bound(self):
        a = BoundedSet(1, 10)
        a.put(1)
        self.assertEqual({1}, a.get())

    def test_filter_condition(self):
        a = BoundedSet(1, 10)
        self.assertTrue(a.filter_condition(5))

    def test_false_filter_condition(self):
        a = BoundedSet(1, 10)
        self.assertFalse(a.filter_condition(15))


if __name__ == '__main__':
    unittest.main()
