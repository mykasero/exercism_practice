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
