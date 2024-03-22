singles = {0: "zero", 1: "one", 2: "two", 3: "three",
           4: "four", 5: "five", 6: "six", 7: "seven",
           8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve",
         13: "thirteen", 14: "fourteen", 15: "fifteen",
         16: "sixteen", 17: "seventeen", 18: "eighteen",
         19: "nineteen"}
tens = {0: "", 2: "twenty", 3: "thirty", 4: "forty",
        5: "fifty", 6: "sixty", 7: "seventy",
        8: "eighty", 9: "ninety"}


def less_100(number):
    final = ""

    # step 1
    if number < 0:
        raise ValueError("input out of range")
    elif number < 100:
        if number < 10:
            final += singles[number]
        elif number >= 10 and number < 20:
            final += teens[number]
        else:
            if str(number)[1] == "0":
                final += tens[int(str(number)[0])]
            else:
                final += tens[int(str(number)[0])] + "-" + singles[int(str(number)[1])]

    return final


def say(number):
    final = ""

    num2 = number
    num_list = []

    words = []
    words2 = []

    test_elements = []

    if number > 999_999_999_999:
        raise ValueError("input out of range")

    elif number < 100:
        final += less_100(number)

    elif number >= 100:
        while num2 >= 1:
            num_list.append(num2 % 1000)
            num2 = int(num2 / 1000)

        print(num_list)

        # step 2-3
        for i in range(len(num_list)):
            if i == 0:
                words.append(num_list[i])
            elif i == 1:
                words.append(" thousand ")
                words.append(int(str(num_list[i])))

            elif i == 2:
                words.append(" million ")
                words.append(int(str(num_list[i])))

            elif i == 3:
                words.append(" billion ")
                words.append(int(str(num_list[i])))

        # step 4
        for item in words[::-1]:
            if len(str(item)) <= 3:
                if len(str(item)) == 3:
                    for i in range(len(str(item))):

                        if i == 0 and str(item)[i]:
                            final += singles[int(str(item)[i])] + " hundred "
                        if i == 1 and str(item)[1] == "1":
                            final += teens[int(str(item)[i:i + 1])]
                        elif i == 1 and str(item)[1] != "1":
                            if str(item)[1] == "0" and str(item)[2] != "0":
                                final += singles[int(str(item)[i + 1])]
                            elif str(item)[1] != "0" and str(item)[2] == "0":
                                final += tens[int(str(item)[i])]
                            elif str(item)[1] != "0" and str(item)[2] != "0":
                                final += tens[int(str(item)[i])] + "-" + singles[int(str(item)[i + 1])]
                    test_elements = final.split()
                else:
                    if item != 0:
                        final += less_100(item)
                    test_elements = final.split()
            else:
                test_elements = final.split()
                if test_elements[len(test_elements) - 1] in ["thousand", "million", "billion"]:
                    pass
                else:
                    final += item
    # remove whitespace at the end of the string
    if final[-1:] == " ":
        final = final.rstrip()

    return final