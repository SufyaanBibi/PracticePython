import unittest
from CodingPractice.OOPPractice.assignments.MaxList import MaxSizeList


class TestMaxListClass(unittest.TestCase):

    def test_list_three_elements(self):
        a = MaxSizeList(3)
        a.push('Hey')
        a.push('hi')
        a.push('you')
        a.push('guys')
        self.assertEqual(['hi', 'you', 'guys'], a.get_list())

    def test_list_one_element(self):
        b = MaxSizeList(1)
        b.push('Hey')
        b.push('hi')
        b.push('you')
        self.assertEqual(['you'], b.get_list())

    def test_copy_is_made(self):
        a = MaxSizeList(1)
        a.push('hello')

        b = a.get_list()
        b.append('world')

        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
