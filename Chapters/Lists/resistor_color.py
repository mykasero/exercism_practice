def color_code(color):
    color_val = None

    color_val = colors().index(color)

    return color_val


def colors():
    colors_list = ["black","brown","red","orange","yellow","green",
                  "blue","violet","grey","white"]

    return colors_list