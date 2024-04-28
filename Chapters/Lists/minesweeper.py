# STATUS :  10 Passed / 5 Failed

def annotate(minefield):
    # Function body starts here
    final_str = ""
    final_field = []
    mine_coords = []
    numbers = ""
    same = []
    number = 0
    for item in minefield:
        for i in range(1,len(item)):
            if item[0] == item[i]:
                same.append(True)
            else:
                same.append(False)

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
                            if j < len(minefield[i])-1:
                                if minefield[i][j + 1] == "*":  # check right
                                    number += 1
                                if minefield[i+1][j+1] == "*": #check bot right
                                    number += 1
                            if j > 0:
                                if minefield[i+1][j-1] == "*": #check bot left
                                    number += 1

                        if i > 0:
                            if minefield[i - 1][j] == "*":  # check above
                                number += 1

                            if j > 0:
                                if minefield[i-1][j-1] == "*": #check top left
                                    number += 1

                            if j < len(minefield[i])-1:
                                if minefield[i-1][j+1] == "*": #check top right
                                    number += 1

                        if j > 0:
                            if minefield [i][j-1] == "*": #check left
                                number += 1



                    if number > 0:
                        if number == 99:
                            numbers += " "
                            number = 0
                        else:
                            numbers += str(number)
                            number = 0
                    else:
                        number = 0
                        numbers += str(number)
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


    final_str = final_str.replace("0","*")
    if len(minefield) == 1:
        final_field.append(final_str)
    elif len(minefield) > 1 and len(minefield[0]) == 1:
        for item in final_str:
            final_field.append(item)
    else:
        final_field = final_str.split()

    return final_field