from datetime import datetime


def number_of_days_between(start_date_str, end_date_str):
    s_year, s_month, s_day = start_date_str.split('/')
    e_year, e_month, e_day = end_date_str.split('/')
    start_date = datetime(int(s_year), int(s_month), int(s_day))
    end_date = datetime(int(e_year), int(e_month), int(e_day))

    difference = end_date - start_date

    return difference.days


def workdays_in_range(start_date_str, end_date_str):

    difference = number_of_days_between(start_date_str, end_date_str)

    weeks = difference / 7

    weekend_days = weeks * 2

    return difference - weekend_days
