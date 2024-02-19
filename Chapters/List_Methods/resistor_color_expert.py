def resistor_label(colors):
    colors_d = {"black": 0, "brown": 1, "red": 2, "orange": 3,
                "yellow": 4, "green": 5, "blue": 6, "violet": 7,
                "grey": 8, "white": 9}

    color_tolerance = {"grey": 0.05, "violet": 0.1, "blue": 0.25,
                       "green": 0.5, "brown": 1, "red": 2,
                       "gold": 5, "silver": 10}

    multiplier = 0
    final_num = 0
    num_string = ""
    final = ""

    if len(colors) == 1:
        final = str(colors_d[colors[0]]) + " ohms"
        return final

    elif len(colors) == 4:
        multiplier = 10 ** int(colors_d[colors[2]])
        num_string = str(colors_d[colors[0]]) + str(colors_d[colors[1]])
        final_num = int(num_string) * multiplier

        if final_num < 1000:
            final = str(final_num) + " ohms" + " ±" + str(color_tolerance[colors[3]]) + "%"
            return final
        elif final_num >= 10 ** 3 and final_num < 10 ** 6:

            final_num = final_num / 10 ** 3
            if final_num.is_integer() == True:
                final = str(int(final_num)) + " kiloohms" + " ±" + str(color_tolerance[colors[3]]) + "%"
            else:
                final = str(final_num) + " kiloohms" + " ±" + str(color_tolerance[colors[3]]) + "%"
            return final

    else:
        multiplier = 10 ** int(colors_d[colors[3]])
        num_string = str(colors_d[colors[0]]) + str(colors_d[colors[1]]) + str(colors_d[colors[2]])
        final_num = int(num_string) * multiplier

        if final_num < 1000:
            final = str(final_num) + " ohms" + " ±" + str(color_tolerance[colors[4]]) + "%"
            return final

        elif final_num >= 10 ** 3 and final_num < 10 ** 6:
            final_num = final_num / 10 ** 3

            if final_num.is_integer() == True:
                final = str(int(final_num)) + " kiloohms" + " ±" + str(color_tolerance[colors[4]]) + "%"

            else:
                final = str(final_num) + " kiloohms" + " ±" + str(color_tolerance[colors[4]]) + "%"
            return final
        elif final_num >= 10 ** 6 and final_num < 10 ** 9:
            final_num = final_num / 10 ** 6
            if final_num.is_integer() == True:
                final = str(int(final_num)) + " megaohms" + " ±" + str(color_tolerance[colors[4]]) + "%"

            else:
                final = str(final_num) + " megaohms" + " ±" + str(color_tolerance[colors[4]]) + "%"
            return final
        elif final_num >= 10 ** 9 and final_num < 10 ** 12:
            final_num = final_num / 10 ** 9
            if final_num.is_integer() == True:
                final = str(int(final_num)) + " gigaohms" + " ±" + str(color_tolerance[colors[4]]) + "%"

            else:
                final = str(final_num) + " gigaohms" + " ±" + str(color_tolerance[colors[4]]) + "%"
            return final