def answer(question):
    answer = 0
    numbers = []
    operations = 0
    minus_numbers = 0
    # "?" is annoying, remove it
    
    question = question.replace("?","")
    
    
    err_counter = 0
    #chop the question into words
    
    words = question.split()
    # checking the amount of negative numbers

    for word in range(len(words)-1):
        if word < 0:
            minus_numbers+=1

    
    # for an operation keyword, do the math for the item index before and after the keyword
    
    # for only for single operation keyword (works but doesnt raise a good syntax error for missing operation)
    
    if len(words) < 4:
        answer = int(words[len(words)-1])
    elif words[0] != "What":
        raise ValueError("syntax error")
    else:
        for word in range(len(words)-1):
            if words[word] == "plus":
                if operations > 0 :
                    answer += int(words[word+1])
                else:
                    answer += int(words[word-1]) + int(words[word+1])
                    operations+=1
            elif words[word] == "minus":
                if int(words[word+1]) < 0 and operations > 0:
                    answer += abs(int(words[word+1]))
                elif int(words[word+1]) < 0 and operations == 0:
                    answer = int(words[word-1]) + abs(int(words[word+1]))
                    operations+=1
                elif int(words[word+1]) >= 0 and operations == 0:
                    answer = int(words[word-1]) - int(words[word+1])
                    operations+=1
                else:
                    answer -= int(words[word+1])
            elif words[word] == "multiplied":
                if operations > 0:
                    answer *= int(words[word+2])
                else:
                    answer = int(words[word-1]) * int(words[word+2])
                    operations+=1
            elif words[word] == "divided":
                if operations > 0 and minus_numbers%2 == 0:
                    answer /= abs(int(words[word-1])) / abs(int(words[word+2]))
                elif operations == 0 and minus_numbers%2 == 0:
                    answer = abs(int(words[word-1])) / abs(int(words[word+2]))
                    operations+=1
                elif operations == 0 and minus_numbers%2 != 0 :
                    answer = int(words[word-1]) / int(words[word+2])
                    operations+=1
                else:
                    answer /= int(words[word+2])
            elif words[word] not in ["plus","minus","multiplied","divided"]:
                err_counter +=1



    return answer
