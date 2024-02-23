def roman(number):
    roman = {1000: "M", 900: "CM", 600: "DC", 500: "D", 400: "CD",
             100: "C", 90: "XC", 60: "LX", 50: "L", 40: "XL",
             10: "X", 9: "IX", 6: "VI", 5: "V", 4: "IV", 1: "I"}
    str_number = str(number)

    final_string = ""
    # max is 3999
    list_of_elements = []
    pwr = len(str_number) - 1
    for item in str_number:
        list_of_elements.append((10 ** pwr) * int(item))
        pwr -= 1

    for element in list_of_elements:
        if element >= 1000:
            final_string += f"{int(element / 1000) * roman[1000]}"
        elif 600 < element < 900:
            final_string += f"D{(int((element / 100)) - 5) * roman[100]}"
        ###etc worth trying
        elif 100 < element < 400:
            final_string += f"{(int(element / 100)) * roman[100]}"
        elif 60 < element < 90:
            final_string += f"L{(int((element / 10)) - 5) * roman[10]}"
        elif 10 < element < 40:
            final_string += f"{(int(element / 10)) * roman[10]}"
        elif 6 < element < 9:
            final_string += f"V{(int(element - 5)) * roman[1]}"
        elif 1 < element < 4:
            final_string += f"{int(element) * roman[1]}"
        else:
            if element == 0:
                pass
            else:
                final_string += roman[element]

    return final_string

