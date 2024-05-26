# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        # first | at 11th spot, second at 39th, total len 0-51
        self.date = date
        self.description = description

        #formatting the change, X is a placeholder to later be replaced by a currency symbol
        if change < -99:
            self.change = "(X" + str(change)[0:len(str(change))-2] + "." + str(change)[len(str(change))-2:len(str(change))] + ")"
            self.change = self.change.replace("-","")
        elif -99 <= change < -9:
            self.change = "(X0." + str(change)[len(str(change)) - 2:len(str(change))] + ")"
            self.change = self.change.replace("-", "")
        elif -9 <= change < 0:
            self.change = "(X0.0" + str(change)[len(str(change)) - 1] + ")"
            self.change = self.change.replace("-", "")
        elif 0 <= change < 10:
            self.change = "X0.0" + str(change)[len(str(change)) - 1]
        elif 10 <= change < 1000:
            self.change = "X0." + str(change)[len(str(change)) - 1]
        else:
            self.change = "X" + str(change)[0:len(str(change))-2] + "." + str(change)[len(str(change))-2:len(str(change))]

        STOP = "STOP"


def create_entry(date, description, change):
    entry = LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)

    return entry


def format_entries(currency, locale, entries):
    # first | at 11th spot, second at 39th, total len 0-51
    template = "Date       | Description               | Change       "
    p1 = ""
    p2 = ""
    p3 = ""
    new_line = ""

    currencies = {"USD" : "$", "EUR" : "€"}

    '''
    lens
    p1 = 12 ends with |
    p2 = 28 (space at the start) ends with |
    p3 = 14 (space at the start)
    '''

    lines = []
    final = ""
    if not entries:
        return template

    else:
        lines.append(template)

        if locale == "en_US":

            for item in entries:
                #convert date to US standard
                p1 = datetime.strftime(item.date,"%m/%d/%Y")


                p2 = item.description

                #replace placeholder with currency symbol
                p3 = item.change.replace("X",currencies[currency])

                if len(p1) < 12:
                    p1 += (11-len(p1)) * " " + "|"
                if len(p2) < 28:
                    p2 = " " + p2 + (26-len(p2)) * " " + "|"
                if len(p3) < 14:
                    p3 = " " + (13-len(p3)) * " " + p3

                new_line = p1 + p2 + p3
                lines.append(new_line)
                new_line = ""

        stop = "STOP"

        #turn list into a string with new liners
        for i in range(len(lines)):
            if i < len(lines)-1:
                final += lines[i] + "\n"
            else:
                final += lines[i]



        return final



