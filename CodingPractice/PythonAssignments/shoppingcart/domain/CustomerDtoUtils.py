from operator import attrgetter


def sort_customers_by_last_name(list_of_cust):
    return sorted(list_of_cust, key=attrgetter('_last_name', '_first_name'))
