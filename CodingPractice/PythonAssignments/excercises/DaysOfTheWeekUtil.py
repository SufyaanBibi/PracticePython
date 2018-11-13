from datetime import datetime


def number_of_weekdays_between(start_date_str, end_date_str):
    s_year, s_month, s_day = start_date_str.split('/')
    e_year, e_month, e_day = end_date_str.split('/')
    start_date = datetime(int(s_year), int(s_month), int(s_day))
    end_date = datetime(int(e_year), int(e_month), int(e_day))

    difference = end_date - start_date

    