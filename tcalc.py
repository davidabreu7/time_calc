"""
Time and date calculator
"""
#!/home/dvlinux/PycharmProjects/time_calc/venv/bin/python

import argparse

from lib.timecalc import parse_date, parse_time, calc_time, calc_date, calc_weekday


def main():
    parser = argparse.ArgumentParser()
    add_argument = parser.add_argument
    add_argument('-d',
                 dest="date",
                 action='store',
                 nargs="+",
                 )
    add_argument('-t',
                 dest="time",
                 action='store',
                 nargs="+",
                 )
    add_argument('--day',
                 dest="day",
                 action='store',
                 nargs=1,
                 )
    args = parser.parse_args()

    if args.date:
        date_obj = parse_date(args.date)
        print(calc_date(date_obj))
    elif args.time:
        time_obj = parse_time(args.time)
        print(calc_time(time_obj))
    elif args.day:
        week_day = parse_date(args.day)
        print(calc_weekday(week_day[0]))


if __name__ == "__main__":
    main()
