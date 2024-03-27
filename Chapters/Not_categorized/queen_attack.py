class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if self.row < 0:
            raise ValueError("row not positive")
        elif self.column < 0:
            raise ValueError("column not positive")
        elif self.row > 7:
            raise ValueError("row not on board")
        elif self.column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        temp_row = self.row
        temp_column = self.column
        can_attack = False

        # diag 0 = +row,column; diag 1 = -row, +column; diag 2 = +row,-column; diag 3 = -row,-column; diag 4 = cannot attack diagonally
        diag = 0
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        elif self.row == another_queen.row or self.column == another_queen.column:
            return True
        else:
            # 4 loops each inc or decrementing one coord
            # increase row and column
            if diag == 0:
                temp_row = self.row
                temp_column = self.column

                for move1 in range(8 - self.row):
                    if temp_row == another_queen.row and temp_column == another_queen.column:
                        can_attack = True
                        break
                    else:
                        temp_row += 1
                        temp_column += 1

                if can_attack == True:
                    return True
                else:
                    diag += 1

            # decrease row increase column
            if diag == 1:
                temp_row = self.row
                temp_column = self.column
                for move1 in range(self.row + 1):
                    if temp_row == another_queen.row and temp_column == another_queen.column:
                        can_attack = True
                        break
                    else:
                        temp_row -= 1
                        temp_column += 1

                if can_attack == True:
                    return True
                else:
                    diag += 1
            # increase row, decrease column
            if diag == 2:
                temp_row = self.row
                temp_column = self.column
                for move1 in range(self.column + 1):
                    if temp_row == another_queen.row and temp_column == another_queen.column:
                        can_attack = True
                        break
                    else:
                        temp_row += 1
                        temp_column -= 1

                if can_attack == True:
                    return True
                else:
                    diag += 1

            # decrease column
            if diag == 3:
                temp_row = self.row
                temp_column = self.column
                for move1 in range(self.column + 1):
                    if temp_row == another_queen.row and temp_column == another_queen.column:
                        can_attack = True
                        break
                    else:
                        temp_row -= 1
                        temp_column -= 1

                if can_attack == True:
                    return True
                else:
                    diag += 1

            # all diagonal options checked without succes = cannot attack
            if diag == 4:
                return False

'''
Instructions
Given the position of two queens on a chess board, indicate whether or not they are positioned so that they can attack each other.

In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal.

A chessboard can be represented by an 8 by 8 array.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/queen-attack/canonical-data.json
