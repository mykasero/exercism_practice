def translate(text):
    # vowel - samogloska
    vowels = ['a', 'e', 'u', 'i', 'o']

    # consonant - spolgloska
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']

    word = text
    iter = 0
    for i in range(len(text) - 1):
        if text[i] == 'y':
            break
        iter += 1

    if " " in text:
        text = text.split()
        word = text[0][2:] + text[0][:2] + 'ay' + " " + text[1][1:] + text[1][0] + 'ay' + " " + text[2][1:] + text[2][
            0] + 'ay'

    elif text[0] in vowels or text[:2] in 'xr' or text[:2] in 'yr' or text[:2] == 'yt':
        word += 'ay'
    elif text[0] == 'q' and text[1] == 'u':
        word = text[2:] + 'qu' + 'ay'
    elif text[0] in consonants and text[1] in vowels:
        word = text[1:] + text[0] + 'ay'
    elif text[0] in consonants and text[1] in 'q' and text[2] in 'u':
        word = text[3:] + text[0] + 'qu' + 'ay'
    elif text[:2] in consonants and text[2] in 'y':
        word = text[2:] + text[:2] + 'ay'
    elif len(text) == 2 and text[1] == 'y':
        word = 'y' + text[0] + 'ay'
    elif text[0] in consonants and text[1] in consonants and text[2] == 'y':
        word = text[2:] + text[:2] + 'ay'
    elif text[0] in consonants and text[1] in consonants and text[2] in consonants:
        word = text[3:] + text[:3] + 'ay'
    elif text[0] in consonants and text[1] in consonants:
        word = text[2:] + text[:2] + 'ay'

    return word