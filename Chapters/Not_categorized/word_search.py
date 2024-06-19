#STATUS 13/24
'''
notes - functions for every single posible direction of search will be too large for this to be optimal, gotta find another way
might check with itertools neighbouring letters in all directions starting from a point where word[0] is found then searching for word[1] will determine the direction
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        TEST = other
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.word = ""

    def search(self, word):
        self.word = word
        splitted = []
        part = []

        begin_point = None
        end_point = None

        for item in self.puzzle:
            for element in item:
                part.append(element)
            splitted.append(part)
            part = []

        # normal search (left to right, checking only every row) all tests passed
        # split this maybe into functions : normal search, backwards search (right to left, every row), top down and down top and diagonal

        left_right = self.left_right(splitted) #works





        if left_right[0] == True:
            return left_right[1], left_right[2]
        else:
            right_left = self.right_left(splitted) #works

            if right_left[0] == True:
                return right_left[1], right_left[2]
            else:
                top_bottom = self.top_bottom(splitted)  # works

                if top_bottom[0] == True:
                    return top_bottom[1], top_bottom[2]

                else:
                    return False


                # else:
                #     bottom_top = self.bottom_top(splitted)  # works
                #     if bottom_top[0] == True:
                #         return bottom_top[1], bottom_top[2]
                #     else:
                #         return False

        STOP = "TEST"

    def left_right(self,split_chars):
        splitted = split_chars
        begin_point = None
        end_point = None
        word_found = False
        stop_loop = False

        for row in range(len(splitted)+1):
            if begin_point is not None and end_point is not None:
                temp_word = splitted[begin_point.y][begin_point.x:end_point.x + 1]
                check_word = "".join(temp_word)

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                    if row == len(splitted):
                        stop_loop = True
                        break
                else:
                    word_found = True
                    #splitted.pop(row)
                    break

            elif begin_point is not None and end_point is None:
                begin_point = None
                end_point = None

            if stop_loop == False:
                for column in range(len(splitted[row])):

                    if splitted[row][column] == self.word[0]:
                        begin_point = Point(column, row)
                        test_b_p = (column,row)
                    elif splitted[row][column] == self.word[-1] and begin_point is not None:
                        if self.word[-1] == self.word[-2]:
                            end_point = Point(column+1, row)
                        else:
                            end_point = Point(column, row)
                        test_e_p = (column,row)
                        break

        return [word_found, begin_point, end_point]

    def right_left(self, split_chars):
        splitted = split_chars
        begin_point = None
        end_point = None
        word_found = False

        for row in range(len(splitted)-1,-2,-1):
            if begin_point is not None and end_point is not None:
                temp_word = splitted[begin_point.y][end_point.x :begin_point.x+1][::-1]
                check_word = "".join(temp_word)

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                    if row == -1:
                        break
                else:
                    word_found = True
                    # splitted.pop(row)
                    break

            elif begin_point is not None and end_point is None or begin_point is None and end_point is not None:
                begin_point = None
                end_point = None

            for column in range(len(splitted[row])-1,-1,-1):

                if splitted[row][column] == self.word[0]:
                    begin_point = Point(column, row)
                    test_b_p = (column, row)
                elif splitted[row][column] == self.word[-1] and begin_point is not None:
                    if self.word[-1] == self.word[-2]:
                        end_point = Point(column + 1, row)
                    else:
                        end_point = Point(column, row)
                    test_e_p = (column, row)
                    break

        return [word_found, begin_point, end_point]

    def top_bottom(self, split_chars):
        splitted = split_chars
        begin_point = None
        end_point = None
        word_found = False


        for column in range(len(splitted[0])+1):
            if begin_point is not None and end_point is not None:
                temp_word = ""
                for y_coord in range(begin_point.y,end_point.y+1):
                    temp_word += splitted[y_coord][begin_point.x]
                # temp_word = splitted[begin_point.y:end_point.y+1][begin_point.x]
                check_word = "".join(temp_word)

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                    if column == len(splitted[0]):
                        break
                else:
                    word_found = True
                    # splitted.pop(row)
                    break

            elif begin_point is not None and end_point is None or begin_point is None and end_point is not None:
                begin_point = None
                end_point = None
                if column == len(splitted[0]):
                    break

            for row in range(len(splitted)):

                if splitted[row][column] == self.word[0]:
                    begin_point = Point(column, row)
                    test_b_p = (column, row)
                elif splitted[row][column] == self.word[-1] and begin_point is not None:
                    if self.word[-1] == self.word[-2]:
                        end_point = Point(column + 1, row)
                    else:
                        end_point = Point(column, row)
                    test_e_p = (column, row)
                    break

        return [word_found, begin_point, end_point]

    def bottom_top(self, split_chars):
        splitted = split_chars
        begin_point = None
        end_point = None
        word_found = False


        for column in range(len(splitted[0])-1,-2,-1):
            if begin_point is not None and end_point is not None:
                temp_word = ""
                for y_coord in range(end_point.y,begin_point.y+1):
                    temp_word += splitted[y_coord][begin_point.x]
                # temp_word = splitted[begin_point.y:end_point.y+1][begin_point.x]
                check_word = "".join(temp_word[::-1])

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                    if column == -1:
                        break
                else:
                    word_found = True
                    # splitted.pop(row)
                    break

            elif begin_point is not None and end_point is None or begin_point is None and end_point is not None:
                begin_point = None
                end_point = None
                if column == -1:
                    break

            for row in range(len(splitted)-1,-1,-1):

                if splitted[row][column] == self.word[0]:
                    begin_point = Point(column, row)
                    test_b_p = (column, row)
                elif splitted[row][column] == self.word[-1] and begin_point is not None:
                    if self.word[-1] == self.word[-2]:
                        end_point = Point(column + 1, row)
                    else:
                        end_point = Point(column, row)
                    test_e_p = (column, row)
                    break

        return [word_found, begin_point, end_point]
