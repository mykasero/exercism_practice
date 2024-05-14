def recite(start_verse, end_verse):
    final = []
    verses = []
    animals = [None,"fly","spider","bird","cat","dog","goat","cow","horse"]
    special_lines = [None,
                     "It wriggled and jiggled and tickled inside her.",
                     "How absurd to swallow a bird!",
                     "Imagine that, to swallow a cat!",
                     "What a hog, to swallow a dog!",
                     "Just opened her throat and swallowed a goat!",
                     "I don't know how she swallowed a cow!"]

    middle_part_one = "She swallowed the "
    middle_part_two = " to catch the "


    first_line = "I know an old lady who swallowed a "
    last_line_fly = "I don't know why she swallowed the fly. Perhaps she'll die."
    last_line_horse = "She's dead, of course!"

    if start_verse == end_verse and start_verse == 1:
        final.append(first_line + animals[start_verse] + ".")
        final.append(last_line_fly)

    elif start_verse == end_verse and start_verse == 8:
        final.append(first_line + animals[start_verse] + ".")
        final.append(last_line_horse)

    elif start_verse == end_verse:
        final.append(first_line + animals[start_verse] + ".")
        final.append(special_lines[start_verse-1])

        for i in range(end_verse,1,-1):
            if i == 3:
                final.append(middle_part_one + animals[i] + middle_part_two + animals[i-1] + " " + special_lines[i-2].replace("It","that") )
            else:
                final.append(middle_part_one + animals[i] + middle_part_two + animals[i-1] + ".")

        final.append(last_line_fly)

    else:
        for i in range(start_verse,end_verse+1):
            for j in range(i,0,-1):
                if i == 1:
                    verses.append(first_line + animals[start_verse] + ".")
                    verses.append(last_line_fly)
                elif i == 8:
                    verses.append(first_line + animals[end_verse] + ".")
                    verses.append(last_line_horse)
                    break
                else:
                    if i == 3 and j == 3:
                        verses.append(first_line + animals[i] + ".")
                        verses.append(special_lines[i-1])
                        verses.append(middle_part_one + animals[i] + middle_part_two + animals[i - 1] + " " + special_lines[i - 2].replace("It", "that"))
                    elif i == j:
                        verses.append(first_line + animals[i] + ".")
                        verses.append(special_lines[i-1])
                        verses.append(middle_part_one + animals[j] + middle_part_two + animals[j-1] + ".")
                    elif j == 1:
                        verses.append(last_line_fly)
                    else:
                        if j == 3 :
                            verses.append(middle_part_one + animals[j] + middle_part_two + animals[j - 1] + " " + special_lines[j - 2].replace("It", "that"))
                        else:

                            verses.append(middle_part_one + animals[j] + middle_part_two + animals[j-1] + ".")

            final += verses
            verses = []

            if i < end_verse:
                final.append("")

    return final
