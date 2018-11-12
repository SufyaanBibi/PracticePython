import unittest
from CodingPractice.PythonAssignments.excercises.RemoveVowels import remove_vowels


class RemoveVowelTest(unittest.TestCase):

    def test_00_remove_vowels_from_word_starting_with_consonant(self):
        word = 'Constantinople'
        self.assertEqual('Cnstntnpl', remove_vowels(word))

    def test_01_remove_vowels_from_word_starting_with_vowel(self):
        word = 'abacus'
        self.assertEqual('abcs', remove_vowels(word))


if __name__ == '__main__':
    unittest.main()
