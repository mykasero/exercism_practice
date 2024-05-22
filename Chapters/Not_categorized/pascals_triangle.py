def rows(row_count):
    # recursion
    mid_line = []
    if row_count < 0:
        raise ValueError("count must be a counting number")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    prior = rows(row_count - 1)

    for a, b in zip(prior[-1][:-1], prior[-1][1:]):
        mid_line.append(a + b)

    return prior + [[1] + mid_line + [1]]

    # attempt with a for loop

    # final = [[] for i in range(11)]
    #
    # line = []
    # if row_count == 1:
    #     final = [[1]]
    # elif row_count == 2:
    #     final=[[1],[1,1]]
    # else:
    #     final[0] = [1]
    #     final[1] = [1,1]
    #     for i in range(2,row_count+1):
    #         for j in range(i):
    #             if j == 0:
    #                 final[i].append(1)
    #             else:
    #                 final[i].append(final[i-1][j-1]+final[i-1][j])
    #         final[i].append(1)
    #
    #
    #
    #
    #
    # return final[:row_count]

'''
nstructions
Compute Pascal's triangle up to a given number of rows.

In Pascal's Triangle each number is computed by adding the numbers to the right and left of the current position in the previous row.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
# ... etc

This exercise is designed to be completed using recursion, rather than loops.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pascals-triangle/canonical-data.json

