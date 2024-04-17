import random
import string

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]


class Cipher:
    def __init__(self, key=None):
        self.key = ""

        if key == None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, text):

        _ctr = 0
        key_len = len(self.key)
        if len(text) > len(self.key):
            while len(text) > len(self.key):
                if _ctr < key_len:
                    self.key += self.key[_ctr]
                    _ctr += 1
                else:
                    _ctr = 0

        new_text = ""

        for item in range(len(text)):
            if (LETTERS.index(self.key[item]) + LETTERS.index(text[item])) > 25:
                new_text += LETTERS[(LETTERS.index(self.key[item]) + LETTERS.index(text[item])) - 26]
            else:
                new_text += LETTERS[LETTERS.index(self.key[item]) + LETTERS.index(text[item])]

        return new_text

    def decode(self, text):
        _ctr = 0
        key_len = len(self.key)
        if len(text) > len(self.key):
            while len(text) > len(self.key):
                if _ctr < key_len:
                    self.key += self.key[_ctr]
                    _ctr += 1
                else:
                    _ctr = 0

        decoded = ""
        t1 = None
        t2 = None

        index_val = 0
        if self.key == "a" * len(text):
            decoded = text
        else:
            for item in range(len(text)):

                t1 = LETTERS.index(self.key[item])
                t2 = LETTERS.index(text[item])

                if text[0] == "z":
                    if t2 - t1 < 0:
                        decoded += LETTERS[26 + (t2 - t1)]
                    elif t2 - t1 == 25:
                        decoded += LETTERS[25]
                else:
                    decoded += LETTERS[abs((t1 - t2))]

        return decoded
