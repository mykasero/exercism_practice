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

'''
Instructions
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: nopqrstuvwxyzabcdefghijklm
It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

Ciphertext is written out in the same formatting as the input including spaces and punctuation.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rotational-cipher/canonical-data.json
