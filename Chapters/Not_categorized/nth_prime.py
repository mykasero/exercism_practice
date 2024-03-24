def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    n = 2
    primes = [2]

    while len(primes) < number:
        n += 1
        if all(n % p > 0 for p in primes):
            primes.append(n)

    return primes[number - 1]


'''
Instructions
Given a number n, determine what the nth prime is.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

If your language provides methods in the standard library to deal with prime numbers, pretend they don't exist and implement them yourself.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/nth-prime/canonical-data.json
