import unittest
from CodingPractice.OOPPractice.assignments.ImmutableDict import ChattyDict
from CodingPractice.OOPPractice.assignments.CustomException import SetAttributeError, DeleteAttributeError


class TestChattyDictionary(unittest.TestCase):

    def test_00_test_construction(self):
        im = ChattyDict([('a', 1), ('b', 2)])
        self.assertEqual({'a': 1, 'b': 2}, im)

    def test_01_chatty_dict_set_item_test(self):
        im = ChattyDict([('a', 1), ('b', 2)])
        with self.assertRaises(SetAttributeError):
            im['z'] = 100

    def test_02_chatty_dict_del_item_test(self):
        im = ChattyDict([('a', 1), ('b', 2)])
        with self.assertRaises(DeleteAttributeError):
            del im['a']


if __name__ == '__main__':
    unittest.main()
