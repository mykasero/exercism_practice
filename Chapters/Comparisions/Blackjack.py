"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 1}
    total_value = 0
    # for cards in card:
    if card in card_symbol_val:
        total_value += card_symbol_val[card]
    else:
        total_value += int(card)

    return total_value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 1}
    value_one = 0
    value_two = 0
    return_val = None
    if card_one in card_symbol_val:
        value_one = card_symbol_val.get(card_one)
    else:
        value_one = int(card_one)

    if card_two in card_symbol_val:
        value_two = card_symbol_val.get(card_two)
    else:
        value_two = int(card_two)


    if value_one == value_two:
        return_val =  (card_one,card_two)
    elif int(value_one) > int(value_two):
        return_val = card_one
    elif int(value_two) > int(value_one):
        return_val = card_two

    return return_val


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 11}
    value_one = 0
    value_two = 0
    hand_value = 0
    ace_value = 0

    if card_one in card_symbol_val:
        value_one = card_symbol_val.get(card_one)
    else:
        value_one = int(card_one)

    if card_two in card_symbol_val:
        value_two = card_symbol_val.get(card_two)
    else:
        value_two = int(card_two)

    hand_value = value_one + value_two

    if hand_value + 11 >= 22:
        ace_value = 1
    elif hand_value + 11 <= 21:
        ace_value = 11



    return ace_value


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    is_true = False

    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 11}
    value_one = 0
    value_two = 0

    if card_one in card_symbol_val:
        value_one = card_symbol_val.get(card_one)
    else:
        value_one = int(card_one)

    if card_two in card_symbol_val:
        value_two = card_symbol_val.get(card_two)
    else:
        value_two = int(card_two)

    if value_one + value_two == 21:
        is_true = True
    else:
        pass

    return is_true


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    can_split = False

    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 11}
    value_one = 0
    value_two = 0

    if card_one in card_symbol_val:
        value_one = card_symbol_val.get(card_one)
    else:
        value_one = int(card_one)

    if card_two in card_symbol_val:
        value_two = card_symbol_val.get(card_two)
    else:
        value_two = int(card_two)

    if value_one == value_two:
        can_split = True
    else:
        pass

    return can_split




def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    is_true = False

    card_symbol_val = {"K" : 10, "Q" : 10, "J" : 10, "A" : 1}
    value_one = 0
    value_two = 0

    if card_one in card_symbol_val:
        value_one = card_symbol_val.get(card_one)
    else:
        value_one = int(card_one)

    if card_two in card_symbol_val:
        value_two = card_symbol_val.get(card_two)
    else:
        value_two = int(card_two)

    if value_one + value_two in [9,10,11]:
        is_true = True
    else:
        pass

    return is_true