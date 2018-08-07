def matching_letter(comp_word, user_letter, lst):
    for i, e in enumerate(comp_word):
        if user_letter == e:
            lst[i] = e


def is_game_over(lst, comp_word):
    return ''.join(lst) == comp_word
