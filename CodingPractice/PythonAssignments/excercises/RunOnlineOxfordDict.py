from CodingPractice.PythonAssignments.excercises.WordDictionary import OxfordDictionary


while True:

    user_word = input('Please enter the word you wish to define. Type Q to exit. > ')

    if user_word == 'Q':
        break

    definition = OxfordDictionary()

    print(definition.look_up(user_word))
