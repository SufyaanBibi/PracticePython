
def list_overlap(a, b):
    c = []
    for element in a:
        if element in b and element not in c:
            c.append(element)
    return c


def using_language_1(a, b):
    c = set()
    for element in a:
        if element in b:
            c.add(element)
    return c


def using_sets(a,b):
    set_a = set(a)
    set_b = set(b)
    return set_a.intersection(set_b)


def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    return set_a.difference(set_b)


def union(a,b):
    set_a = set(a)
    set_b = set(b)
    return set_a.union(set_b)
