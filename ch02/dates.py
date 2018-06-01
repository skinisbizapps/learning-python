from datetime import date
from datetime import time
from datetime import datetime


def main():
    print("in main")

    # Get today's date from the sample today() method from the date class
    today = date.today()
    print("today's date is ", today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Date components: ", today.weekday())
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    print("which is a: ", days[today.weekday()])

    ## Datetime objects
    # Get today's date from the datetime class
    dt = datetime.now()
    print("today's datetime is ", dt)

    # print out the datetime's individual components
    print("datetime components: ", dt.tzinfo, dt.fold, dt.second, dt.minute, dt.hour, dt.day, dt.month, dt.year)

    # Get the current time
    tt = time.hour

if __name__ == '__main__':
    main()
