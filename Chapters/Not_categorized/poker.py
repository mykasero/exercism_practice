hands1 = ["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH"]
def best_hands(hands):
    straight_flush = False  # 6-10/ 7-J + same colour
    four_kind = False  # self explanatory
    full_house = False  # 3 * x + 2 * y
    flush = False  # same colour
    straight = False  # 2-6 ... J-A
    three_kind = False  # self explanatory
    two_pair = False  # self explanatory
    pair = False  # self explanatory

    # straight_flush > 4kind > full_house > flush > straight > 3kind > 2pair > pair > highcard

    splited_nums = []
    splited_colors = []

    tmp_num = ""
    tmp_color = ""
    if len(hands) == 1:
        return hands
    else:
        for items in hands:
            for item in items.split():
                tmp_num += item[0]
                tmp_color += item[1]

            splited_nums.append(tmp_num)
            splited_colors.append(tmp_color)
            tmp_num = ""
            tmp_color = ""
    print(splited_nums,splited_colors)

    for numer, color in splited_nums, splited_colors:
        print(numer, color)


print(best_hands(hands1))