def reverse_order(l):
    if l is None:
        return None
    lst = l.split()
    lst.reverse()
    s = ' '
    return s.join(lst)

