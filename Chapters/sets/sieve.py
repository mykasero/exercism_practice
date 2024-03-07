def primes(limit):
    p=2
    final = []
    marked_list = []
    total_list = []
    for i in range(p,limit+1):
        total_list.append(i)
    if limit >= p:
        final.append(p)
    while len(marked_list) + len(final) < len(total_list):
        for iter1 in range(2*p,limit+1,p):
            marked_list.append(iter1)
        marked_list = list(set(marked_list))

        

        for iter2 in total_list:
            if iter2 > p and iter2 not in marked_list:
                p = iter2
                final.append(p)
                break
        if p == 997:
            break
        

    return final


'''
Introduction
You bought a big box of random computer parts at a garage sale. You've started putting the parts together to build custom computers.

You want to test the performance of different combinations of parts, and decide to create your own benchmarking program to see how your computers compare. You choose the famous "Sieve of Eratosthenes" algorithm, an ancient algorithm, but one that should push your computers to the limits.

Instructions
Your task is to create a program that implements the Sieve of Eratosthenes algorithm to find prime numbers.

A prime number is a number that is only divisible by 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers.

The Sieve of Eratosthenes is an ancient algorithm that works by taking a list of numbers and crossing out all the numbers that aren't prime.

A number that is not prime is called a "composite number".

To use the Sieve of Eratosthenes, you first create a list of all the numbers between 2 and your given number. Then you repeat the following steps:

Find the next unmarked number in your list. This is a prime number.
Mark all the multiples of that prime number as composite (not prime).
You keep repeating these steps until you've gone through every number in your list. At the end, all the unmarked numbers are prime.
'''

# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/sieve/canonical-data.json
