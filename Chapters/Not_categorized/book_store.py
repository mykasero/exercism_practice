DISCOUNTS = {1 : 1, 2 : .95, 3 : .9, 4 : .8, 5 : .75}

def total(basket):
    if len(basket) == 0:
        return 0

    groups = []

    while len(basket) != 0:
        basket_set = set(basket)
        for member in basket_set:
            basket.remove(member)
        groups.append(len(basket_set))

    while {5, 3}.issubset(groups):
        groups.remove(5)
        groups.remove(3)
        groups += [4, 4]

    total = 0

    for group in groups:
        total += sum([800 * group * DISCOUNTS[group]])


    return total