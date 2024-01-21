list_one = list(range(3, 200, 3))
list_two = list(range(15, 200, 15))
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if contains(list_one, list_two):
        return SUPERLIST
    if contains(list_two, list_one):
        return SUBLIST
    return UNEQUAL


def contains(a, b):
    if not len(b):
        return True
    elif len(b) > len(a):
        return False
    for i in range(0, len(a) - len(b) + 1):
        if a[i] != b[0]:
            continue
        for j, v in enumerate(b):
            if a[i + j] != v:
                break
        else:
            return True
    return False



print(sublist(list_one,list_two))