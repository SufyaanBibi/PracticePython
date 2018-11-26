
def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    abbreviation = []
    abbreviation.append(word[0])
    for w in word[1:]:
        if w not in vowels:
            abbreviation.append(w)
    return ''.join(abbreviation)


def num_of_strings_greater_than_n(n, list_of_str):
    return len([s for s in list_of_str if len(s) > n])


def all_lower_case(string):
    return any(s.islower() for s in string)
