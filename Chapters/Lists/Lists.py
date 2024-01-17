"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    final_list = []

    for next_num_add_val in range(3):
        final_list.append(number + next_num_add_val)

    return final_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    final_list = []

    if rounds_1 == [] and len(rounds_1) == 0 and rounds_2 == [] and len(rounds_2) == 0:
        pass
    else:
        for rounds1 in rounds_1:
            if rounds1 != []:
                final_list.append(rounds1)
        for rounds2 in rounds_2:
            if rounds2 != []:
                final_list.append(rounds2)

    return final_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    is_true = False

    if number in rounds:
        is_true = True

    return is_true


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    avg_val = 0.0
    for card in hand:
        avg_val += card

    avg_val = avg_val / len(hand)

    return avg_val


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    is_true = False
    avg_val = 0
    for card in hand:
        avg_val += card

    avg_val = avg_val / len(hand)

    if hand[int((len(hand) / 2) - 0.5)] == avg_val or (
            (hand[0] + hand[len(hand) - 1]) / 2 == avg_val or (
            hand[int((len(hand) / 2) - 0.5)] == avg_val and (hand[0] + hand[len(hand) - 1]) / 2)):
        is_true = True

    return is_true


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    is_true = False

    list_odd = []
    list_even = []
    odd_sum_val = 0
    even_sum_val = 0

    for odd in range(0, len(hand), 2):
        list_odd.append(hand[odd])
        odd_sum_val += hand[odd]

    for even in range(1, len(hand), 2):
        list_even.append(hand[even])
        even_sum_val += hand[even]

    odd_avg_val = odd_sum_val / len(list_odd)
    even_avg_val = even_sum_val / len(list_even)

    if odd_avg_val == even_avg_val:
        is_true = True

    return is_true


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[len(hand) - 1] == 11:
        hand[len(hand) - 1] = 22
    else:
        pass

    return hand