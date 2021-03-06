import unittest
from CodingPractice.PythonAssignments.cleancode.StringUtils import get_even_index_position


class TestIsEvenIndex(unittest.TestCase):

    def test_00_is_even(self):
        self.assertEqual('aceg', get_even_index_position('abcdefg'))

    def test_01_empty_string(self):
        self.assertEqual('', get_even_index_position(''))


if __name__ == '__main__':
    unittest.main()
