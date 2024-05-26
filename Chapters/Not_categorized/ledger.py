# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        # first | at 11th spot, second at 39th, total len 0-51
        self.date = datetime.strftime(date,"%m/%d/%Y")
        self.description = description
        if change < 0:
            self.change = "(X" + str(change)[0:len(str(change))-2].replace("-","") + "." + str(change)[len(str(change))-2:len(str(change))] + ")"
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

    final = []
    if not entries:
        return template

    else:
        final.append(template+"\n")

        if locale == "en_US":

            for item in entries:
                p1 = item.date
                p2 = item.description
                p3 = item.change.replace("X",currencies[currency])

                if len(p1) < 12:
                    p1 += (11-len(p1)) * " " + "|"
                if len(p2) < 28:
                    p2 = " " + p2 + (26-len(p2)) * " " + "|"
                if len(p3) < 14:
                    p3 = " " + (13-len(p3)) * " " + p3

                new_line = p1 + p2 + p3
                final.append(new_line)
                new_line = ""

        return final