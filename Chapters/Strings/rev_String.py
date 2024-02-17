def reverse(text):
    new_string = ""

    for i in range(len(text)-1,-1,-1):
        new_string += text[i]

    return new_string
