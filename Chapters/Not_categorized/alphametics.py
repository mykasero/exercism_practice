"""Solve an alphametics puzzle."""

import itertools
import string
from typing import Optional


def solve(puzzle: str) -> Optional[dict[str, int]]:
    left, right = puzzle.split(" == ")
    parts = [p.strip() for p in left.split("+")]
    words = parts + [right]
    letters = set().union(*(set(w) for w in words))
    # Try all permutations of digits for the letters.
    for vals in itertools.permutations(string.digits, r=len(letters)):
        mapping = dict(zip(letters, vals))
        translation = str.maketrans(mapping)
        translated = [w.translate(translation) for w in words]
        # All numbers cannot start with a 0.
        if any(w[0].startswith("0") for w in translated):
            continue
        if sum(int(w) for w in translated[:-1]) == int(translated[-1]):
            return {k: int(v) for k, v in mapping.items()}
    return None

'''
Instructions
Write a function to solve alphametics puzzles.

Alphametics is a puzzle where letters in words are replaced with numbers.

For example SEND + MORE = MONEY:

  S E N D
  M O R E +
-----------
M O N E Y
Replacing these with valid numbers gives:

  9 5 6 7
  1 0 8 5 +
-----------
1 0 6 5 2
This is correct because every letter is replaced by a different number and the words, translated into numbers, then make a valid sum.

Each letter must represent a different digit, and the leading digit of a multi-digit number must not be zero.

Write a function to solve alphametics puzzles.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/alphametics/canonical-data.json
