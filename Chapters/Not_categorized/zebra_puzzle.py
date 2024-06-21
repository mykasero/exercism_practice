from itertools import permutations
def drinks_water():
    for house in build():
        if house[3] == "water":
            return house[1]
    else:
        return False
def owns_zebra():
    for house in build():
        if house[2] == "zebra":
            return house[1]
    else:
        return False
def build():
    return house()
def house():
    house = ["red", "blue", "ivory", "yellow", "green"]
    for h in permutations(house):
        if list(h).index("green") - 1 != list(h).index("ivory"):
            continue
        if h[1] != "blue":
            continue
        result = nationality(h)
        if result is False:
            continue
        else:
            return result
def nationality(house):
    nationality = ["Norwegian", "Spanish", "Ukrain", "Japanese", "English"]
    for n in permutations(nationality):
        if n[list(house).index("red")] != "English":
            continue
        if n[0] != "Norwegian":
            continue
        result = pet(house, n)
        if result is False:
            continue
        else:
            return result
    else:
        return False
def pet(house, nationality):
    pet = ["dog", "snail", "fox", "horse", "zebra"]
    for p in permutations(pet):
        if p[list(nationality).index("Spanish")] != "dog":
            continue
        result = drink(house, nationality, p)
        if result is False:
            continue
        else:
            return result
    else:
        return False
def drink(house, nationality, pet):
    drink = ["coffee", "tea", "milk", "orange juice", "water"]
    for d in permutations(drink):
        if d[list(house).index("green")] != "coffee":
            continue
        if d[list(nationality).index("Ukrain")] != "tea":
            continue
        if d[2] != "milk":
            continue
        result = smoke(house, nationality, pet, d)
        if result is False:
            continue
        else:
            return result
    else:
        return False
def smoke(house, nationality, pet, drink):
    smoke = ["kool", "old gold", "chesterfield", "lucky strike", "parliament"]
    for s in permutations(smoke):
        if pet[list(s).index("old gold")] != "snail":
            continue
        if s[list(house).index("yellow")] != "kool":
            continue
        if abs(list(s).index("chesterfield") - list(pet).index("fox")) != 1:
            continue
        if abs(list(s).index("kool") - list(pet).index("horse")) != 1:
            continue
        if drink[list(s).index("lucky strike")] != "orange juice":
            continue
        if s[list(nationality).index("Japanese")] != "parliament":
            continue
        return zip(house, nationality, pet, drink, s)
    else:
        return False