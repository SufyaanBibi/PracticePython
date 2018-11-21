import unittest
from CodingPractice.PythonAssignments.cleancode.CountCharacters import count_characters


class TestCountCharacters(unittest.TestCase):

    def test_00_count_letter_a(self):
        expected = 10
        actual = count_characters('a', 'This is the string we need to count letter a. An amorous Aardvark '
                                       'attempted an act of ardour.')
        self.assertEqual(expected, actual)

    def test_01_count_letter_b(self):
        expected = 1
        actual = count_characters('b', 'abc')
        self.assertEqual(expected, actual)

    def test_02_no_letters(self):
        expected = 0
        actual = count_characters('a', 'bcd')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
