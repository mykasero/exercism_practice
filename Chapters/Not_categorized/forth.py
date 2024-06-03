#STATUS 29 / 48 PASSED

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
        splitted = input_data.split()

    else:
        is_op = set()
        stack = []
        for item in input_data[0].split():
            if item not in MATH_OPS and item not in STACK_OPS:
                is_op.add(False)
            else:
                is_op.add(True)


        if len(is_op) == 1 and list(is_op)[0] == False:
            return [int(item) for item in input_data[0].split()]

        else:
            for item in input_data[0].split():
                if item not in MATH_OPS and item not in STACK_OPS:
                    stack.append(int(item))

                elif item in MATH_OPS:

                    if len(stack) < 2:
                        raise StackUnderflowError("Insufficient number of items in stack")

                    elif "0" in stack:
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
                        if len(stack) < 3:
                            raise StackUnderflowError("Insufficient number of items in stack")
                        else:
                            for item in stack:
                                x = stack.pop()
                                stack.insert(len(stack)-1,x)
                                break

                    elif item == "over":
                        if len(stack) < 3:
                            raise StackUnderflowError("Insufficient number of items in stack")
                        else:
                            stack.append(stack[len(stack)-2])


    STOP = "STOP"

    return stack