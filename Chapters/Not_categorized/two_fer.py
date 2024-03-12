def two_fer(*arg):
    return "One for "+str(arg[0])+", one for me." if arg else "One for you, one for me."

'''
Introduction
In some English accents, when you say "two for" quickly, it sounds like "two fer". Two-for-one is a way of saying that if you buy one, you also get one for free. So the phrase "two-fer" often implies a two-for-one offer.

Imagine a bakery that has a holiday offer where you can buy two cookies for the price of one ("two-fer one!"). You go for the offer and (very generously) decide to give the extra cookie to a friend.

Instructions
Your task is to determine what you will say as you give away the extra cookie.

If your friend likes cookies, and is named Do-yun, then you will say:

One for Do-yun, one for me.
If your friend doesn't like cookies, you give the cookie to the next person in line at the bakery. Since you don't know their name, you will say you instead.

One for you, one for me.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/two-fer/canonical-data.json
