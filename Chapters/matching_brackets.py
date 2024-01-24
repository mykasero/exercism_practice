def is_paired(input_string):
    opening_b = []
    closing_b = []
    total = []
    is_true = False

    if len(input_string) == 0:
        is_true = True

    elif " " in input_string:
        is_true = False
    else:
        for bracket in input_string:
            if bracket in ["[", "{", "("]:
                opening_b.append(bracket)
            elif bracket in ["]", "}", ")"]:
                closing_b.append(bracket)
        # total = opening_b + closing_b

        for iter in range(len(total)):
            if opening_b[iter] + closing_b[iter] in ["{}", "()", "[]"]:
                is_true = True
            else:
                is_true = False
                break

    return is_true
