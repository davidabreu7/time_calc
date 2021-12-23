import sys
from datetime import datetime

from dateutil.relativedelta import relativedelta


def parse_time(args: list[str]) -> list[datetime]:
    """
    receives a list of strings from the CLI arguments and parse for errors
    :param args: list of strings from CLI
    :return: a list of datetime objects
    """

    try:
        time_list = [datetime.strptime(arg, "%H:%M:%S") for arg in args]
    except (TypeError, ValueError):
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
    except (ValueError, TypeError):
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
        time_1, time_2 = args[0], args[1]
        rdelta = relativedelta(time_2, time_1)

        return f"{abs(rdelta.hours)}:{abs(rdelta.minutes)}:{abs(rdelta.seconds)}"

    if len(args) == 1:
        time_1 = args[0]
        now = datetime.now()
        rdelta = relativedelta(time_1, now)

        return f"{abs(rdelta.hours)}:{abs(rdelta.minutes)}:{abs(rdelta.seconds)}"


def calc_date(args: list[datetime]) -> str:
    """
    checks if received one or two arguments and calculates accordingly
    :param args: list of datetime objects from parse_date()
    :return: a string with the result of the calculation
    """

    if len(args) > 1:
        argument_1, argument_2 = args[0], args[1]
        rdelta = relativedelta(argument_2, argument_1)

        return f"{abs(rdelta.years)} years {abs(rdelta.months)} months {abs(rdelta.days)} days"

    if len(args) == 1:
        argument_1 = args[0]
        today = datetime.today()
        rdelta = relativedelta(argument_1, today)

        return f"{abs(rdelta.years)} years {abs(rdelta.months)} months {abs(rdelta.days)} days"


def calc_weekday(week_day: datetime) -> str:
    """
    :param week_day:datetime object from parse_date()
    :return: a string containing the date and weekday
    """
    return week_day.date().strftime("%d %b %Y - %A")
