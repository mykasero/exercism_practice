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

'''
Instructions
The dice game Yacht is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor. 
In the game, five dice are rolled and the result can be entered in any of twelve categories. The score of a throw of the dice depends on category chosen.

Scores in Yacht
Category	Score	Description	Example
Ones	1 × number of ones	Any combination	1 1 1 4 5 scores 3
Twos	2 × number of twos	Any combination	2 2 3 4 5 scores 4
Threes	3 × number of threes	Any combination	3 3 3 3 3 scores 15
Fours	4 × number of fours	Any combination	1 2 3 3 5 scores 0
Fives	5 × number of fives	Any combination	5 1 5 2 5 scores 15
Sixes	6 × number of sixes	Any combination	2 3 4 5 6 scores 6
Full House	Total of the dice	Three of one number and two of another	3 3 3 5 5 scores 19
Four of a Kind	Total of the four dice	At least four dice showing the same face	4 4 4 4 6 scores 16
Little Straight	30 points	1-2-3-4-5	1 2 3 4 5 scores 30
Big Straight	30 points	2-3-4-5-6	2 3 4 5 6 scores 30
Choice	Sum of the dice	Any combination	2 3 3 4 6 scores 18
Yacht	50 points	All five dice showing the same face	4 4 4 4 4 scores 50

If the dice do not satisfy the requirements of a category, the score is zero. 
If, for example, Four Of A Kind is entered in the Yacht category, zero points are scored. 
A Yacht scores zero if entered in the Full House category.

Task
Given a list of values for five dice and a category, your solution should return the score of the dice for that category. 
If the dice do not satisfy the requirements of the category your solution should return 0. 
You can assume that five values will always be presented, and the value of each will be between one and six inclusively. 
You should not assume that the dice are ordered.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/yacht/canonical-data.json
