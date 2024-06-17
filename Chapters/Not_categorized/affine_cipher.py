import string

NUMBERS = {"!" : "1", "@" : "2", "#" : "3", "$" : "4", "%" : "5", "^" : "6", "&" : "7", "*" : "8", "(" : "9"}

NUM_SYMBOLS = {}

def invert_dict():
    for key, value in NUMBERS.items():
        if value in NUM_SYMBOLS:
            NUM_SYMBOLS[value].append(key)
        else:
            NUM_SYMBOLS[value] = [key]

def is_coprime(a,b):
    c = 0
    while b != 0:
        c = a % b
        a = b
        b = c

        if a == 1:
            return True

    return False

def encode(plain_text, a, b):
    invert_dict()
    m = len(string.ascii_lowercase)

    if is_coprime(a,m) == False:
        raise ValueError("a and m must be coprime.")

    plain_text = plain_text.replace(" ","").replace(",","").replace(".","").lower()
    indexes = []
    encoded_index = 0

    for letter in plain_text:
        if letter.isnumeric():
            encoded_index = NUM_SYMBOLS[letter][0]

        else:
            encoded_index = ((a * string.ascii_lowercase.index(letter.lower())) + b) % m

        indexes.append(encoded_index)

    final = ""

    ctr = 0
    while ctr < len(plain_text):
        if ctr % 5 == 0 and ctr != 0:
            final += " "

        if indexes[ctr] in NUMBERS.keys():
            final += NUMBERS[indexes[ctr]]
        else:
            final += string.ascii_lowercase[indexes[ctr]]

        ctr += 1

    return final

def decode(ciphered_text, a, b):
    final = ""
    invert_dict()

    m = len(string.ascii_lowercase)

    if is_coprime(a,m) == False:
        raise ValueError("a and m must be coprime.")

    ciphered_text = ciphered_text.replace(" ", "")

    indexes = []

    mmi = 0

    for i in range(50):
        if (a*i) % 26 == 1:
            mmi = i
            break

    for letter in ciphered_text:
        if letter.isnumeric():
            encoded_index = NUM_SYMBOLS[letter][0]

        else:
            encoded_index = int((mmi * (string.ascii_lowercase.index(letter) - b)) % m)

        indexes.append(encoded_index)

    for letter_ind in indexes:
        if letter_ind in NUMBERS.keys():
            final += NUMBERS[letter_ind]
        else:
            final += string.ascii_lowercase[letter_ind]

    return final

