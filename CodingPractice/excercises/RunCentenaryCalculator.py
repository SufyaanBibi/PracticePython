from excercises.PracticePython_CharacterInput import centenary_calculator

user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
current_year = int(input('What is the year? '))

centenary_year = centenary_calculator(user_age, current_year)

print('Hello', user_name, 'you will turn 100 in the year', centenary_year, '.')
