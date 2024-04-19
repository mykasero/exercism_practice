import math as m

PUNCTUATION = [",", " ", ".", "'", '"', "%", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "="]


def cipher_text(plain_text):
    final = ""
    new_text = plain_text.lower()
    for item in PUNCTUATION:
        if item in new_text:
            new_text = new_text.replace(item, "")

    text_len = len(new_text)
    if text_len == 1:
        rows = 1
        columns = 1
    else:
        rows = m.isqrt(text_len)
        columns = rows
    # print(columns,rows)

    if text_len > (rows * columns):
        new_text += (text_len - (rows * columns)) * " "

    if len(new_text) == 0:
        return final
    else:
        for row in range(rows):
            for letter in range(0,text_len,columns):
                final += new_text[letter+row]
            if text_len > 1 and row < rows-1:
                final+=" "

test_text = "Chill out."
print(cipher_text(test_text))