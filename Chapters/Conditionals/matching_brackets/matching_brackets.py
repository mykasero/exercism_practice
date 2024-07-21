def is_paired(input_string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    is_true = False

    for bracket in input_string:
        if bracket in open_list:
            stack.append(bracket)
        elif bracket in close_list:
            pos = close_list.index(bracket)
            if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

    else:
        return False
'''
Instructions
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
verify that any and all pairs are matched and nested correctly. 
The string may also contain other characters, which for the purposes of this exercise should be ignored.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/matching-brackets/canonical-data.json
