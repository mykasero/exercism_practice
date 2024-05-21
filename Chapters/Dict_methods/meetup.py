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
