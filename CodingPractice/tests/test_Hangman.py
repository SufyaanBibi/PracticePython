import unittest
from CodingPractice.excercises.Hangman import is_letter


class HangmanTests(unittest.TestCase):

    def test_is_letter(self):
        user_letter = 'A'
        self.assertTrue(is_letter(user_letter))

    def test_is_number(self):
        user_letter = '1'
        self.assertFalse(is_letter(user_letter))

    def test_is_lower_letter(self):
        user_letter = 'b'
        self.assertFalse(is_letter(user_letter))


if __name__ == '__main__':
    unittest.main()
