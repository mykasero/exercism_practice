'''
    Conversion is wrong. Should iterate down from the number and number % 2 > 0 new val = number%2 then add 1, else if number % 2 == 0 add 0
'''
def byte_count(numbers):
    bytes = []
    for item in numbers:
        if 0 < item < 2**7:
            bytes.append(1)
        elif 127 < item < 16_384:
            bytes.append(2)
        elif 16_383 < item < 20_971_152:
            bytes.append(3)
        elif 20_971_151 < item < 268_435_456:
            bytes.append(4)
        elif 268_435_455 < item < 4_294_967_296: #largest 32-bit = 4_294_967_295
            bytes.append(5)

    return bytes
def dec_to_bin(numbers):
    bytes = byte_count(numbers)
    byte = ""
    splitted = []
    val = 0
    for ctr in range(len(bytes)):
        for i in range(bytes[ctr]*8):

            val += (2**i)

            if val <= numbers[ctr]:
                byte += "1"
            elif val > numbers[ctr]:
                byte += "0"

            if len(byte) == 8:
                splitted.append(byte)
                byte = ""

    # splitted = splitted[::-1]
    # for i in range(len(splitted)):
    #     splitted[i] = splitted[i][::-1]

    test = 0x7F
    stop = "StOP"

    return bin_to_dec(splitted)

def bin_to_dec(bins):
    numbers = []
    val = 0

    for item in bins:
        for j in range(len(item)):
            if item[j] == "1":
                val += (2**j)
        numbers.append(val)
        val = 0

    stop2 = "STOP"
    return numbers
def encode(numbers):
    nums = dec_to_bin(numbers)
    if nums == []:
        return [0]


    return nums
def decode(bytes_):
    pass
