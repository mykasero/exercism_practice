# STATUS :  13 Passed / 2 Failed

def annotate(minefield):
    # Function body starts here
    final_str = ""
    final_field = []
    mine_coords = []
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
        for row in range(len(minefield)):
            for column in range(len(minefield[row])):
                if minefield[row][column] == "*":
                    mine_coords.append((row,column))

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
                                if minefield[i][j + 1] == "*":  # check right
                                    number += 1
                                else:
                                    not_s[4] = True
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

                        if j > 0:
                            if minefield [i][j-1] == "*": #check left
                                number += 1
                            else:
                                not_s[3] = True



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

                        not_s = [None, None, None, None, None, None, None, None]

                # elif minefield[i][j] == "*":
                #     numbers += "0"
                else:
                    numbers += "0"


            if i == len(minefield)-1:
                final_str += numbers
            else:
                if len(minefield[0]) == 1:
                    final_str += numbers
                else:
                 final_str += numbers + " "

            #final_field.append(numbers)
            numbers = ""
    xhyz ="STOP"

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
