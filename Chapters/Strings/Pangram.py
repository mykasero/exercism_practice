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
    
