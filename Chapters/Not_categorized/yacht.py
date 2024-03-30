# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    numbers = {1: 0, 2: 0, 3: 0,
               4: 0, 5: 0, 6: 0}

    sum = 0
    if category == ONES:
        for item in dice:
            if item == 1:
                sum += 1
        return sum
    elif category == TWOS:
        for item in dice:
            if item == 2:
                sum += 2
        return sum
    elif category == THREES:
        for item in dice:
            if item == 3:
                sum += 3
        return sum
    elif category == FOURS:
        for item in dice:
            if item == 4:
                sum += 4
        return sum
    elif category == FIVES:
        for item in dice:
            if item == 5:
                sum += 5
        return sum
    elif category == SIXES:
        for item in dice:
            if item == 6:
                sum += 6
        return sum
    elif category == FULL_HOUSE:
        for number in dice:
            numbers[number] += 1
        non_zero = list(set(list(numbers.values())))
        if non_zero[0] == 0:
            non_zero.pop(0)
        if len(non_zero) == 2 and non_zero[0] in [2, 3]:
            for item in dice:
                sum += item
        else:
            sum = 0

        return sum

    elif category == FOUR_OF_A_KIND:
        for number in dice:
            numbers[number] += 1

        non_zero = list(set(list(numbers.values())))

        if non_zero[0] == 0:
            non_zero.pop(0)
        else:
            pass

        if non_zero[0] == 1 or non_zero[0] == 4:
            for item in dice:
                if item == list(numbers.keys())[list(numbers.values()).index(4)]:
                    sum += item

        elif len(non_zero) == 1:
            for item in dice:
                sum += item
            sum -= dice[0]

        else:
            sum = 0

        return sum

    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            sum = 30
        else:
            sum = 0

        return sum

    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            sum = 30
        else:
            sum = 0

        return sum
    elif category == CHOICE:
        for item in dice:
            sum += item

        return sum

    elif category == YACHT:
        if len(set(dice)) == 1:
            sum = 50
        return sum