def response(hey_bob):
    answer = None
    text_len = len(hey_bob)

    if '?' == hey_bob[-1:] and hey_bob.isupper() and not hey_bob == "":
        answer = "Calm down, I know what I'm doing!"
    elif hey_bob.isupper() and not hey_bob == "":
        answer = 'Whoa, chill out!'
    elif hey_bob.isspace() or not hey_bob:
        answer = "Fine. Be that way!"

    elif '?' == hey_bob[-1:] or '?' == hey_bob.replace(" ", "")[-1:]:
        answer = 'Sure.'

    else:
        answer = "Whatever."
    return answer