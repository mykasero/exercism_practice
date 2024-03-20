def say(number):
    final = ""
    txt_num = ""

    num_to_word_1 = {0 : "zero", 1 : "one", 2 : "two", 3 : "three",
                   4 : "four", 5 : "five", 6 : "six", 7 : "seven",
                   8 : "eight", 9 : "nine"}
    num_to_word_2 = {10 : "ten", 11 : "eleven", 12 : "twelve",
                     13 : "thirteen", 14 : "fourteen", 15 : "fifteen",
                     16 : "sixteen", 17 : "seventeen", 18 : "eighteen",
                     19 : "nineteen"}
    num_to_word_3 = {2 : "twenty", 3 : "thirty", 4 : "forty",
                     5 : "fifty", 6 : "sixty", 7 : "seventy",
                     8 : "eighty", 9 : "ninety"}
    words = []
    numbers = []
    num_rev = str(number)
    print(num_rev)

    if len(num_rev) > 12 or number < 0:
        raise ValueError("input out of range")

    ctr = 0
    i = 0
    while i < len(num_rev):
        txt_num += num_rev[i]
        ctr += 1
        i += 1
        if ctr == 3:
            numbers.append(txt_num)
            txt_num = ""
            ctr = 0
    numbers = numbers[::-1]
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            #print(numbers[i][j])
            if j == 0:
                txt_num += num_to_word_1[int(numbers[i][j])] + " hundred "
                # print(num_to_word_1[int(numbers[i][j])],"hundred")
            elif j == 1:
                if numbers[i][j] == "1" and j == 1:
                    txt_num += num_to_word_2[int(numbers[i][1:])]
                    # print(num_to_word_2[int(numbers[i][1:])])
                else:
                    txt_num += num_to_word_3[int(numbers[i][j])]
                    # print(num_to_word_3[int(numbers[i][j])])
            elif j == 2 and numbers[i][1] != "1":
                txt_num += "-" + num_to_word_1[int(numbers[i][j])]
                # print(num_to_word_1[int(numbers[i][j])])
        if i == 1:
            words.append(" thousand ")
        elif i == 2:
            words.append(" million ")
        elif i == 3:
            words.append(" billion ")
        words.append(txt_num)
        txt_num = ""

    print(words[::-1])
    #print(txt_num,numbers)
    return final

print(say(879678345217))