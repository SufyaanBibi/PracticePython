from CodingPractice.PythonAssignments.excercises.OddorEven import is_even


def finding_less_than(list_of_numbers, number):
    lower_numbers = []
    for item in list_of_numbers:
        if item < number:
            lower_numbers.append(item)
        else:
            continue
    return lower_numbers


def list_comp(list_of_numbers, number):
    return [item for item in list_of_numbers if item < number]


def multi_by_ten(n):
    return n * 10


l = [0, 1, 2, 5, 10, 21]
print([multi_by_ten(n)
       for n in l
       if is_even(n)
       ])


print(list(filter(is_even, l)))

f = lambda e : e % 2 != 0

a = [e for e in l if ( f(e) )]
print(a)
