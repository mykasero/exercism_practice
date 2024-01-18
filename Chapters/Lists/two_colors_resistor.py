def value(colors):
    colors_list = ["black", "brown", "red", "orange", "yellow", "green",
                   "blue", "violet", "grey", "white"]

    color_val = ""
    if len(colors) <= 2:
        for current_color in range(len(colors)):
            color_val += str(colors_list.index(colors[current_color]))

    else:
        for current_color in range(len(colors) - 1):
            color_val += str(colors_list.index(colors[current_color]))

    color_val = int(color_val)

    return color_val
