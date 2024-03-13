def translate(text):
    vowels = ['a', 'e', 'u', 'i', 'o']
    
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']

    word = text
    iter = 0

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

'''
Instructions
Implement a program that translates from English to Pig Latin.

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
There are a few more rules for edge cases, and there are regional variants too. Check the tests for all the details.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pig-latin/canonical-data.json
