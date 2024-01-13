def is_pangram(sentence):
    is_true = False
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    total_letters = 26
    counter = 0
    if '"' in sentence or "." in sentence or "'" in sentence or " " in sentence:
        sentence = sentence.replace('"', "")
        sentence = sentence.replace("'", "")
        sentence = sentence.replace(".", "")
        sentence = sentence.replace(" ", "")
        sentence = sentence.lower()
    for letter in alphabet:
        if letter in sentence:
            counter += 1

    if counter == total_letters:
        is_true = True

    return is_true
