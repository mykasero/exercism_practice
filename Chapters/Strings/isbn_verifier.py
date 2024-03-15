def is_valid(isbn):
    is_true = False
    numbers_conditional = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    undesirable_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "U", "P", "R",
                           "S", "T", "Z", "Y"]
    numbers = []

    if "-" in isbn:
        isbn = isbn.replace("-", "")
    else:
        pass

    if isbn == "" or len(isbn) < 10 or len(isbn) > 10 or isbn[len(isbn) - 1] in undesirable_letters:
        return False

    for i in range(10):
        if isbn[i] == 'X' and i == 9:
            numbers.append("10")
        elif isbn[i] == "X" and i < 9 or not isbn[i] in numbers_conditional and i < 9:
            return False

        else:
            numbers.append(isbn[i])

    isbn_sum = isbn_sum = int(numbers[0]) * 10 + int(numbers[1]) * 9 + int(numbers[2]) * 8 + int(numbers[3]) * 7 + int(
        numbers[4]) * 6 + int(numbers[5]) * 5 + int(numbers[6]) * 4 + int(numbers[7]) * 3 + int(numbers[8]) * 2 + int(
        numbers[9]) * 1

    if isbn_sum % 11 == 0:
        is_true = True

    return is_true

'''
Instructions
The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8

ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

Example
Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
Since the result is 0, this proves that our ISBN is valid.

Task
Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.

Caveats
Converting from strings to numbers can be tricky in certain languages. Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/isbn-verifier/canonical-data.json
