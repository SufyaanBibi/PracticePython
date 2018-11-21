
def factorial_util(n):

    facto = 1
    for x in range(1, n+1):
        facto = facto*x

    return facto


def positive_numbers(list_of_numbers):
    return [n for n in list_of_numbers if n > 0]
