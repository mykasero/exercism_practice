def find(search_list, value):
    list1 = search_list
    number_to_find = value
    iter1 = 0
    if len(list1) == 0:
        raise ValueError("value not in array")
    else:
        for item in list1:
            if item == number_to_find:
                return iter1
                # break
            elif iter1 == 0 and number_to_find < item or iter1 == len(list1) - 1 and number_to_find > item:
                raise ValueError("value not in array")
            else:
                iter1 += 1

    return 0


# 10/11 cases done
