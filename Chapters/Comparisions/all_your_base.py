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

    # return

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



