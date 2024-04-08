def best_hands(hands):
    hands = serialize(hands)
    return [
        deserialize(hand)
        for hand in hands
        if card_ranks(hand) == card_ranks(max(hands, key=hand_rank))
    ]

def serialize(hands):
    # split card into number and color tuple
    _hands = []
    for hand in hands:
        _hand = []
        for card in hand.split():
            _hand.append((card[-2],card[-1]))  #ori bylo -2 i -1 (?)
        _hands.append(_hand)
    return _hands

def deserialize(hand):
    #return to original form
    return " ".join(["".join(["10" if r == "0" else r, s]) for r, s in hand])

def hand_rank(hand):
    #"return ranking of serialized hand"
    ranks = card_ranks(hand)
    groups = [(ranks.count(i), i) for i in set(ranks)]
    groups.sort(reverse=True)
    counts, number = zip(*groups)
    straight = (len(counts) == 5) and (max(number)-min(number)==4)
    flush = len(set([s for r, s in hand])) == 1

    return (
        8 if straight and flush else
        7 if counts == (4, 1) else
        6 if counts == (3, 2) else
        5 if flush else
        4 if straight else
        3 if counts == (3, 1, 1) else
        2 if counts == (2, 2, 1) else
        1 if counts == (2, 1, 1, 1) else
        0, number
    )

def card_ranks(hand):
    ranks = ["--234567890JQKA".index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


'''
My own iteration (in progress:

def best_hands(hands):
    hands = split_hands(hands)
    # print(hands)
    numbers = separate_numbers(hands)
    colors = separate_colors(hands)
    print(numbers," //// ",colors)
    s_f = straight_flush(numbers,colors)

    # print(numbers)
    # print(colors)
    test1 = split_to_normal(s_f)
    print(test1)


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
    _ctr = 0
    _ctr2 = 0

    while len(normal) < 5:
        one_card = hands[_ctr][_ctr2] + hands[_ctr+1][_ctr2]
        _ctr2 +=1
        normal.append(one_card)

    return normal

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

def straight_flush(numbers,colors):
    result = False
    s_f_tmp = []

    final = []
    print(numbers,colors)
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
            print(final)
            s_f_tmp = []
        else:
            s_f_tmp = []

    return final


print(best_hands(["7S 4S 5S 6S 8S", "3H 4H 5C 6C JD"]))
'''
