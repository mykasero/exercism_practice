# 8 passed , 4 failed

import random
import string
LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


class Cipher:
    def __init__(self, key=None):
        self.key = ""

        if key == None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k = 100))
        else:
            self.key = key

     #all encode passed      
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
                new_text += LETTERS[(LETTERS.index(self.key[item])+LETTERS.index(text[item]))-26]
            else:
                new_text += LETTERS[LETTERS.index(self.key[item])+LETTERS.index(text[item])]

        return new_text

    #needs more work
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
        index_val = 0
        if self.key == "a" * len(text):
            decoded = text
        else:
            for item in range(len(text)):
                if (LETTERS.index(self.key[item]) + LETTERS.index(text[item])) > 25:
                    index_val = LETTERS.index(text[item]) - LETTERS.index(self.key[item])
                    decoded += LETTERS[index_val]
                else:
                    decoded += LETTERS[(LETTERS.index(self.key[item]) - LETTERS.index(text[item]))%26]

        return decoded
