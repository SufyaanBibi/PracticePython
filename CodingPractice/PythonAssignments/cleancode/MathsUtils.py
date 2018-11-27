
def factorial_util(n):

    facto = 1
    for x in range(1, n+1):
        facto = facto*x

    return facto


def positive_numbers(list_of_numbers):
    return [n for n in list_of_numbers if n > 0]


def all_numbers_greater_than(num, list_of_numbers):
    return all(n > num for n in list_of_numbers)


def get_even_num_sum(list_of_numbers):
    return sum(list_of_numbers[0::2])
