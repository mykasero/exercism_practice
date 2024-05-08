# Encode tests passed / Decode to-do
def encode(message, rails):
    encoded = []
    final = ""

    for rail in range(rails):
        encoded.append("")

    if rails == 2:
        for i in range(len(message)):
            if i%2 == 0:
                encoded[0] += message[i]
            else:
                encoded[1] += message[i]
    elif rails == 3:
        i_top_bot = 4
        for i in range(len(message)):
            if i % 4 == 0:
                encoded[0] += message[i]
            elif i % 4 == 2:
                encoded[2] += message[i]
            else:
                encoded[1] += message[i]
    elif rails == 4:
        for i in range(len(message)):
            if i % 6 == 0:
                encoded[0] += message[i]
            elif i % 6 == 3:
                encoded [3] += message[i]
            elif i % 4 == 1 or i % 4 == 3:
                encoded[1] += message[i]
            else:
                encoded[2] += message[i]

    for item in encoded:
        final += item

    return final


def decode(encoded_message, rails):
    pass
