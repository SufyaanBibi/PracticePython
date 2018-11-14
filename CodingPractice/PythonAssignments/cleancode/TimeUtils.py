from datetime import datetime

secs_in_day = 24 * 60 * 60


def get_date_time(date_time_str):
    date_str, time_str = date_time_str.split(' ')
    year, month, day = date_str.split('/')
    hour, minute, second = time_str.split(':')
    return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))


def hours_between_util(start_time, end_time):
    start = get_date_time(start_time)
    end = get_date_time(end_time)
    difference = end - start
    return (difference.days * 24) + (difference.seconds // 3600)


def seconds_between_util(start_time, end_time):
    start = get_date_time(start_time)
    end = get_date_time(end_time)
    difference = end - start
    return (difference.days * secs_in_day) + difference.seconds
