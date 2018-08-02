
def horizontal_lines(board_size):
    if board_size is None:
        return None
    return ' --- ' * board_size


def vertical_lines(board_size):
    if board_size is None:
        return None
    return '|    ' * (board_size + 1)

