#STATUS 46 / 48 PASSED

MATH_OPS = ["+","-","*","/"]
STACK_OPS = ["dup","drop","swap","over"]

class StackUnderflowError(Exception):
    def __init__(self,message):
        self.message = message


def evaluate(input_data):
    # if fill this later:
    #     raise StackUnderflowError("Insufficient number of items in stack") #works
    test = type(input_data)
    if len(input_data) > 1:
        #version with 46/48 passed
        for i in range(len(input_data)):
            input_data[i] = input_data[i].lower()
        new_instr = input_data[len(input_data)-2].split()
        new_instr = new_instr[1:len(new_instr)-1]
        lookup = dict()
        lookup[new_instr[0]] = new_instr[1:]
        command = input_data[len(input_data)-1].split()


        stack = []
        for item in command:
            if item not in lookup.keys():
                stack.append(int(item))
            else:
                if item.lower() == "countup":
                    for numb in lookup[item]:
                        stack.append(int(numb))
                    stack.sort()
                else:
                    for value in lookup[item]:
                        if value.lower() == "dup":
                            stack.append(stack[len(stack)-1])
                        elif value.lower() == "+":
                            x = stack.pop()
                            stack = [stack[0] + x]
                        elif value.lower() == "-":
                            x = stack.pop()
                            stack = [stack[0] - x]
                        elif value.lower() == "*":
                            x = stack.pop()
                            stack = [stack[0] * x]
                        elif value.lower() == "-":
                            x = stack.pop()
                            stack = [stack[0] / x]

    else:
        is_op = set()
        stack = []
        input_data[0] = input_data[0].lower()
        for item in input_data[0].split():
            if item not in MATH_OPS and item not in STACK_OPS :
                is_op.add(False)
            else:
                is_op.add(True)

            if item not in MATH_OPS and item not in STACK_OPS:
                try:
                    int(item)
                except:
                    if item == ";" or item == ":":
                        raise ValueError("illegal operation")
                    else:
                        raise ValueError("undefined operation")



        if len(is_op) == 1 and list(is_op)[0] == False:
                return [int(item) for item in input_data[0].split()]

        else:
            for item in input_data[0].split():
                if item not in MATH_OPS and item not in STACK_OPS:
                    stack.append(int(item))

                elif item in MATH_OPS:

                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")

                    elif 0 in stack:
                        raise ZeroDivisionError("divide by zero")

                    elif item == "+":
                        for item1 in stack:
                            if len(stack) > 1:
                                x = int(stack.pop())
                                stack[0] = int(stack[0]) + x

                    elif item == "-":
                        for item1 in stack:
                            if len(stack) > 1:
                                x = int(stack.pop())
                                stack[0] = int(stack[0]) - x

                    elif item == "*":
                        for item1 in stack:
                            if len(stack) > 1:
                                x = int(stack.pop())
                                stack[0] = int(stack[0]) * x

                    elif item == "/":
                        for item1 in stack:
                            if len(stack) > 1:
                                x = int(stack.pop())
                                stack[0] = int(int(stack[0]) / x)

                elif item in STACK_OPS:
                    if len(stack) < 1:
                        raise StackUnderflowError("Insufficient number of items in stack")

                    elif item == "dup":
                        for item1 in stack:
                            x = stack.pop()
                            stack.append(int(x))
                            stack.append(int(x))
                            break

                    elif item == "drop":
                        for item in stack:
                            x = stack.pop()
                            break

                    elif item == "swap":
                        if len(stack) < 2:
                            raise StackUnderflowError("Insufficient number of items in stack")
                        else:
                            for item in stack:
                                x = stack.pop()
                                stack.insert(len(stack)-1,x)
                                break

                    elif item == "over":
                        if len(stack) < 2:
                            raise StackUnderflowError("Insufficient number of items in stack")
                        else:
                            stack.append(stack[len(stack)-2])


    STOP = "STOP"

    return stack