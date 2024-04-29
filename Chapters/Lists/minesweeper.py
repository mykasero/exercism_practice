def annotate(minefield):
    # Function body starts here
    final_str = ""
    final_field = []
    numbers = ""
    same = []
    number = 0

    not_s = [None,None,None,None,None,None,None,None]

    for item in minefield:
        for i in range(1,len(item)):
            if item[0] == item[i]:
                same.append(True)
            else:
                same.append(False)

    for item in minefield[1:]:
        if len(item) != len(minefield[0]):
            raise ValueError("The board is invalid with current input.")

    for lines in minefield:
        for item in lines:
            if item not in [" ","*"]:
                raise ValueError("The board is invalid with current input.")



    if minefield == []:
        return []

    elif minefield[0] == "":
        return [""]

    elif all(same) and len(minefield[0]) > 1:
        return minefield

    else:
        '''
        loop over each element
        loop over row above if exists, the same row, row below if exists
        count the mines
        '''

        for i in range(len(minefield)):
            for j in range(len(minefield[i])):
                if minefield[i][j] != "*":
                    if len(minefield) == 1:
                        if j < len(minefield[0])-1:

                            if minefield[0][j+1] == "*": #check right
                                number += 1

                        if j > 0:

                            if minefield[0][j-1] == "*": #check left
                                number += 1

                        if 0 < j < len(minefield[0]) - 1:

                            if minefield[0][j - 1] == " " and minefield[0][j + 1] == " ":
                                number = 99

                    elif len(minefield) > 1 and len(minefield[0]) == 1:
                        if i < len(minefield)-1:

                            if minefield[i+1][0] == "*":
                                number += 1 # check below

                        if i > 0:

                            if minefield[i-1][0] == "*": # check above
                                number += 1

                        if 0 < i < len(minefield) - 1:

                            if minefield[i-1][0] == " " and minefield[i+1][0] == " ":
                                number = 99

                    else:
                        if i < len(minefield)-1:

                            if minefield[i + 1][j] == "*":  # check below
                                number += 1
                            else:
                                not_s[6] = True

                            if j < len(minefield[i])-1:

                                if minefield[i+1][j+1] == "*": #check bot right
                                    number += 1
                                else:
                                    not_s[7] = True

                            if j > 0:
                                if minefield[i+1][j-1] == "*": #check bot left
                                    number += 1
                                else:
                                    not_s[5] = True
                        if i > 0:

                            if minefield[i - 1][j] == "*":  # check above
                                number += 1
                            else:
                                not_s[1] = True

                            if j > 0:
                                if minefield[i-1][j-1] == "*": #check top left
                                    number += 1
                                else:
                                    not_s[0] = True

                            if j < len(minefield[i])-1:

                                if minefield[i-1][j+1] == "*": #check top right
                                    number += 1
                                else:
                                    not_s[2] = True

                                if minefield[i][j + 1] == "*":  # check right
                                    number += 1
                                else:
                                    not_s[4] = True

                        if j > 0:

                            if minefield [i][j-1] == "*": #check left
                                number += 1
                            else:
                                not_s[3] = True

                            if j < len(minefield[i]) - 1 and i == 0:
                                if minefield[i][j + 1] == "*":  # check right
                                    number += 1
                                else:
                                    not_s[4] = True

                        if j == 0 and i == 0:

                            if minefield[i][j + 1] == "*":  # check right
                                number += 1
                            else:
                                not_s[4] = True


                    if number > 0:
                        if number == 99:
                            numbers += " "
                            number = 0

                        else:
                            numbers += str(number)
                            number = 0

                        not_s = [None, None, None, None, None, None, None, None]

                    else:
                        flags = []
                        for item in not_s:
                            if item is not None:
                                flags.append(item)

                        if len(list(set(flags))) == 1 and list(set(flags))[0] == True:
                            number = 0
                            numbers += "C"
                            flags = []
                        else:
                            number = 0
                            numbers += str(number)
                            flags = []

                        not_s = [None, None, None, None, None, None, None, None]

                else:
                    numbers += "0"


            if i == len(minefield)-1:
                final_str += numbers

            else:
                if len(minefield[0]) == 1:
                    final_str += numbers

                else:
                    final_str += numbers + " "


            numbers = ""

    final_str = final_str.replace("0","*")
    if len(minefield) == 1:
        final_field.append(final_str)

    elif len(minefield) > 1 and len(minefield[0]) == 1:
        for item in final_str:
            final_field.append(item)
    else:
        final_field = final_str.split()

        for item in range(len(final_field)):
            if "C" in final_field[item]:
                final_field[item] = final_field[item].replace("C"," ")

    return final_field


'''
Introduction
Minesweeper is a popular game where the user has to find the mines using numeric hints that indicate how many mines are directly adjacent (horizontally, vertically, diagonally) to a square.

Instructions
Your task is to add the mine counts to empty squares in a completed Minesweeper board. The board itself is a rectangle composed of squares that are either empty (' ') or a mine ('*').

For each empty square, count the number of mines adjacent to it (horizontally, vertically, diagonally). If the empty square has no adjacent mines, leave it empty. Otherwise replace it with the adjacent mines count.

For example, you may receive a 5 x 4 board like this (empty spaces are represented here with the '·' character for display on screen):

·*·*·
··*··
··*··
·····
Which your code should transform into this:

1*3*1
13*31
·2*2·
·111·
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/minesweeper/canonical-data.json
