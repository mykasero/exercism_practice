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
    new_num = numbers.copy()
    for i in range(len(numbers)):
        while new_num[i] > 1:
            remainder = int(new_num[i] % 2)
            byte += str(remainder)
            new_num[i] = int(new_num[i] / 2)

            if len(byte) == 8:
                splitted.append(byte)
                byte = ""

            if new_num[i] == 1:
                if len(byte) < 8:
                    byte += (7 - len(byte)) * "0" + "1"
                    splitted.append(byte)
                    byte = ""
                    break
                elif len(byte) == 8:
                    splitted.append(byte)
                    byte = ""
                    break
        # for i in range(len(splitted)):
        #     splitted[i] = splitted[i][::-1]

        splitted = splitted[::-1]
        if bytes[i] > 1: # A - it's not the last octet
            splitted[0] = "1" + splitted[0][1:]

            if numbers[i] > 0 and len(splitted) > 1:
                splitted[0] = splitted[0][0] + "1" + splitted[0][2:]

            # if len(splitted) == 1:
            #     splitted.append("00000000")


        if bytes[i] > 1 and len(splitted) == 1:
            splitted.append("00000000")



    # for ctr in range(len(bytes)):
    #     for i in range(bytes[ctr]*8):
    #
    #         val += (2**i)
    #
    #         if val <= numbers[ctr]:
    #             byte += "1"
    #         elif val > numbers[ctr]:
    #             byte += "0"
    #
    #         if len(byte) == 8:
    #             splitted.append(byte)
    #             byte = ""

    # splitted = splitted[::-1]
    # for i in range(len(splitted)):
    #     splitted[i] = splitted[i][::-1]

    test = 0x7F
    stop = "StOP"

    return bin_to_dec(splitted)

def bin_to_dec(bins):
    numbers = []
    val = 0
    results = bins.copy()

    for i in range(len(results)):
        results[i] = results[i][::-1]

    for item in results:
        for j in range(len(item)):
            if item[j] == "1":
                val += (2**j)
        numbers.append(val)
        val = 0

    stop2 = "STOP"
    return numbers
def encode(numbers):
    nums = []
    if numbers == [0]:
        return [0]
    else:
        for item in numbers:
            if item < 128:
                nums.append(item)
            else:
                nums = dec_to_bin(numbers)


    return nums
def decode(bytes_):
    pass
