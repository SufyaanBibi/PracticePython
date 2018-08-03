import unittest
from CodingPractice.excercises.GameBoard import horizontal_lines, vertical_lines


class GameBoardTests(unittest.TestCase):

    def test_horizontal_lines(self):
        board_size = 1
        expected_result = ' --- '
        self.assertEqual(expected_result, horizontal_lines(board_size))

    def test_vertical_lines(self):
        board_size = 1
        expected_result = '|    |    '
        self.assertEqual(expected_result, vertical_lines(board_size))

    def test_none_vertical_lines(self):
        board_size = None
        self.assertEqual(None, vertical_lines(board_size))

    def test_none_horizontal_lines(self):
        board_size = None
        self.assertEqual(None, horizontal_lines(board_size))

    def test_three_horizontal_lines(self):
        board_size = 3
        expected_result = ' ---  ---  --- '
        self.assertEqual(expected_result, horizontal_lines(board_size))

    def test_three_vertical_lines(self):
        board_size = 3
        expected_result = '|    |    |    |    '
        self.assertEqual(expected_result, vertical_lines(board_size))


if __name__ == '__main__':
    unittest.main()
