from CodingPractice.excercises.GameBoard import horizontal_lines, vertical_lines

board_size = int(input('Enter board size here: '))

for element in range(board_size):
    print(horizontal_lines(board_size))
    print(vertical_lines(board_size))


print (horizontal_lines(board_size))
