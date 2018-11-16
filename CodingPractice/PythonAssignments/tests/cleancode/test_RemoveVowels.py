import unittest
from CodingPractice.PythonAssignments.cleancode.RemoveVowels import remove_vowels


class RemoveVowelTest(unittest.TestCase):

    def test_00_remove_vowels_from_word_starting_with_consonant(self):
        word = 'Constantinople'
        self.assertEqual('Cnstntnpl', remove_vowels(word))

    def test_01_remove_vowels_from_word_starting_with_vowel(self):
        word = 'abacus'
        self.assertEqual('abcs', remove_vowels(word))

    def test_02_no_vowels_in_word(self):
        word = 'fry'
        self.assertEqual('fry', remove_vowels(word))

    def test_03_all_vowel_word(self):
        word = 'EUOUAE'
        self.assertEqual('E', remove_vowels(word))


if __name__ == '__main__':
    unittest.main()
