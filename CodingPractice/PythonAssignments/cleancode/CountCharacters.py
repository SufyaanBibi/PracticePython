
def count_characters(letter, string):
    ll = letter.lower()
    return len([a for a in string.lower() if a == ll])
