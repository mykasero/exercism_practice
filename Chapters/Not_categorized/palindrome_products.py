from itertools import combinations_with_replacement

def palindromes(min_num, max_num, s_l):
    if s_l == "S" and min_num + 100 < max_num and min_num < 2000:
        max_num = min_num + 100
    elif s_l == "L" and min_num + 100 < max_num and min_num < 2000:
        min_num = max_num - 100

    products = []
    values = []
    combos = combinations_with_replacement([str(item) for item in range(min_num,max_num+1)], 2)

    first_half = ""
    second_half = ""

    for item in combos:
        value = int(item[0]) * int(item[1])
        str_val = str(value)
        len1 = len(str_val)

        if len(str_val) % 2 == 0:
            for i in range(int(len(str_val)/2)):
                first_half += str_val[i]
            for j in range(len(str_val)-1, int(len(str_val)/2)-1, -1):
                second_half += str_val[j]

            if first_half == second_half:
                products.append([int(item[0]),int(item[1])])
                values.append(value)
                value = 0

            first_half = second_half = ""

        elif len1 % 2 == 1:

            for i in range(int(len(str_val)/2)):
                first_half += str_val[i]
            for j in range(len(str_val)-1,int(len(str_val)/2),-1):
                second_half += str_val[j]

            if first_half == second_half:
                products.append([int(item[0]),int(item[1])])
                values.append(value)
                value = 0

            first_half = second_half = ""

    return products, values

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    else:
        numbers, values = palindromes(min_factor,max_factor,"L")
        nums = []

        for item in numbers:
            if int(item[0])*int(item[1]) == max(values):

                nums.append([int(item[0]),int(item[1])])

        if numbers == [] or values == []:
            return (None,[])
        else:
            final = (max(values),nums)

    return final


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    numbers, values = palindromes(min_factor, max_factor,"S")
    pair = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    else:
        if numbers == [] or values == []:
            return (None,[])
        else:
            for item in numbers[values.index(min(values))]:
                pair.append(int(item))

            final = tuple((min(values), [pair]))

    return final
