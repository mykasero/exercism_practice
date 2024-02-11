def recite(start_verse, end_verse):
    base_text_1 = "On the "
    base_text_2 = " day of Christmas my true love gave to me: "

    all_gifts = ('and a Partridge in a Pear Tree.', 'two Turtle Doves, ', 'three French Hens, ',
                 'four Calling Birds, ', 'five Gold Rings, ', 'six Geese-a-Laying, ', 'seven Swans-a-Swimming, ',
                 'eight Maids-a-Milking, ', 'nine Ladies Dancing, ', 'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ',
                 'twelve Drummers Drumming, ')

    days = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
            "twelfth")

    final = []

    if end_verse == 1 and start_verse == 1:
        final.append(base_text_1 + days[0] + base_text_2 + all_gifts[0].replace("and ", ""))
    else:
        for iter1 in range(start_verse, end_verse + 1):
            if iter1 == 1:
                final.append(base_text_1 + days[0] + base_text_2 + all_gifts[0].replace("and ", ""))
            else:
                final.append(base_text_1 + days[iter1 - 1] + base_text_2 + "".join(all_gifts[iter1 - 1::-1]))

    return final


