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


test_text = "If man was meant to stay on the ground, god would have given us roots."

print(cipher_text(test_text))
