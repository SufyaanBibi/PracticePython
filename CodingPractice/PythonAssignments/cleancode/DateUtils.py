from datetime import datetime


def datetime_days(date_str):
    year, month, day = date_str.split('/')
    return datetime(int(year), int(month), int(day))


def number_of_days_between(start_date_str, end_date_str):
    start_date = datetime_days(start_date_str)
    end_date = datetime_days(end_date_str)

    difference = end_date - start_date

    return difference.days


def workdays_in_range(start_date_str, end_date_str):

    difference = number_of_days_between(start_date_str, end_date_str)

    start = datetime_days(start_date_str)
    end = datetime_days(end_date_str)

    s = start.weekday()
    e = end.weekday()

    if difference % 7 == 0:
        weeks = difference / 7
        weekend_days = weeks * 2
        return difference - weekend_days
    else:
        pass
