class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
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

        left_right = self.left_right(splitted)


        if left_right[0] == True:
            return left_right[1], left_right[2]


        STOP = "TEST"

    def left_right(self,split_chars):
        splitted = split_chars
        begin_point = None
        end_point = None
        word_found = False
        check_word = ""

        for row in range(len(splitted)+1):
            if begin_point is not None and end_point is not None:
                temp_word = splitted[begin_point.y][begin_point.x:end_point.x + 1]
                check_word = "".join(temp_word)

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                    if row == len(splitted) + 1:
                        break
                else:
                    word_found = True
                    #splitted.pop(row)
                    break

            elif begin_point is not None and end_point is None:
                begin_point = None
                end_point = None

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
