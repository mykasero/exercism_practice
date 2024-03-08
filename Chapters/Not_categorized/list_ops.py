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
