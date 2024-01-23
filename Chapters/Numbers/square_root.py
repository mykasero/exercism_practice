def square_root(number):
    return_val = 0
    val = number
    odd = []
    for odd_nums in range(1, 550, 2):
        odd.append(odd_nums)
    times_substracted = 0

    for substract in odd:
        if val > 0:
            val = val - substract
            times_substracted += 1
    return_val = times_substracted

    return return_val
