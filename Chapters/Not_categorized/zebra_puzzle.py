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


'''
Introduction
The Zebra Puzzle is a famous logic puzzle in which there are five houses, each painted a different color. 
The houses have different inhabitants, who have different nationalities, own different pets, drink different beverages and smoke different brands of cigarettes.

To help you solve the puzzle, you're given 15 statements describing the solution. However, only by combining the information in all statements 
will you be able to find the solution to the puzzle.

Note
The Zebra Puzzle is a Constraint satisfaction problem (CSP). In such a problem, you have a set of possible values and a set of constraints that 
limit which values are valid. Another well-known CSP is Sudoku.

Instructions
Your task is to solve the Zebra Puzzle to find the answer to these two questions:

Which of the residents drinks water?
Who owns the zebra?
Puzzle
The following 15 statements are all known to be true:

There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.
Additionally, each of the five houses is painted a different color, and their inhabitants are of different national extractions, 
own different pets, drink different beverages and smoke different brands of cigarettes.

Note
There are 24 billion (5!⁵ = 24,883,200,000) possible solutions, so try ruling out as many solutions as possible.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/zebra-puzzle/canonical-data.json
