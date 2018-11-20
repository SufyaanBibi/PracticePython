from datetime import datetime


def datetime_days(date_str):
    year, month, day = date_str.split('/')
    return datetime(int(year), int(month), int(day))


def isoweek_datetime(date):
    return datetime_days(date).isoweekday()


def isoweek_day_list(iso_weekday_num, num_of_days):
    min_day_num, max_day_num = 1, 7

    count = iso_weekday_num
    lst = [count]
    while True:
        count += 1
        if count > max_day_num:
            count = min_day_num
        lst.append(count)
        if len(lst) >= num_of_days:
            break

    return lst


def number_of_days_between(start_date_str, end_date_str):
    start_date = datetime_days(start_date_str)
    end_date = datetime_days(end_date_str)

    difference = end_date - start_date

    return difference.days


def weekdays_in_range(start_date_str, end_date_str):
    start_date = isoweek_datetime(start_date_str)
    difference = number_of_days_between(start_date_str, end_date_str)

    days_list = isoweek_day_list(start_date, difference)

    days_without_weekends = [d for d in days_list
                             if d != 6 and d != 7]

    return len(days_without_weekends)
