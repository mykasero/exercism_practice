import re

FILE_TEXT = {
    "iliad.txt": """Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.\n""",
    "midsummer-night.txt": """I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.\n""",
    "paradise-lost.txt": """Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed\n""",
}

'''
Flags
The grep command supports the following flags:

-n Prepend the line number and a colon (':') to each line in the output, placing the number after the filename (if present).
-l Output only the names of the files that contain at least one matching line.
-i Match using a case-insensitive comparison.
-v Invert the program -- collect all lines that fail to match.
-x Search only for lines where the search string matches the entire line.
'''


def grep(pattern, flags, files):
    final = ""
    flag_list = flags.split()

    # working on 1 file
    # STATUS - all passed

    if len(flag_list) == 0:
        flag_list.append("")

    if len(files) == 1:
        text1 = FILE_TEXT[files[0]].split("\n")
        for flag in flag_list:
            if flag == "":
                for item in text1:
                    if item.find(pattern) > 0:
                        index1 = text1.index(item)
                        final += text1[index1] + "\n"

            if flag == "-n":
                for i in range(len(text1)):
                    line_num = i + 1

                    if re.search(pattern.lower(), text1[i].lower()):
                        index1 = text1.index(text1[i])
                        if len(flag_list) > 1:
                            final += str(line_num) + ":"
                        else:
                            final += str(line_num) + ":" + text1[index1] + "\n"



            if flag == "-x":
                for item in text1:
                    # test1 = item.find(pattern)
                    # x = re.search(pattern, item)
                    if re.search(pattern, item) and len(pattern) == len(item):
                        index1 = text1.index(item)
                        final += text1[index1] + "\n"

            if flag == "-i":
                pattern = pattern.lower()
                for item in text1:
                    if re.search(pattern.lower(), item.lower()):
                        index1 = text1.index(item)
                        final += text1[index1] + "\n"

            if flag == "-v":
                final = ""
                for item in text1:
                    if not re.search(pattern,item):
                        index1 = text1.index(item)
                        if index1 == len(text1)-1:
                            final += text1[index1]
                        else:
                            final += text1[index1] + "\n"

            if flag == "-l":
                keys = list(FILE_TEXT.keys())
                index = keys.index(files[0])
                for item in text1:
                    if re.search(pattern.lower(),item.lower()):
                        final = keys[index] + "\n"

    #working on multiple files

    else:
        final_group = []

        for title in files:
            text1 = FILE_TEXT[title].split("\n")
            for flag in flag_list:
                if flag == "":
                    for item in text1:
                        if item.find(pattern) > 0:
                            index1 = text1.index(item)
                            final += title+":"+text1[index1] + "\n"

                if flag == "-n":
                    for i in range(len(text1)):
                        line_num = i + 1
                        if "-i" in flag_list:
                            if re.search(pattern.lower(), text1[i].lower()):
                                index1 = text1.index(text1[i])
                                if len(flag_list) > 1:
                                    final += title+":"+str(line_num) + ":"
                                else:
                                    final += title+":"+str(line_num) + ":" + text1[index1] + "\n"
                        else:
                            if re.search(pattern, text1[i]):
                                index1 = text1.index(text1[i])
                                if len(flag_list) > 1:
                                    final += title+":"+str(line_num) + ":"
                                else:
                                    final += title+":"+str(line_num) + ":" + text1[index1] + "\n"

                if flag == "-l":
                    for item in text1:
                        if re.search(pattern.lower(), item.lower()):
                            final = title + "\n"

                if flag == "-x":
                    if len(flag_list) == 1:
                        for item in text1:

                            if re.search(pattern, item) and len(pattern) == len(item):
                                index1 = text1.index(item)
                                final += title + ":" + text1[index1] + "\n"

                if flag == "-i":
                    pattern = pattern.lower()
                    for item in text1:
                        if re.search(pattern.lower(), item.lower()):
                            index1 = text1.index(item)
                            if "-n" in flag_list:
                                final += text1[index1] + "\n"
                            else:
                                final += title + ":" + text1[index1] + "\n"

                if flag == "-v":
                    final = ""
                    for item in text1:
                        if not re.search(pattern, item) and item != "":
                            final += title + ":" + item + "\n"
            if final != "":
                final_group.append(final)
                final = ""


        if len(final_group) > 1:
            for item in final_group:
                final += item
        else:
            if final_group != []:
                final = final_group[0]
            else:
                final = ""


    return final


'''
Instructions
Search files for lines matching a search string and return all matching lines.

The Unix grep command searches files for lines that match a regular expression. 
Your task is to implement a simplified grep command, which supports searching for fixed strings.

The grep command takes three arguments:

The string to search for.
Zero or more flags for customizing the command's behavior.
One or more files to search in.
It then reads the contents of the specified files (in the order specified), finds the lines that contain the search string, 
and finally returns those lines in the order in which they were found. When searching in multiple files, each matching line is prepended by the file name and a colon (':').

Flags
The grep command supports the following flags:

-n Prepend the line number and a colon (':') to each line in the output, placing the number after the filename (if present).
-l Output only the names of the files that contain at least one matching line.
-i Match using a case-insensitive comparison.
-v Invert the program -- collect all lines that fail to match.
-x Search only for lines where the search string matches the entire line.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/grep/canonical-data.json
