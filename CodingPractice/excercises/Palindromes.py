
def palindrome_sniffer(user_input):
    word = str(user_input)
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    else:
        return False
