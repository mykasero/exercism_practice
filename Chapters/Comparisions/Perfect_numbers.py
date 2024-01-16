def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    num_list = []
    what_type = ""
    total = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        what_type = "perfect"
    elif total > number:
        what_type = "abundant"
    elif total < number:
        what_type = "deficient"

    return what_type