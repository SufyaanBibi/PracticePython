from excercises.PracticePython_RockPaperScissors import rock_paper_scissors, result_of_rps, is_valid_input

print('Welcome to Rock Paper Scissors, Sufyaan and Basil!')

player_1 = input('So, rock, paper or scissors? ')
player_2 = input('And you? Rock, paper or scissors? ')

if( is_valid_input(player_1, player_2)) :
    result = rock_paper_scissors(player_1, player_2)

    if result is None:
        print("It's a draw!")
    elif result == "Invalid input.":
        print(result)
    elif result:
        print('Player 1 won!')
    else:
        print('Player 2 won!')
else:
    print('Invalid input.')
