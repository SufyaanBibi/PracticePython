from excercises.PracticePython_GuessLetters import matching_letter, is_game_over

comp_word = 'EVAPORATE'
lst = list('_' * len(comp_word))

while True:
    user_letter = input('Insert your letter here: ').upper()
    matching_letter(comp_word, user_letter, lst)

    print(' '.join(lst))

    if is_game_over(lst, comp_word):
        print('Game Over')
        break
