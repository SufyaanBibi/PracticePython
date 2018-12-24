import unittest
from CodingPractice.PythonAssignments.excercises.CheckTicTacToe \
    import row_win, column_win, diagonals_win


class CheckTicTacToeTests(unittest.TestCase):

    def test_player_1_row_win(self):
        board = [[1, 1, 1],
                 [2, 2, 0],
                 [2, 1, 1]]
        self.assertEqual('Player 1 wins!', row_win(board))

    def test_player_1_column_win(self):
        board = [[1, 0, 2],
                 [1, 2, 0],
                 [1, 0, 2]]
        self.assertEqual('Player 1 wins!', column_win(board))

    def test_player_2_row_win(self):
        board = [[2, 2, 2],
                 [1, 2, 0],
                 [1, 0, 2]]
        self.assertEqual('Player 2 wins!', row_win(board))

    def test_player_2_column_win(self):
        board = [[1, 2, 0],
                 [1, 2, 1],
                 [0, 2, 1]]
        self.assertEqual('Player 2 wins!', column_win(board))

    def test_diagonal_player_1_win(self):
        board = [[1, 2, 0],
                 [1, 1, 2],
                 [0, 2, 1]]
        self.assertEqual('Player 1 wins!', diagonals_win(board))

    def test_diagonal_player_2_win(self):
        board = [[2, 2, 0],
                 [1, 2, 1],
                 [0, 2, 2]]
        self.assertEqual('Player 2 wins!', diagonals_win(board))

    def test_no_row_win(self):
        board = [[2, 2, 0],
                 [1, 2, 1],
                 [0, 2, 2]]
        self.assertEqual(None, row_win(board))

    def test_no_column_win(self):
        board = [[2, 2, 0],
                 [1, 0, 1],
                 [0, 2, 2]]
        self.assertEqual(None, column_win(board))

    def test_no_diagonal_win(self):
        board = [[1, 0, 2],
                 [1, 2, 0],
                 [1, 0, 2]]
        self.assertEqual(None, diagonals_win(board))


if __name__ == '__main__':
    unittest.main()
