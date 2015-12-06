# -*- coding: utf-8 -*-
# Conventions are according to NumPy Docstring.

NUMERIC_TO_MONTH = {1: "January",
                    2: "February",
                    3: "March",
                    4: "April",
                    5: "May",
                    6: "June",
                    7: "July",
                    8: "August",
                    9: "September",
                    10: "October",
                    11: "November",
                    12: "December"}

MONTH_DAYS_DICT = {"January": 31,
                   "February": 29,
                   "March": 31,
                   "April": 30,
                   "May": 31,
                   "June": 30,
                   "July": 31,
                   "August": 31,
                   "September": 30,
                   "October": 31,
                   "November": 30,
                   "December": 31}

WEEKDAYS = {0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"}


def isLeapYear(year):
    """Determine if the input year is a leap-year.

    A leap-year has an extra day in February.

    Parameters
    ----------
    year : int
        An integer representative of a date's year.

    """
    if (year % 4 == 0):
        if (str(year)[-2:] == "00" and year % 400 != 0):
            return False
        return True
    else:
        return False


class Date:
    """This date class, as the name suggests, represents dates in YYYY-MM-DD format.

    Attributes
    ----------
    year : int
        An integer representative of the year.
    month : int
        An integer representative of the month.
    day : int
        An integer representative of the day.

    """

    def __init__(self, year=1900, month=1, day=1):
        """Initializer method

        Raises exception if date is invalid. This may be due to the day exceeding
        the maximum number of days in the given month, or February 29 is specified on a
        non-Leap Year, etc.

        Parameters
        ----------
        year : int
            A four-digit integer representative of the year.
        month : int
            An integer representative of the month.
        day : int
            An integer representative of the day.

        """
        # ensure the inputs are parsed into integers
        year = int(year)
        month = int(month)
        day = int(day)
        # if the year is not from 0000 to 9999
        if not (0 <= year and year <= 9999):
            raise Exception("Year must be between 0000 A.C. and 9999 A.C.")
        # if the day is less than or equal to 0 or
        # it exceeds maximum number of days in corresponding month
        if not (0 < day and day <= MONTH_DAYS_DICT[NUMERIC_TO_MONTH[month]]):
            raise Exception("Day does not exist in the month.")
        # check leap year validity
        if (not isLeapYear(year) and month == 2 and day > 28):
            raise Exception("February 29 does not exist in non-Leap Years")
        else:
            self._year = year
            self._month = month
            self._day = day

    def __str__(self):
        """Return string representation of the date in the format YYYY-MM-DD."""
        # year, formatted unambiguously as YYYY, padded with zeros if not
        # four-digit
        yearString = "0" * (4 - len(str(self.get_year()))
                            ) + str(self.get_year())
        # month, formatted unambiguously as MM, padded with zeros if not
        # two-digit
        monthString = "0" * (2 - len(str(self.get_month()))
                             ) + str(self.get_month())
        # day, formatted unambiguously as DD, padded with zeros
        dayString = "0" * (2 - len(str(self.get_day()))) + str(self.get_day())
        # aggregate all the string representations
        return "%s-%s-%s" % (yearString, monthString, dayString)

    def get_year(self):
        """int: Get the year from the date."""
        return self._year

    def get_month(self):
        """int: Get the month from the date."""
        return self._month

    def get_day(self):
        """int: Get the day from the date."""
        return self._day

    def get_weekday(self):
        """Find the weekday of a given date in the format YYYY-MM-DD.

        Based on the fact that 1900-01-01 (January 1st, 1900) is a Monday.

        Parameters
        ----------
        date : str
            The input string must be in the form YYYY-MM-DD.

        Returns
        -------
        str
            The outcomes can be:
                - "Monday"
                - "Tuesday"
                - "Wednesday"
                - "Thursday"
                - "Friday"
                - "Saturday"
                - "Sunday"

        """
        originDate = Date(1900, 1, 1)
        return WEEKDAYS[originDate.days_since(self) % 7]

    def days_since(self, otherDate):
        """Given another date, find out how many days passed since this date.

        Parameters
        ----------
        otherDate : Date
            Another initialized, valid date.

        Returns
        -------
        int
            The number of days that has passed since.

        """
        # initialize days passed
        days = 0
        # time difference of the year
        yearDiff = otherDate.get_year() - self.get_year()
        days += yearDiff * 365
        # if other date is in the future, traverse forwards otherwise go
        # backwards
        if yearDiff > 0:
            yearIncrementer = 1
        else:
            yearIncrementer = -1
        # account for leap years
        for yr in range(self.get_year(),
                        otherDate.get_year() + yearIncrementer,
                        yearIncrementer):
            if isLeapYear(yr) and yr != otherDate.get_year():
                days += 1
        monthDiff = otherDate.get_month() - self.get_month()
        if monthDiff > 0:
            monthIncrementer = 1
        else:
            monthIncrementer = -1
        for month in range(min(self.get_month(), otherDate.get_month()),
                           max(self.get_month(), otherDate.get_month())):
            daysIncrement = MONTH_DAYS_DICT[NUMERIC_TO_MONTH[month]]
            if (month == 2 and (not isLeapYear(otherDate.get_year()))):
                daysIncrement -= 1
            # print month, daysIncrement
            days += monthIncrementer * daysIncrement
        # account for days
        dayDiff = otherDate.get_day() - self.get_day()
        days += dayDiff
        # return resulting days passed
        return days
