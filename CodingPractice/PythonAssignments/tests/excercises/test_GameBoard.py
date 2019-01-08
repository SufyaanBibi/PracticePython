import unittest
from CodingPractice.PythonAssignments.excercises.GameBoard import horizontal_lines, vertical_lines, draw_a_line, draw_a_board


class GameBoardTests(unittest.TestCase):

    def test_horizontal_lines(self):
        board_size = 1
        expected_result = '\n ---'
        self.assertEqual(expected_result, horizontal_lines(board_size))

    def test_vertical_lines(self):
        board_size = 1
        expected_result = '|   |   '
        self.assertEqual(expected_result, vertical_lines(board_size))

    def test_none_vertical_lines(self):
        board_size = None
        self.assertEqual(None, vertical_lines(board_size))

    def test_none_horizontal_lines(self):
        board_size = None
        self.assertEqual(None, horizontal_lines(board_size))

    def test_draw_a_line(self):
        board_size = 3
        self.assertEqual(
'''
 --- --- ---
|   |   |   |   ''', draw_a_line(board_size))

    def test_three_board(self):
        board_size = 3
        self.assertEqual(
'''
 --- --- ---
|   |   |   |   
 --- --- ---
|   |   |   |   
 --- --- ---
|   |   |   |   
 --- --- ---''', draw_a_board(board_size))


if __name__ == '__main__':
    unittest.main()
