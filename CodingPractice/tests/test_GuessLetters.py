import unittest
from CodingPractice.excercises.GuessLetters import matching_letter, is_game_over


class LetterGuessTests(unittest.TestCase):

    def test_word_evaporate(self):
        comp_word = 'EVAPORATE'
        lst = list('_' * len(comp_word))
        matching_letter(comp_word, 'E', lst)
        expected_result = ['E', '_', '_', '_', '_', '_', '_', '_', 'E']
        self.assertTrue(expected_result == lst)

    def test_empty_letter(self):
        comp_word = 'RUN'
        lst = list('_' * len(comp_word))
        matching_letter(comp_word, '', lst)
        expected_result = ['_', '_', '_']
        self.assertTrue(expected_result == lst)              

    def test_is_over(self):
        comp_word = 'RUN'
        lst = 'RUN'
        self.assertTrue(is_game_over(comp_word, lst))

    def test_is_not_over(self):
        comp_word = 'RUN'
        lst = ['_', '_', '_']
        self.assertFalse(is_game_over(comp_word, lst))


if __name__ == '__main__':
    unittest.main()
