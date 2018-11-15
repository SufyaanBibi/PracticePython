from datetime import datetime


def datetime_days(date_str):
    year, month, day = date_str.split('/')
    return datetime(int(year), int(month), int(day))


def number_of_days_between(start_date_str, end_date_str):
    start_date = datetime_days(start_date_str)
    end_date = datetime_days(end_date_str)

    difference = end_date - start_date

    return difference.days


def weekdays_in_range(start_date_str, end_date_str):
    difference = number_of_days_between(start_date_str, end_date_str)
    isoweek_days = [1, 2, 3, 4, 5, 6, 7]

    num_of_weeks = difference // 7
    num_of_extra_days = difference % 7
    days_list = isoweek_days * num_of_weeks

    extra_days = list(range(1, num_of_extra_days+1))
    days_list.extend(extra_days)

    days_without_weekends = [d for d in days_list
                             if d != 6 and d != 7]

    return len(days_without_weekends)
