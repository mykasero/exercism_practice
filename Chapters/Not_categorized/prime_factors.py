def factors(value):
    new_val = value
    prime = 2
    divisors = []

    while new_val > 1:
        if new_val % prime == 0:
            divisors.append(prime)
            new_val = int(new_val / prime)
        else:
            prime+=1

    return divisors

print(factors(1257642))

'''
Instructions
Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.

Note that 1 is not a prime number.

Example
What are the prime factors of 60?
Our successful divisors in that computation represent the list of prime factors of 60: 2, 2, 3, and 5.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/prime-factors/canonical-data.json
