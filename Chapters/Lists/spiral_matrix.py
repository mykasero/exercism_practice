from itertools import cycle
def spiral_matrix(size):
    matrix = [[None] * size for _ in range(size)]
    r, c = 0, 0
    # this cycle determines the movement of the "current cell"
    # (0,1) represents moving along a row to the right
    # (1,0) represents moving down a column
    deltas = cycle(((0,1), (1,0), (0,-1), (-1,0)))
    dr, dc = next(deltas)
    for i in range(size**2):
        matrix[r][c] = i+1
        if  not 0 <= r+dr < size or \
            not 0 <= c+dc < size or \
            matrix[r+dr][c+dc] is not None:

            dr, dc = next(deltas)

        r += dr
        c += dc

    return matrix

'''
Instructions
Given the size, return a square matrix of numbers in spiral order.

The matrix should be filled with natural numbers, starting from 1 in the top-left corner, increasing in an inward, clockwise spiral order, like these examples:

Examples
Spiral matrix of size 3

1 2 3
8 9 4
7 6 5

Spiral matrix of size 4

 1  2  3 4
12 13 14 5
11 16 15 6
10  9  8 7
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/spiral-matrix/canonical-data.json
