#STATUS 8/12

# 31st is the place of the first |

def tally(rows):
    line_zero = "Team" + 27*" " + "| MP |  W |  D |  L |  P"
    results = []

    teams = {"Allegoric Alaskans" : [0, 0, 0 ,0 ,0],"Blithering Badgers" : [0, 0, 0 ,0 ,0],
             "Courageous Californians" : [0, 0, 0 ,0 ,0], "Devastating Donkeys"  : [0, 0, 0 ,0 ,0]}

    points = 0

    txt_stats = "|"
    final = []
    final.append(line_zero)


    if len(rows) == 0:
        return [line_zero]
    else:
        for item in rows:
            results.append(item.split(";"))


        for result in results:
            if result[2] == "win":
                #MP
                teams[result[0]][0] += 1
                teams[result[1]][0] += 1

                #W
                teams[result[0]][1] += 1

                #L
                teams[result[1]][3] += 1

            elif result[2] == "draw":
                #MP
                teams[result[0]][0] += 1
                teams[result[1]][0] += 1

                # Draw
                teams[result[0]][2] += 1
                teams[result[1]][2] += 1

            elif result[2] == "loss":
                # MP
                teams[result[0]][0] += 1
                teams[result[1]][0] += 1

                # W
                teams[result[1]][1] += 1

                # L
                teams[result[0]][3] += 1


        for team, stats in teams.items():
            for i in range(1,3):
                if i == 1:
                    points += 3*stats[i]
                elif i == 2:
                    points += stats[i]
            teams[team][4] = points
            points = 0

        #sort dict based by pts
        # teams1 = dict(sorted(teams.items(), key = lambda item: item[1][4], reverse = True))
        # needs more work /\

        for team, stats in teams.items():
            if set(stats) != {0}:
                for i in range(len(stats)):
                    if i == len(stats)-1:
                        txt_stats += "  " + str(stats[i])
                    else:
                        if stats[i] > 9:
                            txt_stats += " " + str(stats[i]) + " |"
                        else:
                            txt_stats += "  " + str(stats[i]) + " |"


                txt = team + (31 - len(team)) * ' ' + txt_stats
                final.append(txt)
            txt = ""
            txt_stats = "|"

    STOP = "STOP"

    return final