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

"""
Instructions
Implement a simple shift cipher like Caesar and a more secure substitution cipher.

Step 1
"If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. 
If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others." 
—Suetonius, Life of Julius Caesar

Ciphers are very straight-forward algorithms that allow us to render text less readable while still allowing easy deciphering. 
They are vulnerable to many forms of cryptanalysis, but Caesar was lucky that his enemies were not cryptanalysts.

The Caesar Cipher was used for some messages from Julius Caesar that were sent afield. 
Now Caesar knew that the cipher wasn't very good, but he had one ally in that respect: almost nobody could read well. 
So even being a couple letters off was sufficient so that people couldn't recognize the few words that they did know.

Your task is to create a simple shift cipher like the Caesar Cipher.
For example:

Giving "iamapandabear" as input to the encode function returns the cipher "ldpdsdqgdehdu". Obscure enough to keep our message secret in transit.

When "ldpdsdqgdehdu" is put into the decode function it would return the original "iamapandabear" letting your friend read your original message.

Step 2
Shift ciphers quickly cease to be useful when the opposition commander figures them out. So instead, let's try using a substitution cipher. 
Try amending the code to allow us to specify a key and use that for the shift distance.

Here's an example:

Given the key "aaaaaaaaaaaaaaaaaa", encoding the string "iamapandabear" would return the original "iamapandabear".

Given the key "ddddddddddddddddd", encoding our string "iamapandabear" would return the obscured "ldpdsdqgdehdu"

In the example above, we've set a = 0 for the key value. So when the plaintext is added to the key, we end up with the same message coming out. 
So "aaaa" is not an ideal key. But if we set the key to "dddd", we would get the same thing as the Caesar Cipher.

Step 3
The weakest link in any cipher is the human being. Let's make your substitution cipher a little more fault tolerant by 
providing a source of randomness and ensuring that the key contains only lowercase letters.

If someone doesn't submit a key at all, generate a truly random key of at least 100 lowercase characters in length.
"""
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/simple-cipher/canonical-data.json
