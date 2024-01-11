def convert(number):
    result = None
    if number % 7 == 0 and number % 5 == 0 and number % 3 == 0:
        result = "PlingPlangPlong"
    elif number % 7 == 0 and number % 5 == 0 and not number % 3 == 0:
        result = "PlangPlong"
    elif not number % 7 == 0 and number % 5 == 0 and number % 3 == 0:
        result = "PlingPlang"
    elif number % 7 == 0 and not number % 5 == 0 and number % 3 == 0:
        result = "PlingPlong"
    elif number % 7 == 0 and not number % 5 == 0 and not number % 3 == 0:
        result = "Plong"
    elif not number % 7 == 0 and number % 5 == 0 and not number % 3 == 0:
        result = "Plang"
    elif not number % 7 == 0 and not number % 5 == 0 and number % 3 == 0:
        result = "Pling"
    else:
        result = str(number)
    return result