def equilateral(sides):
    # rownoboczny
    a = sides[0]
    b = sides[1]
    c = sides[2]
    is_true = False

    if a == b == c and a != 0:
        is_true = True

    return is_true


def isosceles(sides):
    # rownoramienny
    is_true = False
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a == b and a != c or b == c and b != a or c == a and c != b or a == b == c and a != 0:
        is_true = True
    if a + b < c or b + c < a or c + a < b:
        is_true = False

    return is_true


def scalene(sides):
    # rozboczny
    is_true = False
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if a != 0 and b != 0 and c != 0 and a != b != c:
        is_true = True

    if a == b or b == c or a == c:
        is_true = False

    if a + b < c or b + c < a or c + a < b:
        is_true = False

    return is_true