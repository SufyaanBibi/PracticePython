import random

comp_number = random.randint(1, 20)
user_number = 0

count = 0

while user_number != comp_number:

    user_number = input('Please enter number from 1 to 20 here: ')

    if user_number == 'exit':
        break

    user_number = float(user_number)

    count += 1

    if user_number < comp_number:
        print('You guessed too low.')
    elif user_number > comp_number:
        print('You guessed too high!')
    else:
        print('You got it! It only took you', count, 'tries!')
        break
