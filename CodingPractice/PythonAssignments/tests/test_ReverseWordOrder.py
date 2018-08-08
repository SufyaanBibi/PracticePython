import unittest
from CodingPractice.PythonAssignments.excercises.ReverseWordOrder import reverse_order


class TestReverseWordOrder(unittest.TestCase):

    def test_reverse_string(self):
        l = 'My name is Sufyaan.'
        expected_result = 'Sufyaan. is name My'
        self.assertEqual(expected_result, reverse_order(l))

    def test_none(self):
        l = None
        expected_result = None
        self.assertEqual(expected_result, reverse_order(l))

    def test_single_word(self):
        l = 'Sufi'
        expected_result = 'Sufi'
        self.assertEqual(expected_result, reverse_order(l))


if __name__ == '__main__':
    unittest.main()