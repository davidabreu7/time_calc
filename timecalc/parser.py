"""
receives cli arguments and checks validity
"""
import sys
from datetime import datetime


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
