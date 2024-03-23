def decode(string):
    final = ""
    multiplies = []
    ltr = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
               "J", "K", "L", "M", "N", "O", "U", "P", "R",
               "S", "T", "Q", "W", "X", "Y", "Z", " "]

    repeats = ""

    string1 = string

    for letter in string1:
        if letter.upper() not in letters:
            repeats += letter
        else:
            ltr.append(letter)
            if repeats == "":
                multiplies.append(1)
            else:
                multiplies.append(int(repeats))
            repeats = ""

    for amount in range(len(multiplies)):
        final += multiplies[amount] * ltr[amount]

    print(multiplies, ltr)
    return final


def encode(string):
    count = 0
    final = ""
    if len(string) < 1:
        return ""
    else:
        for letter in range(1, len(string)):
            if string[letter - 1] == string[letter]:
                count += 1

            elif string[letter - 1] != string[letter]:
                count += 1
                if count == 1:
                    final += string[letter - 1]
                else:
                    final += str(count) + string[letter - 1]
                count = 0

        if count == 0:
            final += string[len(string) - 1]
        else:
            final += str(count + 1) + string[len(string) - 1]

    return final

'''
Instructions
Implement run-length encoding and decoding.

Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count.

For example we can represent the original 53 characters with only 13.

"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or upper case) and whitespace. This way data to be encoded will never contain any numbers and numbers inside data to be decoded always represent the count for the following character.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/run-length-encoding/canonical-data.json
