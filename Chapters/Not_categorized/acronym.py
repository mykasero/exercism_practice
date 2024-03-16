def abbreviate(words):
    final = ""
    words = words.replace("-"," ").replace(",","").replace("_","")
    w_split = words.split()
    for item in w_split:
        final += item[0].upper()
    return final
