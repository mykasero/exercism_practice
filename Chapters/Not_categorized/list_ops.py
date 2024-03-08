def append(list1, list2):
    final = []
    final = list1 + list2
    return final


def concat(lists):
    final = []

    for list in lists:
        final += list

    return final


def filter(function, list):
    final = []
    for number in list:
        if number % 2 == 1:
            final.append(number)

    return final


def append(list1, list2):
    final = []
    final = list1 + list2
    return final


def concat(lists):
    final = []

    for list in lists:
        final += list

    return final


def filter(function, list):
    final = []
    for number in list:
        if function(number):
            final.append(number)

    return final


def length(list):
    return len(list)


def map(function, list):
    final = []
    for item in list:
        final.append(function(item))
    return final


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]


def length(list):
    return len(list)


def map(function, list):
    final = []
    for item in list:
        final.append(item + 1)
    return final


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]

'''
Instructions
Implement basic list operations.

In functional languages list operations like length, map, and reduce are very common. Implement a series of basic list operations, without using existing functions.

The precise number and names of the operations to be implemented will be track dependent to avoid conflicts with existing names, but the general operations you will implement include:

append (given two lists, add all items in the second list to the end of the first list);
concatenate (given a series of lists, combine all items in all lists into one flattened list);
filter (given a predicate and a list, return the list of all items for which predicate(item) is True);
length (given a list, return the total number of items within it);
map (given a function and a list, return the list of the results of applying function(item) on all items);
foldl (given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left);
foldr (given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right);
reverse (given a list, return a list with all the original items, but in reversed order).
Note, the ordering in which arguments are passed to the fold functions (foldl, foldr) is significant.
'''

# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/list-ops/canonical-data.json
