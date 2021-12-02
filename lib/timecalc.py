from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


def parse_time(args):
    time_list = []
    try:
        time_list = [datetime.strptime(arg, "%H:%M:%S") for arg in args]
    except ValueError:
        print("hora fora do formato hh:mm:ss")
    return time_list


def parse_date(args):
    date_list = []
    try:
        date_list = [datetime.strptime(arg, "%d/%m/%Y") for arg in args]
    except ValueError:
        print("data fora do formato dd/mm/yyyy")
    return date_list


def calc_time(args):
    for arg in args:
        print(arg.time())

    if len(args) > 1:
        h1, h2 = args[0], args[1]
        if h1 < h2:
            h2, h1 = h1, h2

        delta = timedelta(hours=h2.hour, minutes=h2.minute, seconds=h2.second)
        print(delta)
        return args[0] - delta
    elif len(args) == 1:
        h1 = args[0]
        now = datetime.now()

        delta = timedelta(hours=h1.hour, minutes=h1.minute, seconds=h1.second)
        return now - delta


def calc_date(args):
    for arg in args:
        print(arg.date())

    if len(args) > 1:
        delta = relativedelta(years=args[0].year, months=args[0].month, days=args[0].day)
        return args[1] - delta
    elif len(args) == 1:
        today = datetime.today()
        delta = relativedelta(years=args[0].year, months=args[0].month, days=args[0].day)
        return today - delta


def calc_weekday(args):
    for arg in args:
        print(arg.date().strftime("%d %b %Y - %A"))