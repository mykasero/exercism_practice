def recite(start_verse, end_verse):
    base_text_1 = "On the "
    base_text_2 = " day of Christmas my true love gave to me: "
    
    all_gifts = ('and a Partridge in a Pear Tree.', 'two Turtle Doves, ', 'three French Hens, ',
             'four Calling Birds, ', 'five Gold Rings, ', 'six Geese-a-Laying, ', 'seven Swans-a-Swimming, ',
             'eight Maids-a-Milking, ', 'nine Ladies Dancing, ', 'ten Lords-a-Leaping, ', 'eleven Pipers Piping, ',
             'twelve Drummers Drumming ')
    
    days = ("first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth")

    final = []
    loop_iter = end_verse-1
    
    if end_verse == 1 and start_verse==1:
        day_string = base_text_1 + days[end_verse - 1] + base_text_2
        final.append(day_string + all_gifts[0].replace("and ", ""))
    else:
        for day_num in range(start_verse, end_verse+1):
            day_string = base_text_1 + days[day_num - 1] + base_text_2
            gifts = all_gifts[day_num - 1::-1]  # Get the corresponding gifts for this day
            final.append(day_string + ''.join(gifts))
            
    
    return final
