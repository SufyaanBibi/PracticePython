def second_largest_element(list_of_numbers):
    if list_of_numbers is None:
        return None

    elif list_of_numbers == []:
        return None

    large_element = max(list_of_numbers[0], list_of_numbers[1])
    second_largest_element= min(list_of_numbers[0], list_of_numbers[1])

    for element in list_of_numbers:
        if element > large_element:
            second_largest_element = large_element
            large_element = element

        elif second_largest_element < element and element < large_element:
            second_largest_element = element


    return second_largest_element


