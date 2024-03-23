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
