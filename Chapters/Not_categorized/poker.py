VALUES = {"J" : "11", "Q" : "12", "K" : "13", "A" : "14"}

'''
Notes:

Remake functions to return indexes instead of the lists so you can pull the return value from the OG list

Apply working with J,Q,K,A values


'''

def best_hands(hands):
    final = []
    _tmp_hands = []
    new_hands = []
    for hand in hands:
        for card in hand.split():
            if card[0] in VALUES:
                # print(card)
                card = card.replace(card[0],VALUES[card[0]])
                _tmp_hands.append(card)
            else:
                _tmp_hands.append(card)
        new_hands.append(_tmp_hands)
        _tmp_hands = []

    new_hands = split_hands(new_hands)

    numbers = separate_numbers(new_hands)
    colors = separate_colors(new_hands)
    #print(numbers,colors)

    _val_ctr = 0
    _vals = []
    _card = ""
    _hands = ""

    if len(split_to_normal(straight_flush(numbers,colors))) > 0:
        print("straight_flush")
        for cards in split_to_normal(straight_flush(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(four_kind(numbers,colors))) > 0:
        print("four_kind")
        for cards in split_to_normal(four_kind(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(full_house(numbers,colors))) > 0:
        print("full house")
        for cards in split_to_normal(full_house(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(straight(numbers,colors))) > 0:
        print("straight")
        for cards in split_to_normal(straight(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(three_kind(numbers,colors))) > 0:
        print("three kind")
        for cards in split_to_normal(three_kind(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(two_pair(numbers,colors))) > 0:
        print("2pair")
        for cards in split_to_normal(two_pair(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(one_pair(numbers,colors))) > 0:
        print("pair")
        for cards in split_to_normal(one_pair(numbers,colors)):
            final.append(cards)
    else:
        print("high card")

        # needs rework, its not about highest score but about highest card
        for hand in new_hands:
            for card in hand:
                # print(card)
                if len(card) > 2:
                    _val_ctr += int(card[0])*10 + int(card[1])
                else:
                    _val_ctr += int(card[0])
            _vals.append(_val_ctr)
            _val_ctr = 0

        final = [hands[_vals.index(max(_vals))]]
    print(final)
    return final

def split_hands(hands):
    splited_hands = []
    hand1 = []
    for hand in hands:
        hand1 = []
        for cards in hand:
            if len(cards) > 2:
                hand1.append((cards[0],cards[1],cards[2]))
            else:
                hand1.append((cards[0],cards[1]))
        splited_hands.append(hand1)

    return splited_hands

def split_to_normal(hands):
    normal = []
    one_card = ""
    _ctr2 = 0
    final = []
    for item in range(0, len(hands), 2):
        while len(normal) < 5:
            # if len(hands[item][_ctr2]) > 1:
            #     print(hands[item][_ctr2])
            #     # one_card = hands[item][_ctr2] + hands[item][_ctr2+1] + hands[item + 2][_ctr2]
            #     # _ctr2 += 1
            #     # normal.append(one_card)
            # else:
            one_card = hands[item][_ctr2] + hands[item+1][_ctr2]
            _ctr2 +=1
            normal.append(one_card)
        final.append(normal)
        normal = []
        _ctr2 = 0

    return final

def separate_numbers(hands):
    numbers = []
    _number = []
    _txtnum = " "
    for hand in hands:
        for card in hand:
            if len(card) > 2:
                _txtnum = card[0] + card[1]
                _number.append(_txtnum)
                _txtnum = ""
            else:
                _number.append(card[0])
        numbers.append(_number)
        _number = []

    return numbers

def separate_colors(hands):
    colors = []
    _color = []
    for hand in hands:
        for card in hand:
            if len(card) > 2:
                _color.append(card[2])
            else:
                _color.append(card[1])
        colors.append(_color)
        _color = []

    return colors

#return empty list if no straight flush
def straight_flush(numbers,colors):
    result = False
    s_f_tmp = []
    _single_digit = []
    _double_digit = []
    _total = []
    for hand in numbers:
        for card in hand:
            if len(card) > 1:
                _double_digit.append(card)
            else:
                _single_digit.append(card)
        _double_digit.sort()
        _single_digit.sort()
        _total.append(_single_digit)
        _total.append(_double_digit)
        _double_digit = []
        _single_digit = []


    numbers = [_total[0] + _total[1], _total[2] + _total[3] ]


    final = []

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 5 and len(list(set(colors[hand]))) == 1:
            for card in range(len(numbers[hand])-1):
                if int(numbers[hand][card]) == int(numbers[hand][card+1])-1:
                    s_f_tmp.append("True")
        if len(list(set(s_f_tmp))) == 1 and len(s_f_tmp) > 3 :
            final.append(numbers[hand])
            final.append(colors[hand])
            s_f_tmp = []
        else:
            s_f_tmp = []
    # print(final)
    return final

def four_kind(numbers,colors):
    final = []

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 2:
            final.append(numbers[hand])
            final.append(colors[hand])

    return final

def full_house(numbers,colors):
    count1 = 0
    count2 = 0
    final = []
    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 2:
            for item in numbers[hand]:
                if item == numbers[hand][0]:
                    count1 += 1
                elif item == numbers[hand][len(numbers[hand])-1]:
                    count2 += 1
        if count1 in [3,2] and count2 in [3,2]:
            final.append(numbers[hand])
            final.append(colors[hand])

    return final

def flush(numbers,colors):
    final = []
    for hand in range(len(colors)):
        if len(list(set(colors[hand]))) == 1:
            final.append(numbers[hand])
            final.append(colors[hand])

    return final

def straight(numbers,colors):
    final = []

    s_tmp = []

    for item in numbers:
        item.sort()

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 5:
            for card in range(len(numbers[hand])-1):
                if int(numbers[hand][card]) == int(numbers[hand][card+1])-1:
                    s_tmp.append("True")
                else:
                    s_tmp.append("False")

        if len(list(set(s_tmp))) == 1 and list(set(s_tmp))[0] != "False":
            final.append(numbers[hand])
            final.append(colors[hand])
            s_tmp = []
        else:
            s_tmp = []

    return final

def three_kind(numbers,colors):
    final = []
    _ctr1 = 0
    _ctr2 = 0
    _ctr3 = 0


    for item in numbers:
        item.sort()

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 3:
            for card in numbers[hand]:
                if card == numbers[hand][0]:
                    _ctr1 += 1
                elif card == numbers[hand][1]:
                    _ctr2 += 1
                elif card == numbers[hand][2]:
                    _ctr3 += 1
        if _ctr1 == 3 or _ctr2 == 3 or _ctr3 == 3:
            final.append(numbers[hand])
            final.append(colors[hand])
            _ctr1 = _ctr2 = _ctr3 = 0
    return final

def two_pair(numbers,colors):
    final = []
    _ctr1 = 0
    _ctr2 = 0
    _ctr3 = 0


    for item in numbers:
        item.sort()

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 3:
            for card in numbers[hand]:
                if card == numbers[hand][0]:
                    _ctr1 += 1
                elif card == numbers[hand][1]:
                    _ctr2 += 1
                elif card == numbers[hand][2]:
                    _ctr3 += 1
        if _ctr1 == 2 and _ctr2 == 2 or _ctr2 == 2 and _ctr3 == 2 or _ctr3 == 2 and _ctr1 == 2:
            final.append(numbers[hand])
            final.append(colors[hand])
            _ctr1 = _ctr2 = _ctr3 = 0

    return final

def one_pair(numbers,colors):
    final = []
    _ctr1 = 0
    _ctr2 = 0
    _ctr3 = 0
    _ctr4 = 0

    for item in numbers:
        item.sort()

    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 4:
            for card in numbers[hand]:
                if card == numbers[hand][0]:
                    _ctr1 += 1
                elif card == numbers[hand][1]:
                    _ctr2 += 1
                elif card == numbers[hand][2]:
                    _ctr3 += 1
                elif card == numbers[hand][3]:
                    _ctr4 += 1
        if _ctr1 == 2 or _ctr2 == 2 or _ctr3 == 2 or _ctr4 == 2:
            final.append(numbers[hand])
            final.append(colors[hand])
            _ctr1 = _ctr2 = _ctr3 = _ctr4 = 0

    return final

print(best_hands(["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH"]))
