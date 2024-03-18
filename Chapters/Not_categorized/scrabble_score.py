def score(word):
    let_scores = {"A" : 1, "E" : 1, "I" : 1, "O" : 1, "U" : 1, "L" : 1, "N" : 1,
                 "R" : 1, "S" : 1, "T" : 1, "D" : 2, "G" : 2, "B" : 3, "C" : 3,
                 "M" : 3, "P" : 3, "F" : 4, "H" : 4, "V" : 4, "W" : 4, "Y" : 4,
                 "K" : 5, "J" : 8, "X" : 8, "Q" : 10, "Z" : 10}
    score = 0
    for letter in word:
        score += let_scores[letter.upper()]

    return score

'''
Instructions
Given a word, compute the Scrabble score for that word.

Letter Values
You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
Examples
"cabbage" should be scored as worth 14 points:

3 points for C
1 point for A, twice
3 points for B, twice
2 points for G
1 point for E
And to total:

3 + 2*1 + 2*3 + 2 + 1
= 3 + 2 + 6 + 3
= 5 + 9
= 14
Extensions
You can play a double or a triple letter.
You can play a double or a triple word.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/scrabble-score/canonical-data.json
