
def set_removal(n):
    s = set(n)
    return s


def for_loop_removal(n):
    newlist = []
    for element in n:
        if element not in newlist:
            newlist.append(element)
    return newlist
