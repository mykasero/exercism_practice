def flatten(iterable):
    final = []

    for item in iterable:
        if isinstance(item,list):
            final.extend(flatten(item))
        elif item is not None:
            final.append(item)

    return final

'''
Instructions
Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For example:

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/flatten-array/canonical-data.json
