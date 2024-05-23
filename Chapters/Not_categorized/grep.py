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
    text1 = ""
    text2 = ""
    text3 = ""

    final = ""

    if len(files) == 1:
        text1 = FILE_TEXT[files[0]].split("\n")

        if flags == "":
            for item in text1:
                if item.find(pattern) > 0:
                    index1 = text1.index(item)
                    final += text1[index1] + "\n"

        elif flags == "-n":
            for i in range(len(text1)):
                if text1[i].find(pattern) > 0:
                    index1 = text1.index(text1[i])
                    line_num = i+1
                    final += str(line_num) + ":" + text1[index1] + "\n"

        elif flags == "-l":
            keys = list(FILE_TEXT.keys())
            index = keys.index(files[0])
            final = keys[index] + "\n"

        elif flags == "-x":
            for item in text1:
                # test1 = item.find(pattern)
                # x = re.search(pattern, item)
                if re.search(pattern, item) and len(pattern) == len(item):
                    index1 = text1.index(item)
                    final += text1[index1] + "\n"

        elif flags == "-i":
            pattern = pattern.lower()
            for item in text1:
                if re.search(pattern.lower(), item.lower()):
                    index1 = text1.index(item)
                    final += text1[index1] + "\n"

        elif flags == "-v":
            for item in text1:
                if not re.search(pattern,item):
                    index1 = text1.index(item)
                    if index1 == len(text1)-1:
                        final += text1[index1]
                    else:
                        final += text1[index1] + "\n"


    elif len(files) == 2:
        text1 = FILE_TEXT[files[0]]
        text2 = FILE_TEXT[files[1]]
    else:
        text1 = FILE_TEXT[files[0]]
        text2 = FILE_TEXT[files[1]]
        text3 = FILE_TEXT[files[2]]

    #working on 1 file



    STOP = "STOP"
    return final