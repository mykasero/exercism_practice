def score(x, y):
    points = 0
    x = float(abs(x))
    y = float(abs(y))

    if pow((x - 0), 2) + pow((y - 0), 2) <= 1.00000:
        points = 10
    elif pow((x - 0), 2) + pow((y - 0), 2) > 1.00000 and pow((x - 0), 2) + pow((y - 0), 2) <= 25.00000:
        points = 5
    elif pow((x - 0), 2) + pow((y - 0), 2) > 25.00000 and pow((x - 0), 2) + pow((y - 0), 2) <= 100.00000:
        points = 1
    else:
        points = 0

    return points
