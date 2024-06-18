#STATUS 14/24 passed
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
        for row in range(len(splitted)):
            if begin_point is not None and end_point is not None:
                temp_word = splitted[begin_point.y][begin_point.x:end_point.x + 1]
                check_word = "".join(temp_word)

                if check_word != self.word:
                    begin_point = None
                    end_point = None
                else:
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


        STOP = "TEST"

        if begin_point is None or end_point is None:
            return None
        else:
            return begin_point, end_point
