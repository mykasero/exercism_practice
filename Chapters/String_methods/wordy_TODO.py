def answer(question):
    answer = 0
    # "?" is annoying, remove it
    
    question = question.replace("?","")
    numbers = []
    err_counter = 0
    #chop the question into words
    
    words = question.split()

    # for an operation keyword, do the math for the item index before and after the keyword
    # for only for single operation keyword
    if len(words) < 4:
        answer = int(words[len(words)-1])
    elif words[0] != "What":
        raise ValueError("syntax error")
    else:
        for word in range(len(words)-1):
            if words[word] == "plus":
                answer = int(words[word-1]) + int(words[word+1])
            elif words[word] == "minus":
                answer = int(words[word-1]) - int(words[word+1])
            elif words[word] == "multiplied":
                answer = int(words[word-1]) * int(words[word+2])
            elif words[word] == "divided":
                answer = int(words[word-1]) / int(words[word+2])
            elif words[word] not in ["plus","minus","multiplied","divided"]:
                err_counter +=1
        if len(words)-1 != err_counter:
            raise ValueError("unknown operation")


    return answer
