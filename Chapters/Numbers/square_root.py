'''
Instructions
Given a natural radicand, return its square root.

Note that the term "radicand" refers to the number for which the root is to be determined. That is, it is the number under the root symbol.

Check out the Wikipedia pages on square root and methods of computing square roots.

Recall also that natural numbers are positive real whole numbers (i.e. 1, 2, 3 and up).

How this Exercise is Structured in Python
Python offers a wealth of mathematical functions in the form of the math module and built-ins such as pow() and sum(). However, we'd like you to consider the challenge of solving this exercise without those built-ins or modules.

While there is a mathematical formula that will find the square root of any number, we have gone the route of having only natural numbers (positive integers) as solutions.
'''

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
