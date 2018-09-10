import unittest
from CodingPractice.OOPPractice.assignments.WrappedSet import *


class TestWrappedSet(unittest.TestCase):

    def show_function_passing(self):

        def mult_5(e):
            return e % 5 == 0

        def odd(e):
            return e % 2 != 0

        def take_both( a, b, element ):
            return a(element) and b(element)

        def make_f():
            def x(n):
                n % 2 == 0
            return x

    def test_even_number_filter_condition(self):
        def is_even(e):
            return e % 2 == 0

        a = WrappedSet(is_even)

        a.put(2)

        self.assertEqual({2}, a.get())

    def test_odd_number_filter_condition(self):
        def is_odd(e):
            return e % 2 != 0

        a = WrappedSet(is_odd)

        a.put(3)

        self.assertEqual({3}, a.get())

    def test_assert_false_odd_number_filter_condition(self):
        def is_odd(e):
            return e % 2 != 0

        a = WrappedSet(is_odd)

        a.put(4)

        self.assertEqual(set(), a.get())

    def test_multiple_of_five(self):
        def multiple_of_five(e):
            return e % 5 == 0

        a = WrappedSet(multiple_of_five)

        a.put(10)

        self.assertEqual({10}, a.get())


if __name__ == '__main__':
    unittest.main()
