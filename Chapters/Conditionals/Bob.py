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

'''
Introduction
Bob is a lackadaisical teenager. He likes to think that he's very cool. And he definitely doesn't get excited about things. That wouldn't be cool.

When people talk to him, his responses are pretty limited.

Instructions
Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/bob/canonical-data.json
