class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    user_defined_dict = {}

    for i in range(len(input_data) - 1):
        data_list = input_data[i].lower().split()

        if data_list[1].isdigit():
            raise ValueError("illegal operation")

        user_defined_dict[data_list[1]] = " ".join(data_list[2:-1])

        next_data_list = input_data[i + 1].lower().split()

        if next_data_list[0] == ':':
            for key, value in user_defined_dict.items():
                if key in next_data_list[2:]:
                    temp = " ".join(next_data_list[2:]).replace(key, value)
                    input_data[i + 1] = " ".join(next_data_list[:2]) + ' ' + temp

    return evaluate_stack(input_data[-1].lower(), user_defined_dict)


def evaluate_stack(stack_string, user_defined_dict):
    int_list = []

    for key, value in user_defined_dict.items():
        if key in stack_string:
            stack_string = stack_string.replace(key, value)

    CHEAT_DICT = {'dup': 1, 'over': 2}
    stack_list = stack_string.split()

    while stack_list:
        word = stack_list.pop(0)

        if word.isdigit() or (len(word) > 1 and word[0] == '-' and word[1:].isdigit()):
            int_list.append(int(word))

        elif word in '+-*':
            check_for_underflow(int_list, 2)
            int_list = [eval(f"{int_list[-2]} {word} {int_list[-1]}")]

        elif word == '/':
            check_for_underflow(int_list, 2)
            if int_list[-1] == 0:
                raise ZeroDivisionError("divide by zero")
            int_list = [int_list[-2] // int_list[-1]]

        elif word in CHEAT_DICT:
            check_for_underflow(int_list, CHEAT_DICT[word])
            int_list.append(int_list[-1 * CHEAT_DICT[word]])

        elif word == 'drop':
            check_for_underflow(int_list, 1)
            int_list.pop()

        elif word == 'swap':
            check_for_underflow(int_list, 2)
            int_list = int_list[:-2] + [int_list[-1]] + [int_list[-2]]

        elif word == ':':
            raise ValueError("illegal operation")

        else:
            raise ValueError("undefined operation")

    return int_list


def check_for_underflow(list_, min_stack_len):
    if len(list_) < min_stack_len:
        raise StackUnderflowError("Insufficient number of items in stack")