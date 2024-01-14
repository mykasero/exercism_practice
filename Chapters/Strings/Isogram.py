def is_isogram(string):
    is_true = True
    string = string.lower()
    hyphen = "-"
    space = " "
    string = string.replace(hyphen, "")
    string = string.replace(space, "")
    letters_in_string = []

    for i in range(len(string)):
        letters_in_string.append(string[i])
    letters_in_string.sort()

    for j in range(len(letters_in_string) - 1):
        if letters_in_string[j] == letters_in_string[j + 1]:
            is_true = False

    return is_true