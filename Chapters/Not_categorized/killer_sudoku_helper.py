from itertools import combinations_with_replacement

def combinations(target, size, exclude):
    numbers = [1,2,3,4,5,6,7,8,9]
    final = []

    if exclude is not None:
        for item in exclude:
            numbers.pop(numbers.index(item))

    for i in range(size+1):
        combos = combinations_with_replacement(numbers, i)
        for combo in combos:
            if sum(combo) == target and len(list(set(combo))) == size:
                final.append(sorted(combo))


    return final

'''
Instructions
A friend of yours is learning how to solve Killer Sudokus (rules below) but struggling to figure out which digits can go in a cage. They ask you to help them out by writing a small program that lists all valid combinations for a given cage, and any constraints that affect the cage.

To make the output of your program easy to read, the combinations it returns must be sorted.

Killer Sudoku Rules
Standard Sudoku rules apply.
The digits in a cage, usually marked by a dotted line, add up to the small number given in the corner of the cage.
A digit may only occur once in a cage.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/killer-sudoku-helper/canonical-data.json
