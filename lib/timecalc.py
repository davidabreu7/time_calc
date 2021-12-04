import sys
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


def parse_time(args):
    time_list = []
    try:
        time_list = [datetime.strptime(arg, "%H:%M:%S") for arg in args]
    except TypeError:
        print("wrong time format -> hh:mm:ss")
        sys.exit(1)
    except ValueError:
        print("wrong time format -> hh:mm:ss")
        sys.exit(1)
    return time_list


def parse_date(args):
    date_list = []
    try:
        date_list = [datetime.strptime(arg, "%d/%m/%Y") for arg in args]
    except ValueError:
        print("wrong date format -> dd/mm/yyyy")
        sys.exit(1)
    except TypeError:
        print("wrong date format -> dd/mm/yyyy")
        sys.exit(1)
    return date_list


def calc_time(args):
    if len(args) > 1:
        h1, h2 = args[0], args[1]
        if h1 < h2:
            h2, h1 = h1, h2

        delta = timedelta(hours=h2.hour, minutes=h2.minute, seconds=h2.second)
        return h1 - delta
    elif len(args) == 1:
        h1 = args[0]
        now = datetime.now()
        if h1 < now:
            now, h1 = h1, now

        delta = timedelta(hours=h1.hour, minutes=h1.minute, seconds=h1.second)
        calculation_time = now - delta
        return calculation_time.strftime("%H:%M:%S")


def calc_date(args):
    if len(args) > 1:
        h1, h2 = args[0], args[1]
        if h1 > h2:
            h2, h1 = h1, h2

    if len(args) > 1:
        delta = relativedelta(years=h1.year, months=h1.month, days=h1.day)
        calculation_date = h2 - delta
        return calculation_date.strftime(f"%Y years %m months %d days")
    elif len(args) == 1:
        h1 = args[0]
        today = datetime.today()
        if h1 > today:
            today, h1 = h1, today
        delta = relativedelta(years=h1.year, months=h1.month, days=h1.day)
        calculation_date = today - delta
        return calculation_date.strftime("%Y years %m months %d days")


def calc_weekday(week_day: str):
    return week_day.date().strftime("%d %b %Y - %A")
