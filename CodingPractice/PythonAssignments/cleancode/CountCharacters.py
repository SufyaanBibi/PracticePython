
def count_characters(letter, string):
    count = 0

    s = string.lower()

    for l in s:
        if l == letter:
            count += 1

    return count
