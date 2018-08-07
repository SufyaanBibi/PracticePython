import random


def get_file_path(file_name):
    import os
    return os.path.join(os.path.dirname(__file__), file_name)


def get_sowpods():
    sp = get_file_path('sowpods.txt')
    with open(sp, 'r') as fh:
        return [word.strip() for word in fh.readlines()]


def random_word():
    words = get_sowpods()
    return random.choice(words)
