def recite(start, take=1):
    numbers_str = ["One", "Two", "Three", "Four",
                   "Five", "Six", "Seven", "Eight",
                   "Nine", "Ten"]

    lines = [" green bottles hanging on the wall,",
             "And if one green bottle should accidentally fall,",
             "There'll be ", " green bottles hanging on the wall."]

    final_list = []

    end = take
    step1 = 1
    if take == 1:
        if start == 1:
            for iter1 in range(len(lines)):
                if iter1 < 2:
                    final_list.append(numbers_str[start - 1] + lines[0].replace("bottles", "bottle"))
                elif iter1 >= 2 and iter1 < 3:
                    final_list.append(lines[1])
                else:
                    final_list.append(lines[2] + "no" + lines[3])
            return final_list
        elif start == 2:
            for iter1 in range(len(lines)):
                if iter1 < 2:
                    final_list.append(numbers_str[start - 1].replace("bottles", "bottle") + lines[0])
                elif iter1 >= 2 and iter1 < 3:
                    final_list.append(lines[1])
                else:
                    final_list.append(lines[2] + numbers_str[0].lower() + lines[3].replace("bottles", "bottle"))
            return final_list
        else:
            for iter1 in range(len(lines)):
                if iter1 < 2:
                    final_list.append(numbers_str[start - 1] + lines[0])
                elif iter1 >= 2 and iter1 < 3:
                    final_list.append(lines[1])
                else:
                    final_list.append(lines[2] + numbers_str[start - 2].lower() + lines[3])
            return final_list
    else:
        for iter1 in range(start, start - take, -1):
            for iter2 in range(len(lines)):
                if iter2 < 2:
                    if iter1 < 2:
                        final_list.append(numbers_str[iter1 - step1] + lines[0].replace("bottles", "bottle"))
                    else:
                        final_list.append(numbers_str[iter1 - step1] + lines[0])
                elif iter2 >= 2 and iter2 < 3:
                    final_list.append(lines[1])

                    step1 += 1
                else:
                    if iter1 == 2:
                        final_list.append(
                            lines[2] + numbers_str[iter1 - step1].lower() + lines[3].replace("bottles", "bottle"))
                    elif iter1 == 1:
                        final_list.append(lines[2] + "no" + lines[3])
                    else:
                        final_list.append(lines[2] + numbers_str[iter1 - step1].lower() + lines[3])

                    if iter1 != start - take + 1:
                        final_list.append("")
                    step1 = 1
        return final_list