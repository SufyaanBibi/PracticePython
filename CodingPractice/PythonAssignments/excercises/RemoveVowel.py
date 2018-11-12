

def remove_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word.split()
    abbreviation = []
    for w in word[0]:
        abbreviation.append(w)
    for w in word[1:]:
        if w not in vowels:
            abbreviation.append(w)
    return ''.join(abbreviation)
