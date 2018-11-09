import re

get_day_pattern = re.compile('[0-9]{2,}')


def number_of_days_between(start_date_str, end_date_str):
    '''This function takes two date strings and works out the
    number of days between the two dates'''
    start_day = get_day_pattern.findall(start_date_str)
    end_day = get_day_pattern.findall(end_date_str)

    s = int(start_day[2])
    e = int(end_day[2])

    diff = e - s
    print(diff)
    return diff