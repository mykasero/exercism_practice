def proverb(*input_data,qualifier):
    final = []
    line = ""

    if len(input_data) == 0:
        return final
    elif len(input_data) == 1:
        if qualifier:
            final.append("And all for the want of a " + qualifier + " " + input_data[0] + ".")
        else:
            final.append("And all for the want of a " + input_data[0] + ".")

    else:

        if qualifier:
            for item in range(len(input_data)-1):
                line = "For want of a " + input_data[item] + " the " + input_data[item+1] + " was lost."
                final.append(line)
            final.append("And all for the want of a " + qualifier + " " + input_data[0] + ".")
        else:
            for item in range(len(input_data)-1):
                line = "For want of a " + input_data[item] + " the " + input_data[item+1] + " was lost."
                final.append(line)
            final.append("And all for the want of a " + input_data[0] + ".")


    return final
