import unittest
from CodingPractice.OOPPractice.assignments.ImmutableDict import ImmutableDict


class TestImmutableDict(unittest.TestCase):

    def test_01_check_dict_works(self):

        im = ImmutableDict([('a', 1), ('b', 2)])

        self.assertEqual({'a': 1, 'b': 2}, im)

    def test_02_check_dict_is_immutable(self):

        im = ImmutableDict([('a', 1), ('b', 2)])

        im['z'] = 100

        with self.assertRaises(KeyError):
            im['z']

    def test_03_check_set_item_does_not_work(self):

        im = ImmutableDict([('a', 1), ('b', 2)])

        im['a'] = 3

        self.assertEqual({'a': 1, 'b': 2}, im)

    def test_04_check_del_does_not_work(self):

        im = ImmutableDict([('a', 1), ('b', 2)])

        del im['a']

        self.assertEqual({'a': 1, 'b': 2}, im)


if __name__ == '__main__':
    unittest.main()

