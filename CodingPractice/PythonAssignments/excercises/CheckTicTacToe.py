
def row_win(board):
    for r in [set(row) for row in board]:
        if r == set({1}):
            return 'Player 1 wins!'
        elif r == set({2}):
            return 'Player 2 wins!'


def column_win(board):
    columns = zip(*board)
    for c in [set(column) for column in columns]:
        if c == set({1}):
            return 'Player 1 wins!'
        elif c == set({2}):
            return 'Player 2 wins!'


def diagonals_win(board):
    diag_1 = set([board[0][0], board[1][1], board[2][2]])
    diag_2 = set([board[0][2], board[1][1], board[2][0]])
    if diag_1 == set({1}) or diag_2 == set({1}):
        return 'Player 1 wins!'
    elif diag_1 == set({2}) or diag_2 == set({2}):
        return 'Player 2 wins!'
