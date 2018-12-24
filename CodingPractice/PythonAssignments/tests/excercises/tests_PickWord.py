import unittest
from CodingPractice.PythonAssignments.excercises.PickWord import random_word


def get_file_path(file_name):
    import os
    return os.path.join(os.path.dirname(__file__), file_name)


def get_sowpods():
    sp = get_file_path('sowpods.txt')
    with open(sp, 'r') as fh:
        return [word.strip() for word in fh.readlines()]


words = get_sowpods()


class TestPickRandomWord(unittest.TestCase):

    def test_one(self):
        rnd_w = random_word()
        self.assertTrue(rnd_w in words)


if __name__ == '__main__':
    unittest.main()
