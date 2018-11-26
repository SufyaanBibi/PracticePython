import unittest
from CodingPractice.PythonAssignments.cleancode.StringUtils import first_and_last_letter


class TestFirstAndLastLetter(unittest.TestCase):

    def test_00_first_and_last_letter(self):
        e = first_and_last_letter('The quick brown fox jumped over the lazy dog')
        self.assertEqual(['Te', 'qk', 'bn', 'fx', 'jd', 'or', 'te', 'ly', 'dg'], e)

    def test_01_one_word(self):
        e = first_and_last_letter('dog')
        self.assertEqual(['dg'], e)


if __name__ == '__main__':
    unittest.main()
