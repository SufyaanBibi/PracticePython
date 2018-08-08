
def horizontal_lines(board_size):
    if board_size is None:
        return None
    return '\n' + ' ---' * board_size


def vertical_lines(board_size):
    if board_size is None:
        return None
    return '|   ' * (board_size + 1)


def draw_a_line(board_size):
    return horizontal_lines(board_size) + '\n' + vertical_lines(board_size)


def draw_a_board(bs):
    board = ''
    for i in range(bs):
        board += draw_a_line(bs)
    board += horizontal_lines(bs)
    return board

