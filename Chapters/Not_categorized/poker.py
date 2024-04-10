values = {"J" : 12, "Q" : 13, "K" : 14, "A" : 15}

'''
Notes:

Remake functions to return indexes instead of the lists so you can pull the return value from the OG list

Apply working with J,Q,K,A values


'''

def best_hands(hands):
    final = []

    new_hands = hands.copy()
    new_hands = split_hands(hands)

    numbers = separate_numbers(new_hands)
    colors = separate_colors(new_hands)

    _val_ctr = 0
    _vals = []
    _card = ""
    _hands = ""

    if len(split_to_normal(straight_flush(numbers,colors))) > 0:
        for cards in split_to_normal(straight_flush(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(four_kind(numbers,colors))) > 0:
        for cards in split_to_normal(four_kind(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(full_house(numbers,colors))) > 0:
        for cards in split_to_normal(full_house(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(straight(numbers,colors))) > 0:
        for cards in split_to_normal(straight(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(three_kind(numbers,colors))) > 0:
        for cards in split_to_normal(three_kind(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(two_pair(numbers,colors))) > 0:
        for cards in split_to_normal(two_pair(numbers,colors)):
            final.append(cards)
    elif len(split_to_normal(one_pair(numbers,colors))) > 0:
        for cards in split_to_normal(one_pair(numbers,colors)):
            final.append(cards)
    else:
        for hand in new_hands:
            for card in hand:
                _val_ctr += int(card[0])
            _vals.append(_val_ctr)
            _val_ctr = 0

        final = [hands[_vals.index(max(_vals))]]

    return final

def split_hands(hands):
    splited_hands = []
    hand1 = []
    for hand in hands:
        hand1 = []
        for cards in hand.split():
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
    for hand in hands:
        for card in hand:
            _number.append(card[0])
        numbers.append(_number)
        _number = []

    return numbers

def separate_colors(hands):
    colors = []
    _color = []
    for hand in hands:
        for card in hand:
            _color.append(card[1])
        colors.append(_color)
        _color = []

    return colors

#return empty list if no straight flush
def straight_flush(numbers,colors):
    result = False
    s_f_tmp = []

    final = []
    for item in numbers:
        item.sort()
    for hand in range(len(numbers)):
        if len(list(set(numbers[hand]))) == 5 and len(list(set(colors[hand]))) == 1:
            for card in range(len(numbers[hand])-1):
                if int(numbers[hand][card]) == int(numbers[hand][card+1])-1:
                    s_f_tmp.append("True")
        if len(list(set(s_f_tmp))) == 1:
            final.append(numbers[hand])
            final.append(colors[hand])
            s_f_tmp = []
        else:
            s_f_tmp = []

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

print(best_hands(["5S 3S 2S 8S 11H", "5H 4C 8C JC JC"]))