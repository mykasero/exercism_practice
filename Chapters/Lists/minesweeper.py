# STATUS :  5 Passed / 10 Failed

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
    elif all(same):
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
                #if minefield[i][j] != "*":
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

                numbers += str(number)
                number = 0

                # else:
                #     pass
            if i == len(minefield)-1:
                final_str += numbers
            else:
                final_str += numbers + " "
            #final_field.append(numbers)
            numbers = ""


    final_str = final_str.replace("0","*")
    final_field = final_str.split()

    return final_field