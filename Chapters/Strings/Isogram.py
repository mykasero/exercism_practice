def is_isogram(string):
    is_true = True
    string = string.lower()
    hyphen = "-"
    space = " "
    string = string.replace(hyphen, "")
    string = string.replace(space, "")
    letters_in_string = []

    for i in range(len(string)):
        letters_in_string.append(string[i])
    letters_in_string.sort()

    for j in range(len(letters_in_string) - 1):
        if letters_in_string[j] == letters_in_string[j + 1]:
            is_true = False

    return is_true

'''
Instructions
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/isogram/canonical-data.json
