from excercises.PracticePython_Hangman import is_letter
from excercises.PracticePython_PickWord import random_word
from excercises.PracticePython_GuessLetters import matching_letter, is_game_over

print('Welcome to Hangman! You have 15 attempts to guess the word.')

while True:

    comp_word = random_word()
    lst = list('_' * len(comp_word))
    guessed_letters = []
    print(' '.join(lst))
    count = 0

    while True:
        user_letter = input('\nInsert your letter here: ').upper()

        if user_letter == 'EXIT':
            break

        if user_letter not in guessed_letters and user_letter not in comp_word:
            count += 1

        guessed_letters.append(user_letter)
        guessed_letters = sorted(guessed_letters)

        print('\nHere are your guessed letters:', ' '.join(guessed_letters))
        print('You have guessed', count, 'time(s)!')

        if count == 15:
            print('Game over!')
            break

        if not is_letter(user_letter):
            print('This is not a letter. Try again!')

        matching_letter(comp_word, user_letter, lst)
        print(' '.join(lst))

        if is_game_over(lst, comp_word):
            print('Well done! Game over!')
            break

    print('\nYour word was', comp_word, '!')
    user_choice = input('\nWould you like to play again? Y/N: ').upper()

    if user_choice == 'Y':
        continue
    else:
        break
