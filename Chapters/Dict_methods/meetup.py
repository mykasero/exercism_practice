import calendar
from datetime import date

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self,message):
        self.message = message


WEEKDAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
            5: "Friday", 6: "Saturday", 7: "Sunday"}

TEENTH = [13,14,15,16,17,18,19]

def meetup(year, month, week, day_of_week):
    final_date = None

    if week == "teenth":
        for item in TEENTH:
            that_date = date(year,month,item)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                final_date = that_date
                break

    elif week == "first":
        for i in range(1,calendar.monthrange(year,month)[1]+1):
            that_date = date(year,month,i)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                final_date = that_date
                break

    elif week == "second":
        ctr = 0
        for i in range(1,calendar.monthrange(year,month)[1]+1):
            that_date = date(year, month, i)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                ctr += 1
                if ctr == 2:
                    final_date = that_date
                    break

    elif week == "third":
        ctr = 0
        for i in range(1,calendar.monthrange(year,month)[1]+1):
            that_date = date(year, month, i)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                ctr += 1
                if ctr == 3:
                    final_date = that_date
                    break

    elif week == "fourth":
        ctr = 0
        for i in range(1,calendar.monthrange(year,month)[1]+1):
            that_date = date(year, month, i)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                ctr += 1
                if ctr == 4:
                    final_date = that_date
                    break

    elif week == "last":
        d_o_w_dates = []
        for i in range(1,calendar.monthrange(year,month)[1]+1):
            that_date = date(year,month,i)
            calendar_info = date.isocalendar(that_date)

            if WEEKDAYS[calendar_info.weekday] == day_of_week:
                d_o_w_dates.append(that_date)

        final_date = d_o_w_dates[len(d_o_w_dates)-1]

    elif week == "fifth":
        weeks_matrix = calendar.monthcalendar(year,month)
        d_o_w_dates = []

        if len(weeks_matrix) >= 5:
            for i in range(1, calendar.monthrange(year, month)[1] + 1):
                that_date = date(year, month, i)
                calendar_info = date.isocalendar(that_date)

                if WEEKDAYS[calendar_info.weekday] == day_of_week:
                    d_o_w_dates.append(that_date)


        if len(d_o_w_dates) >= 5:
            final_date = d_o_w_dates[len(d_o_w_dates) - 1]
        else:
            raise MeetupDayException("That day does not exist.")

    return final_date

'''
Instructions
Recurring monthly meetups are generally scheduled on the given weekday of a given week each month. 
In this exercise you will be given the recurring schedule, along with a month and year, and then asked to find the exact date of the meetup.

For example a meetup might be scheduled on the first Monday of every month. 
You might then be asked to find the date that this meetup will happen in January 2018. In other words, you need to determine the date of the first Monday of January 2018.

Similarly, you might be asked to find:

the third Tuesday of August 2019 (August 20, 2019)
the teenth Wednesday of May 2020 (May 13, 2020)
the fourth Sunday of July 2021 (July 25, 2021)
the last Thursday of November 2022 (November 24, 2022)
The descriptors you are expected to process are: first, second, third, fourth, last, teenth.

Note that descriptor teenth is a made-up word.

It refers to the seven numbers that end in '-teen' in English: 13, 14, 15, 16, 17, 18, and 19. 
But general descriptions of dates use ordinal numbers, e.g. the first Monday, the third Tuesday.

For the numbers ending in '-teen', that becomes:

13th (thirteenth)
14th (fourteenth)
15th (fifteenth)
16th (sixteenth)
17th (seventeenth)
18th (eighteenth)
19th (nineteenth)
So there are seven numbers ending in '-teen'. And there are also seven weekdays (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). 
Therefore, it is guaranteed that each day of the week (Monday, Tuesday, ...) will have exactly one numbered day ending with "teen" each month.

If asked to find the teenth Saturday of August, 1953 (or, alternately the "Saturteenth" of August, 1953), we need to look at the calendar for August 1953:

    August 1953
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
The Saturday that has a number ending in '-teen' is August 15, 1953.

How this Exercise is Structured in Python
We have added an additional week descriptor (fifth) for the fifth weekday of the month, if there is one.
If there is not a fifth weekday in a month, you should raise an exception.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/meetup/canonical-data.json
