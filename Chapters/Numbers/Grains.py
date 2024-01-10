def square(number):
    if number > 0 and number < 65:
        GRAIN_AMOUNT = 1
        for grain in range(2,number+1):
            GRAIN_AMOUNT *= 2
        return GRAIN_AMOUNT
    else:
        raise ValueError("square must be between 1 and 64")
def total():
    GRAIN_TOTAL = 1
    square_grain_amount = 1
    for grain in range(2,65):
        square_grain_amount *= 2
        GRAIN_TOTAL += square_grain_amount
        print(GRAIN_TOTAL)
    return GRAIN_TOTAL
