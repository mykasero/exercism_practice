def is_pangram(sentence):
    is_true = False
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
    special_chars = ["@","$","#","&",".",'"',"'","*"," ","(",")","[","]","{","}","=",",","-","+",";","/"]
    total_letters = 26
    counter = 0
    sentence = sentence.lower()
    
    for character in special_chars:
        if character in sentence:
            sentence = sentence.replace(character,"")
            
    for letter in alphabet:
        if letter in sentence:
            counter+=1

    if counter == total_letters:
        is_true = True
    
    return is_true

'''
Instructions
Your task is to figure out if a sentence is a pangram.

A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pangram/canonical-data.json
