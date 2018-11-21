
def count_characters(letter, string):
    return len([a for a in string.lower() if a == letter.lower()])
