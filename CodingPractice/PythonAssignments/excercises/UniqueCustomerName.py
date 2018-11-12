
def unique_customer_name(name_list):
    unique_first_names = [name[0] for name in name_list]
    first_names_set = set(unique_first_names)
    return len(first_names_set)
