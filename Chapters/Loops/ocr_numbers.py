def convert(input_grid):
    DIGIT_STRINGS = [
        ' _ | ||_|   ',  # 0
        '     |  |   ',  # 1
        ' _  _||_    ',  # 2
        ' _  _| _|   ',  # 3
        '   |_|  |   ',  # 4
        ' _ |_  _|   ',  # 5
        ' _ |_ |_|   ',  # 6
        ' _   |  |   ',  # 7
        ' _ |_||_|   ',  # 8
        ' _ |_| _|   ',  # 9
    ]
    # Checking the errors

    line_ctr = 0
    col_ctr = 0
    for element in input_grid:
        for piece in element:
            col_ctr += 1
        if col_ctr % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
        col_ctr = 0
        line_ctr += 1

    if line_ctr % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # doing the task
    number_str = ""
    number_list = []
    list_digit_check = []
    digit_check = ""

    if len(input_grid) == 4:
        for three_space in range(0, len(input_grid[0]), 3):
            for iter_col in range(0, 4):
                if three_space == 0:
                    for iter_row in range(three_space, three_space + 3):
                        digit_check += input_grid[iter_col][iter_row]

                else:
                    for iter_row in range(three_space, three_space + 3):
                        digit_check += input_grid[iter_col][iter_row]

            list_digit_check.append(digit_check)
            digit_check = ""
    else:
        for four_space_col in range(0, len(input_grid), 4):
            for three_space in range(0, len(input_grid[0]), 3):
                for iter_col in range(four_space_col, four_space_col + 4):
                    if three_space == 0:
                        for iter_row in range(three_space, three_space + 3):
                            digit_check += input_grid[iter_col][iter_row]

                    else:
                        for iter_row in range(three_space, three_space + 3):
                            digit_check += input_grid[iter_col][iter_row]

                list_digit_check.append(digit_check)
                digit_check = ""

    # appending the return string
    str_ctr = 0
    for items in list_digit_check:
        if items in DIGIT_STRINGS:
            number_list.append(DIGIT_STRINGS.index(items))
            number_str += str(DIGIT_STRINGS.index(items))
            str_ctr += 1
            if len(input_grid) > 4 and str_ctr % 3 == 0 and str_ctr < len(list_digit_check) - 1:
                number_str += ","
        else:
            # if digit unrecognizable place ? instead of a digit
            number_str += "?"
    # this is specifically for the one case with 1 digit not being in the digit list

    if len(input_grid) == 4 and len(input_grid[0]) == 3 and number_str == "":
        return "?"
    else:
        return number_str