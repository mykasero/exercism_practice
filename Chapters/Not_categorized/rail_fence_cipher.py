from itertools import cycle

def encode(message, rails):
    encoded = []
    final = ""
    movement = []

    for rail in range(rails):
        encoded.append("")

    if rails == 2:
        movement = [0,1]
        cycles = cycle(movement)

        for item in cycles:
            if len(message) > 0:
                encoded[item] += message[0]
                message = message[1:]
            else:
                break

    elif rails == 3:
        movement = [0,1,2,1]
        cycles = cycle(movement)

        for item in cycles:
            if len(message) > 0:
                encoded[item] += message[0]
                message = message[1:]
            else:
                break


    elif rails == 4:
        movement = [0,1,2,3,2,1]
        cycles = cycle(movement)

        for item in cycles:
            if len(message) > 0:
                encoded[item] += message[0]
                message = message[1:]
            else:
                break

    for item in encoded:
        final += item

    return final


def decode(encoded_message, rails):
    split_text = []
    final = ""

    movement = []


    if rails == 3:
        movement = [0, 1, 2, 1]
        for i in range(rails):
            split_text.append("")

        for i in range(len(encoded_message)):
            if i < rails*2:
                split_text[0] += encoded_message[i]

            elif rails*2 <= i < (rails*2) + (rails*4)-1:
                split_text[1] += encoded_message[i]
            else:
                split_text[2] += encoded_message[i]

    elif rails == 5:
        movement = [0, 1, 2, 3, 4, 3, 2, 1]
        for i in range(rails):
            split_text.append("")

        for i in range(len(encoded_message)):
            if i < rails-2:
                split_text[0] += encoded_message[i]
            elif rails-2 <= i < rails+2:
                split_text[1] += encoded_message[i]
            elif rails+2 <= i < (2*rails)+1:
                split_text[2] += encoded_message[i]
            elif (2*rails)+1 <= i < (3*rails):
                split_text[3] += encoded_message[i]
            else:
                split_text[4] += encoded_message[i]

    elif rails == 6:
        movement = [0,1,2,3,4,5,4,3,2,1]

        for i in range(rails):
            split_text.append("")

        for i in range(len(encoded_message)):
            if i < rails:
                split_text[0] += encoded_message[i]

            elif rails <= i < (rails) + (2*rails):
                split_text[1] += encoded_message[i]

            elif (rails+2) + (2*rails)-2 <= i < rails + 2*((2*rails)):
                split_text[2] += encoded_message[i]

            elif rails + 2*((2*rails)) <= i < rails + 3*((2*rails)):
                split_text[3] += encoded_message[i]

            elif rails + 3*((2*rails)) <= i < rails + 4*((2*rails)):
                split_text[4] += encoded_message[i]

            else:
                split_text[5] += encoded_message[i]


    while len(encoded_message) > len(final):
        for item in movement:
            if len(split_text[item]) > 0:
                final += split_text[item][0]
                split_text[item] = split_text[item][1:]

    return final

'''
Instructions
Implement encoding and decoding for the rail fence cipher.

The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence, then moving up when we get to the bottom (like a zig-zag). 
Finally the message is then read off in rows.

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipherer writes out:

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .

Then reads off:

WECRLTEERDSOEEFEAOCAIVDEN


To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.

? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .

The first row has seven spots that can be filled with "WECRLTE".

W . . . E . . . C . . . R . . . L . . . T . . . E
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .

Now the 2nd row takes "ERDSOEEFEAOC".

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .

Leaving "AIVDEN" for the last row.

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rail-fence-cipher/canonical-data.json
