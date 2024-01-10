def leap_year(year):
    leap_yr = False

    if year % 4 == 0 and year % 400 == 0 or year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
        leap_yr=True

    return leap_yr