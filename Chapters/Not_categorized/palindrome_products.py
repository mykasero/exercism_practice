from itertools import combinations_with_replacement

def palindromes(min_num, max_num):
    products = []
    values = []
    combos = combinations_with_replacement([str(item) for item in range(min_num,max_num+1)], 2)

    for item in combos:
        value = int(item[0]) * int(item[1])
        str_val = str(value)
        len1 = len(str_val)
        if len(str_val) % 2 == 0:
            #print( sorted(sorted(str_val[:len1 - int(len1/2)]), " ||| ", str_val[len1-(int((len1/2))) : len1]))
            if sorted(str_val[:len1 - int(len1/2)]) == \
                    sorted(str_val[len1 - (int((len1 / 2))): len1]):

                products.append([int(item[0]), int(item[1])])
                # products.append(item)
                values.append(value)
                value = 0

        elif len1 % 2 == 1:
            # int(len1/2) = half-1, so for the 2nd half just int(len1/2)+2
            #print(sorted(str_val[:int(len1/2)]), " ||| ", sorted(str_val[int(len1/2)+1:len1]))
            if sorted(str_val[:int(len1/2)]) == sorted(str_val[int(len1/2)+1:len1]):
                products.append(item)
                values.append(value)
                value = 0

    TEST = "STOP"



    return products, values

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    numbers, values = palindromes(min_factor,max_factor)

    final = (max(values), [numbers[values.index(max(values))]])

    STOP1 = "s"
    return final


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    numbers, values = palindromes(min_factor, max_factor)

    final = (min(values), [list(set(numbers[values.index(min(values))]))])

    TEST = "STOP"

    return final
