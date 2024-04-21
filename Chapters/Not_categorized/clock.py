class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return "Clock(" + str(self.hour) + ", " + str(self.minute) + ")"

    def __str__(self):
        final = ""

        if self.minute < 0:
            if self.minute < -59:
                self.hour = self.hour - int(abs(self.minute) / 60) - 1
                self.minute = 60 - (abs(self.minute) % 60)
            else:
                self.hour -= 1
                self.minute += 60

        if self.hour < 0:
            if self.hour < -24:
                self.hour = 24 - (abs(self.hour) % 24)
            else:
                self.hour += 24

        if self.minute > 59:
            self.hour = self.hour + int(self.minute / 60)
            self.minute %= 60

        if self.hour > 24:
            self.hour %= 24

        if len(str(self.hour)) > 1 and len(str(self.minute)) > 1:
            if self.hour == 24:
                final = "00:" + str(self.minute)
            else:
                final = str(self.hour) + ":" + str(self.minute)
        elif len(str(self.hour)) > 1 and len(str(self.minute)) == 1:
            if self.hour == 24:
                final = "00:0" + str(self.minute)
            else:
                final = str(self.hour) + ":0" + str(self.minute)
        elif len(str(self.hour)) == 1 and len(str(self.minute)) > 1:
            final = "0" + str(self.hour) + ":" + str(self.minute)
        elif len(str(self.hour)) == 1 and len(str(self.minute)) == 1:
            final = "0" + str(self.hour) + ":0" + str(self.minute)

        return final

    def __eq__(self, other):
        hrs_flag = False
        mins_flag = False

        if other.minute < 0:
            other.hour -= int(abs(other.minute) / 60)
            other.minute = 60 - abs(other.minute)
            other.hour -= 1

        other.hour %= 24
        self.hour %= 24

        other.minute %= 60
        self.minute %= 60

        if other.hour == self.hour:
            hrs_flag = True
        if other.minute == self.minute:
            mins_flag = True

        return hrs_flag and mins_flag

    def __add__(self, minutes):
        final = self.__str__()
        hrs = int(final.split(":")[0])
        mins = int(final.split(":")[1])

        extra_hrs = 0

        if minutes + mins < 60:
            if mins < 10 and hrs < 10:
                final = "0" + str(hrs) + ":0" + str(mins + minutes)
            elif mins < 10 and hrs >= 10:
                final = str(hrs) + ":0" + str(mins + minutes)
            elif mins >= 10 and hrs < 10:
                final = "0" + str(hrs) + ":" + str(mins + minutes)
            else:
                final = str(hrs) + ":" + str(mins + minutes)
        else:
            extra_hrs = int((minutes + mins) / 60)
            hrs += extra_hrs
            mins = (minutes + mins) % 60

            if hrs >= 24:
                hrs %= 24

            if mins < 10 and hrs < 10:
                final = "0" + str(hrs) + ":0" + str(mins)
            elif mins < 10 and hrs >= 10:
                final = str(hrs) + ":0" + str(mins)
            elif mins >= 10 and hrs < 10:
                final = "0" + str(hrs) + ":" + str(mins)
            else:
                final = str(hrs) + ":" + str(mins)

        return final

    def __sub__(self, minutes):
        final = self.__str__()
        hrs = int(final.split(":")[0])
        mins = int(final.split(":")[1])

        extra_hrs = 0

        if 0 <= mins - minutes < 60:
            if mins < 10 and hrs < 10:
                final = "0" + str(hrs) + ":0" + str(mins - minutes)
            elif mins < 10 and hrs >= 10:
                final = str(hrs) + ":0" + str(mins - minutes)
            elif mins >= 10 and hrs < 10:
                final = "0" + str(hrs) + ":" + str(mins - minutes)
            else:
                final = str(hrs) + ":" + str(mins - minutes)
        else:
            extra_hrs = int(abs(mins - minutes) / 60)
            hrs -= extra_hrs
            mins = 60 - (abs((mins - minutes)) % 60)
            hrs -= 1
            if abs(hrs) >= 24:
                hrs = abs(hrs) % 24
            elif hrs < 0:
                hrs += 24

            if mins < 10 and hrs < 10:
                final = "0" + str(hrs) + ":0" + str(mins)
            elif mins < 10 and hrs >= 10:
                final = str(hrs) + ":0" + str(mins)
            elif mins >= 10 and hrs < 10:
                final = "0" + str(hrs) + ":" + str(mins)
            else:
                final = str(hrs) + ":" + str(mins)

        return final
