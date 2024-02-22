#17/26 passed
number = 16
roman = {1000 : "M", 500 : "D", 100 : "C",
         50 : "L", 10 : "X", 5 : "V", 1 : "I"}

str_number = str(number)[::-1]

final_string = ""
#max is 3999
for iter_num in range(len(str_number)-1,-1,-1):
    if iter_num == 3:
        final_string += int(str_number[iter_num]) * "M"
        print(iter_num, final_string)
    elif iter_num == 2:
        if int(str_number[iter_num]) < 4:
            final_string += int(str_number[iter_num]) * "C"
        elif int(str_number[iter_num]) == 4:
            final_string += "CD"
        elif int(str_number[iter_num]) == 5:
            final_string += "D"
        elif int(str_number[iter_num]) > 5 and int(str_number[iter_num])<9:
            final_string += f"D{(int(str_number[iter_num])-5)*roman[100]}"
        else:
            final_string += "CM"
        print(iter_num, final_string)
    elif iter_num == 1:
        if int(str_number[iter_num]) < 4:
            final_string += int(str_number[iter_num]) * "X"
        elif int(str_number[iter_num]) == 4:
            final_string += "XL"
        elif int(str_number[iter_num]) == 5:
            final_string += "L"
        elif int(str_number[iter_num]) > 5 and int(str_number[iter_num]) < 9:
            final_string += f"L{(int(str_number[iter_num])-5) * roman[10]}"
        else:
            final_string += "XC"
        print(iter_num, final_string)
    else:
        if int(str_number[iter_num]) < 4:
            final_string += int(str_number[iter_num]) * "I"
        elif int(str_number[iter_num]) == 4:
            final_string += "IV"
        elif int(str_number[iter_num]) == 5:
            final_string += "V"
        elif 5 < int(str_number[iter_num]) < 9:
            final_string += f"V{(int(str_number[iter_num])-5) * roman[1]}"
        else:
            final_string += "IX"
        print(iter_num,final_string)

print(final_string)
