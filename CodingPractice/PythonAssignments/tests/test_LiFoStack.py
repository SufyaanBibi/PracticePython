import unittest
from CodingPractice.PythonAssignments.excercises.LiFoStack import LiFoStack


class TestLiFoStack(unittest.TestCase):

    def test_00_push_test(self):
        a = LiFoStack()
        a.push(1)
        self.assertEqual([1], a)

    def test_01_pop_test(self):
        a = LiFoStack()
        a.push(1)
        a.push(2)
        a.push(3)
        self.assertEqual(3, a.pop())

    def test_02_peek_test(self):
        a = LiFoStack()
        a.push(1)
        a.push(2)
        self.assertEqual(2, a.peek())


if __name__ == '__main__':
    unittest.main()
