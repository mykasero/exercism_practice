#Needs a re-do, prob best to split into separate functions

def rectangles(strings):
    final = 0

    ctr_plus = 0
    ctr_pause = 0
    ctr_wall = 0

    ctrs = []

    if len(strings) in [0, 1]:
        return 0
    else:
        for string in strings:
            for item in string:
                if item == "+":
                    ctr_plus += 1
                elif item == "-":
                    ctr_pause += 1
                elif item == "|":
                    ctr_wall += 1

            ctrs.append([ctr_plus, ctr_pause, ctr_wall])
            ctr_plus = 0
            ctr_pause = 0

    if ctrs[0][0] - 1 == ctrs[0][1] and len(strings) < 4:
        final = ctrs[0][1]

    elif ctrs[0][0] > 0 and ctrs[0][1] == 0:
        for pluses in ctrs:
            ctr_pause += pluses[1]
        if ctr_pause == 0:
            final = 1
    else:
        for items in ctrs:
            ctr_plus += items[0]
            ctr_pause += items[1]
        if ctr_plus == ctr_pause:
            final = 1

    return final

