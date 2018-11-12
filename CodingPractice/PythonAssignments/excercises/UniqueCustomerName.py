
def unique_customer_name(name_list):
    unique_first_names = [name[0] for name in name_list]
    upper_case_first_names = [upper.upper() for upper in unique_first_names]
    first_names_set = set(upper_case_first_names)
    return len(first_names_set)
