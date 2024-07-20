def triplets_with_sum(number):
    final = []

    for a in range(1, number // 3 + 1):
        for b in range(a, (number - a)//2 +1):
            c = number - a - b

            if (a * a) + (b * b) == c * c:
                final.append([a,b,c])

    return final

'''
Instructions
A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

a² + b² = c²
and such that,

a < b < c
For example,

3² + 4² = 5².
Given an input integer N, find all Pythagorean triplets for which a + b + c = N.

For example, with N = 1000, there is exactly one Pythagorean triplet for which a + b + c = 1000: {200, 375, 425}.

NOTE: The description above mentions mathematical sets, but also that a Pythagorean Triplet {a, b, c} must be ordered such that a < b < c (ascending order). 
This makes Python's set type unsuited to this exercise, since it is an inherently unordered container. Therefore please return a list of lists instead (i.e. [[a, b, c]]). 
You can generate the triplets themselves in whatever order you would like, as the enclosing list's order will be ignored in the tests.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pythagorean-triplet/canonical-data.json
