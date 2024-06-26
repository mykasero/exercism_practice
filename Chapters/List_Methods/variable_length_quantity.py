def encode(bytes):
    result = []
    for b in bytes:
        print('For:', b)
        t = []
        while b != 0:
            t.insert(0, b & 0x7f)
            b = b >> 7
        for i in range(len(t) - 1):
            t[i] = t[i] | 0x80
        if len(t) == 0:
            result.append(0)
        else:
            for x in t:
                result.append(x)
    return result
def decode(bytes):
    if len(bytes) > 0 and bytes[-1] & 0x80 > 0:
        raise ValueError('incomplete sequence')
    result = []
    x = 0
    for b in bytes:
        x = (x << 7) | (b & 0x7f)
        if b & 0x80 == 0:
            result.append(x)
            x = 0
    return result
'''
Instructions
Implement variable length quantity encoding and decoding.

The goal of this exercise is to implement VLQ encoding/decoding.

In short, the goal of this encoding is to encode integer values in a way that would save bytes. Only the first 7 bits of each byte are significant (right-justified; sort of like an ASCII byte). So, if you have a 32-bit value, you have to unpack it into a series of 7-bit bytes. Of course, you will have a variable number of bytes depending upon your integer. To indicate which is the last byte of the series, you leave bit #7 clear. In all of the preceding bytes, you set bit #7.

So, if an integer is between 0-127, it can be represented as one byte. Although VLQ can deal with numbers of arbitrary sizes, for this exercise we will restrict ourselves to only numbers that fit in a 32-bit unsigned integer. Here are examples of integers as 32-bit values, and the variable length quantities that they translate to:

 NUMBER        VARIABLE QUANTITY
00000000              00
00000040              40
0000007F              7F
00000080             81 00
00002000             C0 00
00003FFF             FF 7F
00004000           81 80 00
00100000           C0 80 00
001FFFFF           FF FF 7F
00200000          81 80 80 00
08000000          C0 80 80 00
0FFFFFFF          FF FF FF 7F
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/variable-length-quantity/canonical-data.json
