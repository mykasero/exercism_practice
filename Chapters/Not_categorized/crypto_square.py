import math as m

PUNCTUATION = [",", " ", ".", "'", '"', "%", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "="]


def cipher_text(plain_text):
    final = ""
    new_text = plain_text.lower()

    columns = 0
    rows = 0

    for item in PUNCTUATION:
        if item in new_text:
            new_text = new_text.replace(item, "")

    text_len = len(new_text)
    if text_len == 1:
        rows = 1
        columns = 1
    else:
        rows_ori = m.sqrt(text_len)
        rows_rnd_down = m.isqrt(text_len)
        if rows_ori - rows_rnd_down > 0.5:
            columns = rows_rnd_down + 1
            rows = rows_rnd_down
        else:
            columns = rows_rnd_down
            rows = rows_rnd_down

    if text_len > (rows * columns):
        new_text += (text_len - (rows * columns)) * " "

    if len(new_text) == 0:
        return final
    else:
        if text_len < 10:
            for column in range(columns):
                for letter in range(0, text_len, columns):
                    if text_len > letter + column:
                        final += new_text[letter + column]

                if text_len > 1 and column < columns - 1:
                    final += " "

            final_chopped = final.split()
            if len(final_chopped[len(final_chopped) - 1]) < len(final_chopped[len(final_chopped) - 2]):
                final += " "

        else:
            columns += 1
            for column in range(columns):
                for letter in range(0, text_len, columns):
                    if text_len > letter + column:
                        final += new_text[letter + column]

                if text_len > 1 and column < columns - 1:
                    final += " "

            final_chopped = final.split()

            for item in range(1, len(final_chopped)):
                if len(final_chopped[0]) > len(final_chopped[item]) and len(final_chopped) - 1 > item:
                    final_chopped[item] += "  "
                else:
                    final_chopped[item] += " "

            final_chopped[0] += " "
            final = ""

            for item in final_chopped:
                final += item

    return final

'''
Instructions
Implement the classic method for composing secret messages called a square code.

Given an English text, output the encoded version of that text.

First, the input is normalized: the spaces and punctuation are removed from the English text and the message is down-cased.

Then, the normalized characters are broken into rows. These rows can be regarded as forming a rectangle when printed with intervening newlines.

For example, the sentence

"If man was meant to stay on the ground, god would have given us roots."
is normalized to:

"ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
The plaintext should be organized into a rectangle as square as possible. The size of the rectangle should be decided by the length of the message.

If c is the number of columns and r is the number of rows, then for the rectangle r x c find the smallest possible integer c such that:

r * c >= length of message,
and c >= r,
and c - r <= 1.
Our normalized text is 54 characters long, dictating a rectangle with c = 8 and r = 7:

"ifmanwas"
"meanttos"
"tayonthe"
"groundgo"
"dwouldha"
"vegivenu"
"sroots  "
The coded message is obtained by reading down the columns going left to right.

The message above is coded as:

"imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"
Output the encoded text in chunks that fill perfect rectangles (r X c), with c chunks of r length, separated by spaces. 
For phrases that are n characters short of the perfect rectangle, pad each of the last n chunks with a single trailing space.

"imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
Notice that were we to stack these, we could visually decode the ciphertext back in to the original message:

"imtgdvs"
"fearwer"
"mayoogo"
"anouuio"
"ntnnlvt"
"wttddes"
"aohghn "
"sseoau "
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/crypto-square/canonical-data.json
