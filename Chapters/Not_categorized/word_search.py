#STATUS works for left to right 12/24 Passed
import itertools
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
        #              R      D      L      U      TL     TR     BL     BR
        DIRECTIONS = [0,1,-1]

        begin_point = None
        end_point = None

        self.word = word
        splitted = []
        part = []

        for item in self.puzzle:
            for element in item:
                part.append(element)
            splitted.append(part)
            part = []

        move_dir = itertools.combinations_with_replacement(DIRECTIONS, 2)
        check_word = ""

        row = 0
        column = 0
        ctr = 0
        loops = 0
        while check_word != self.word:
            move_dir = itertools.combinations_with_replacement(DIRECTIONS, 2)
            if splitted[row][column] == self.word[ctr]:
                if ctr == 0:
                    begin_point = Point(column, row)
                    check_word += splitted[row][column]
                    ctr += 1

            for x_move, y_move in move_dir:
                if -1 < row + x_move < len(splitted) and -1 < column + y_move < len(splitted[0]) and (x_move + y_move != 0):
                    if splitted[row + x_move][column + y_move] == self.word[ctr]:
                        check_word += splitted[row + x_move][column + y_move]
                        row += x_move
                        column += y_move
                        if ctr == 0:
                            begin_point = Point(column, row)

                        ctr += 1
                        if len(check_word) == len(self.word):
                            end_point = Point(column, row)
                        break


            if loops > 0 and begin_point is None:
                column += 1

            loops += 1

            if loops == len(splitted) * len(splitted[0]):
                return None
            elif loops == len(splitted[0]) and len(check_word) != len(self.word):
                ctr = 0
                loops = 0
                check_word = ""
                row += 1
                column = 0

        return begin_point, end_point
