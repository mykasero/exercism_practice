alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet1 = dict()
inv_alphabet = dict()
for iter1 in range(0, 26):
    alphabet1[alphabet[iter1]] = alphabet1.get(alphabet[iter1], alphabet[iter1])
for iter2 in range(25, -1, -1):
    inv_alphabet[alphabet[25 - iter2]] = inv_alphabet.get("", alphabet[iter2])


def encode(plain_text):
    group_iter = 0
    encoded1 = ""
    plain_text = plain_text.replace(" ", "").replace(".", "").replace(",", "").lower()
    for letter in plain_text:
        if group_iter < 5 and letter not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            encoded1 += inv_alphabet[letter]
            group_iter += 1

        elif group_iter < 5 and letter in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            encoded1 += letter
            group_iter += 1
        else:
            encoded1 += " " + inv_alphabet[letter]
            group_iter = 1

    return encoded1


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "").replace(".", "").replace(",", "").lower()
    decoded1 = ""
    for letter in ciphered_text:
        if letter not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            decoded1 += inv_alphabet[letter]
        else:
            decoded1 += letter

    return decoded1