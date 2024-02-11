def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]

    actions_string = binary_str[:0:-1]

    final = []
    final_inv = []
    if binary_str == "00000":
        return final
    elif binary_str[0] == "0":
        for item in range(4):
            if actions_string[item] == "1":
                final.append(actions[item])
        return final
    else:
        for item in range(4):
            if actions_string[item] == "1":
                final.append(actions[item])

        for item2 in range(len(final) - 1, -1, -1):
            final_inv.append(final[item2])
        return final_inv

    return final