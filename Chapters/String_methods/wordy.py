import re
def answer(question):
    operators = {
        'minus': lambda a, b: a - b,
        'plus': lambda a, b: a + b,
        'multiplied': lambda a, b: a * b,
        'divided': lambda a, b: a / b,
        'power': lambda a, b: a**b
    }

    if not question.startswith("What is"):
        raise ValueError("unknown operation")

    if question.endswith("cubed?"):
        raise ValueError("unknown operation")
    array = question[8:-1].replace('by ', '').split(' ')
    acc = None
    try:
        acc = float(array[0])
    except ValueError:
            raise ValueError("syntax error")
    
    for op in range(1, len(array), 2):
        try:
            acc = operators[array[op]](acc, float(array[op + 1]))
        except KeyError:
            raise ValueError("syntax error")
        except ValueError:
            raise ValueError("syntax error")
        except IndexError:
            raise ValueError("syntax error")
    return acc
