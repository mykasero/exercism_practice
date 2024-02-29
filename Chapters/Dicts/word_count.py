def count_words(sentence):
    punctuation = [":", "!", "?", ",", ".", "\t", "\n", " ",
                   "!", "@", "#", "$", "%", "^", "&", "*", "_"]

    if sentence[0] == "'" and sentence[-1:] == "'":
        sentence = sentence[1:-1]

    sentence = sentence.lower()
    for item in sentence:
        if item in punctuation:
            sentence = sentence.replace(item, " ")

    elements_list = sentence.split()

    new_word = ""
    for word in elements_list:
        if word[0] == "'":
            new_word = word[1:-1]
            elements_list[elements_list.index(word)] = new_word
        elif word[0] == '"':
            new_word = word[1:-1]
            elements_list[elements_list.index(word)] = new_word

    words = dict()

    for element in range(len(elements_list)):
        if elements_list[element] not in words.keys():
            words[elements_list[element]] = words.get(elements_list[element], 1)
        else:
            words[elements_list[element]] += 1

    return words