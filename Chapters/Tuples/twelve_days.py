def recite(start_verse, end_verse):
    base_text = "On the first day of Christmas my true love gave to me:"
    all_gifts = ['and a Partridge in a Pear Tree.', 'two Turtle Doves,', 'three French Hens,',
                 'four Calling Birds,', 'five Gold Rings,', 'six Geese-a-Laying,', 'seven Swans-a-Swimming,',
                 'eight Maids-a-Milking,', 'nine Ladies Dancing,', 'ten Lords-a-Leaping,', 'eleven Pipers Piping,',
                 'twelve Drummers Drumming']

    # gift_list = all_gifts.split(",")
    gift_list2 = []

    for iter in range(len(all_gifts) - 1, 0, -1):
        gift_list2.append(all_gifts[iter])

    # print(gift_list,'\n',gift_list2)
    strings = [gift_list2[0].strip()]

    gift_list2.remove(gift_list2[0])

    final = base_text
    for item in gift_list2:
        # print(item)
        item += ","
        strings.append(item.strip())

    if end_verse == 1:
        final.join()
    else:
        for iter in range(end_verse - 1, 0, -1):
            final += '\n' + strings[iter]

    return final
