def rotate(text, key):
    ciphered = ""
    which_letters_upper = []
    counter = 0

    letters_letter = {"a": 1, "b": 2, "c": 3, "d": 4,
                      "e": 5, "f": 6, "g": 7, "h": 8,
                      "i": 9, "j": 10, "k": 11, "l": 12,
                      "m": 13, "n": 14, "o": 15, "p": 16,
                      "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24,
                      "y": 25, "z": 26, " ": 0}

    letters_num = {1: "a", 2: "b", 3: "c", 4: "d",
                   5: "e", 6: "f", 7: "g", 8: "h",
                   9: "i", 10: "j", 11: "k", 12: "l",
                   13: "m", 14: "n", 15: "o", 16: "p",
                   17: "q", 18: "r", 19: "s", 20: "t",
                   21: "u", 22: "v", 23: "w", 24: "x",
                   25: "y", 26: "z", 0: " "}

    for i in range(len(text)):
        if text[i].isupper():
            which_letters_upper.append(i)

    text = text.lower()

    for letter in text:

        if letter in [" ", ",", ".", ":", ";", "'", '"', "?", "!"] or letter in ["1", "2", "3", "4", "5", "6", "7", "8",
                                                                                 "9", "0"]:
            ciphered += letter
        else:
            raw_num = letters_letter[letter] + key
            dict_num = divmod(raw_num, 26)[1]

            if counter in which_letters_upper:

                if raw_num == 26:
                    ciphered += "Z"
                else:
                    ciphered += letters_num[dict_num].upper()
            else:

                if raw_num == 26:
                    ciphered += "z"
                else:
                    ciphered += letters_num[dict_num]
        counter += 1
    return ciphered
