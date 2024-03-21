def rebase(input_base, digits, output_base):
    dec_list = []
    dec_num = 0
    final = []
    digits = digits[::-1]

    # check errors
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    else:
        for items in digits:
            if items < 0 or items >= input_base:
                raise ValueError("all digits must satisfy 0 <= d < input base")
                print("True")
    # check if all digits are 0
    zeros_ctr = 0
    for item in digits:
        if item == 0:
            zeros_ctr += 1

    # convert to decimal
    if input_base == 10:
        for base in range(len(digits) - 1, -1, -1):
            dec_num += digits[base] * input_base ** base
    else:
        for base in range(len(digits) - 1, -1, -1):
            dec_num += digits[base] * input_base ** base

    dec_list.append(dec_num)
    # convert to specified output base
    new_dec_num = dec_num

    while new_dec_num > 1:
        final.append(int(new_dec_num % output_base))
        new_dec_num = new_dec_num / output_base

    dec_list_split = []


    if zeros_ctr == len(digits):
        return [0]
    elif dec_num >= 10 and output_base == 10:
        for i in str(dec_num):
            dec_list_split.append(int(i))
        return dec_list_split

    elif output_base == 10:
        return dec_list

    else:
        return final[::-1]


'''
[medium level exercise]
Instructions
Convert a number, represented as a sequence of digits in one base, to any other base.

Implement general base conversion. Given a number in base a, represented as a sequence of digits, convert it to base b.

Note
Try to implement the conversion yourself. Do not use something else to perform the conversion for you.
About Positional Notation
In positional notation, a number in base b can be understood as a linear combination of powers of b.

The number 42, in base 10, means:

(4 * 10^1) + (2 * 10^0)

The number 101010, in base 2, means:

(1 * 2^5) + (0 * 2^4) + (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)

The number 1120, in base 3, means:

(1 * 3^3) + (1 * 3^2) + (2 * 3^1) + (0 * 3^0)

I think you got the idea!

Yes. Those three numbers above are exactly the same. Congratulations!
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/all-your-base/canonical-data.json
