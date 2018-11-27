
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


def has_lower_case(string):
    return any(s.islower() for s in string)


def first_and_last_letter(string):
    return [word[0] + word[-1] for word in string.split()]


def is_even_index_position(string):
    a = []
    for l in string:
        if string.index(l) % 2 == 0:
            a.append(l)
    return ''.join(a)