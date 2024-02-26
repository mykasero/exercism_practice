def recite(start_verse, end_verse):
    elements1 = ["PLACEHOLDER", " the house that Jack", " the malt", " the rat", " the cat",
                 " the dog", " the cow with the crumpled horn", " the maiden all forlorn",
                 " the man all tattered and torn", " the priest all shaven and shorn",
                 " the rooster that crowed in the morn", " to the farmer sowing his corn",
                 " the horse and the hound and the horn"]

    elements2 = ["PLACEHOLDER", " built.", " lay in", " ate", " killed", " worried", " tossed", " milked", " kissed",
                 " married", " woke", " kept", " belonged"]

    recite_str = ""
    final_recite = []

    if start_verse == end_verse:
        for recite1 in range(start_verse, 0, -1):
            if recite1 == start_verse and not recite1 == 1:
                if recite1 == 11:
                    recite_str += "This is" + elements1[recite1].replace(" to", "") + " that" + elements2[recite1]
                else:
                    recite_str += "This is" + elements1[recite1] + " that" + elements2[recite1]
            elif recite1 == start_verse and recite1 == 1:
                recite_str += "This is" + elements1[recite1] + elements2[recite1]
            else:
                if recite1 == 1:
                    recite_str += elements1[recite1] + elements2[recite1]
                else:
                    recite_str += elements1[recite1] + " that" + elements2[recite1]
        final_recite.append(recite_str)
    else:
        for lines in range(start_verse, end_verse + 1):
            if lines == 1:
                recite_str += "This is" + elements1[lines] + elements2[lines]

            else:
                for recite in range(lines, 0, -1):
                    if lines == recite:
                        if lines == 11:
                            recite_str += "This is" + elements1[recite].replace(" to", "") + " that" + elements2[recite]
                        else:
                            recite_str += "This is" + elements1[recite] + " that" + elements2[recite]

                    elif recite == 1:
                        recite_str += elements1[recite] + elements2[recite]
                    else:
                        recite_str += elements1[recite] + " that" + elements2[recite]

            final_recite.append(recite_str)
            recite_str = ""

    return final_recite
