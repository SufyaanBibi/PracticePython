lst_of_numbers = range(1, 201)

for element in lst_of_numbers:
    if element % 3 == 0 and element % 5 == 0:
        print('fizz buzz')
    elif element % 3 == 0:
        print('fizz')
    elif element % 5 == 0:
        print('buzz')
    else:
        print(element)
