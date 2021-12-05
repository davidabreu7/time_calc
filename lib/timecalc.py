import sys
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


def parse_time(args: list[str]) -> list[datetime]:
    """
    receives a list of strings from the CLI arguments and parse for errors
    :param args: list of strings from CLI
    :return: a list of datetime objects
    """

    try:
        time_list = [datetime.strptime(arg, "%H:%M:%S") for arg in args]
    except TypeError:
        print("wrong time format -> hh:mm:ss")
        sys.exit(1)
    except ValueError:
        print("wrong time format -> hh:mm:ss")
        sys.exit(1)

    return time_list


def parse_date(args: list[str]) -> list:
    """
    receives a list of string from the CLI arguments and parse for errors
    :param args: strings from CLI
    :return: a list of datetime objects
    """

    try:
        date_list = [datetime.strptime(arg, "%d/%m/%Y") for arg in args]
    except ValueError:
        print("wrong date format -> dd/mm/yyyy")
        sys.exit(1)
    except TypeError:
        print("wrong date format -> dd/mm/yyyy")
        sys.exit(1)

    return date_list


def calc_time(args: list[datetime]) -> str:
    """
    checks if received one or two arguments and calculates accordingly
    :param args: list of datetime objects from parse_time()
    :return: a string with the result of the calculation
    """
    if len(args) > 1:
        argument_1, argument_2 = args[0], args[1]
        if argument_1 < argument_2:
            argument_2, argument_1 = argument_1, argument_2

        delta = timedelta(hours=argument_2.hour, minutes=argument_2.minute, seconds=argument_2.second)
        calculation_time = argument_1 - delta
        return calculation_time.strftime("%H:%M:%S")

    if len(args) == 1:
        argument_1 = args[0]
        now = datetime.now()
        if argument_1 < now:
            now, argument_1 = argument_1, now

        delta = timedelta(hours=argument_1.hour, minutes=argument_1.minute, seconds=argument_1.second)
        calculation_time = now - delta

        return calculation_time.strftime("%H:%M:%S")


def calc_date(args: list[datetime]) -> str:
    """
    checks if received one or two arguments and calculates accordingly
    :param args: list of datetime objects from parse_date()
    :return: a string with the result of the calculation
    """

    if len(args) > 1:
        argument_1, argument_2 = args[0], args[1]
        if argument_1 > argument_2:
            argument_2, argument_1 = argument_1, argument_2

        delta = relativedelta(years=argument_1.year, months=argument_1.month, days=argument_1.day)
        calculation_date = argument_2 - delta

        return calculation_date.strftime("%Y years %m months %d days")

    if len(args) == 1:
        argument_1 = args[0]
        today = datetime.today()
        if argument_1 > today:
            today, argument_1 = argument_1, today
        delta = relativedelta(years=argument_1.year, months=argument_1.month, days=argument_1.day)
        calculation_date = today - delta

        return calculation_date.strftime("%Y years %m months %d days")


def calc_weekday(week_day: datetime) -> str:
    """
    :param week_day:datetime object from parse_date()
    :return: a string containing the date and weekday
    """
    return week_day.date().strftime("%d %b %Y - %A")
