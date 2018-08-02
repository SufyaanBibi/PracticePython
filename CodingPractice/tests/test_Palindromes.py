import unittest
from CodingPractice.excercises.Palindromes import palindrome_sniffer


class IsPalindromeTests(unittest.TestCase):

    def test_is_palindrome(self):
        user_input = 'hannah'
        self.assertTrue(palindrome_sniffer(user_input))

    def test_not_palindrome(self):
        user_input = 'morgan'
        self.assertFalse(palindrome_sniffer(user_input))


if __name__ == '__main__':
    unittest.main()
