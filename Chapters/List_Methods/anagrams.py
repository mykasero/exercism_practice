def find_anagrams(word, candidates):
    word_letters = []
    anagrams = []

    candidate_letters = []

    for iter in range(len(word)):
        word_letters.append(word[iter].lower())

    word_letters.sort()

    for candidate0 in candidates:
        if word.lower() == candidate0.lower():
            candidates.remove(candidate0)

    for candidate in candidates:

        for letter in range(len(candidate)):
            candidate_letters.append(candidate[letter].lower())

        candidate_letters.sort()

        if word_letters == candidate_letters:
            anagrams.append(candidate)
        else:
            pass

        candidate_letters = []

    return anagrams
