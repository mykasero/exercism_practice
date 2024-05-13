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
        # turn into list
        for item in rows:
            results.append(item.split(";"))

        #count the stats MP,W,D,L
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


        #count points
        for team, stats in teams.items():
            for i in range(1,3):
                if i == 1:
                    points += 3*stats[i]
                elif i == 2:
                    points += stats[i]
            teams[team][4] = points
            points = 0

        #remove teams that haven't played
        ctr = 0
        teams_k = [item for item in teams.keys()]
        teams_v = [item for item in teams.values()]
        while True:
            if set(teams_v[ctr]) == {0}:
                del teams[teams_k[ctr]]

            ctr += 1
            if ctr == 4:
                break

        #sort the teams desc by points
        teams1 = dict(sorted(teams.items(), key=lambda item: item[1][4], reverse=True))

        #prepare final result
        for team, stats in teams1.items():
            for i in range(len(stats)):
                if i == len(stats)-1:
                    if stats[i] > 9:
                        txt_stats += " " + str(stats[i])
                    else:
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


    return final

'''

Instructions
Tally the results of a small football competition.

Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
What do those abbreviations mean?

MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points
A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome is ordered by points, descending. In case of a tie, teams are ordered alphabetically.

Input
Your tallying program will receive input that looks like:

Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win
The result of the match refers to the first team listed. So this line:

Allegoric Alaskans;Blithering Badgers;win
means that the Allegoric Alaskans beat the Blithering Badgers.

This line:

Courageous Californians;Blithering Badgers;loss
means that the Blithering Badgers beat the Courageous Californians.

And this line:

Devastating Donkeys;Courageous Californians;draw
means that the Devastating Donkeys and Courageous Californians tied.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/tournament/canonical-data.json
