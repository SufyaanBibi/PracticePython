def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    for element in range(5, n):
        if n % element == 0:
            return False

    return True
