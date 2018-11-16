import unittest
from CodingPractice.PythonAssignments.excercises.FiFoQueue import FiFoQ


class TestFiFoQueue(unittest.TestCase):

    def test_00_construct_list(self):
        a = FiFoQ()
        a.enqueue(1)
        a.enqueue(2)
        self.assertEqual([1, 2], a)

    def test_01_dequeue(self):
        a = FiFoQ()
        a.enqueue(1)
        a.enqueue(2)
        self.assertEqual(1, a.dequeue())

    def test_02_exception_raised_when_off_queue(self):
        a = FiFoQ()
        with self.assertRaises(IndexError):
            a.dequeue()


if __name__ == '__main__':
    unittest.main()
