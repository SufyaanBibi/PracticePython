import unittest
from CodingPractice.OOPPractice.assignments.BoundedSet import *


class TestBoundedSet(unittest.TestCase):

    def test_set_boundries(self):
        a = BoundedSet(1, 10)
        a.put(3)
        a.get()
        self.assertEqual({3}, a.get())

    def test_boundries_fail(self):
        b = BoundedSet(1, 10)
        b.put(11)
        self.assertTrue('Number is out of bounds.', b)


if __name__ == '__main__':
    unittest.main()
