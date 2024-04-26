class ConnectGame:
    def __init__(self, board):
        self.board = [[stone for stone in row] for row in board.replace(' ', '').splitlines()]  # Generate 2d array
        self.neighbours = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]  # hex neighbours relative pos in array
        #         movement:   >       \/      \/<       <        /\      /\>

    def get_winner(self):  # check player 0, then X, if neither win output ' '
        for player in ['O', 'X']:
            result = self.checker(player)
            if result is True:
                return player
        return ''

    def checker(self, player):
        if player == 'O':  # set parameters for player O
            array = self.board
        if player == 'X':  # set parameters for player X
            array = list(zip(*self.board))  # transpose the board, so X becomes top to down
        # get player first and last row stones
        stones = []
        ends = []

        for index,stone in enumerate(array[0]):
            if stone == player:
                stones.append((index, 0))
                break

        for index, stone in enumerate(array[-1]):
            if stone == player:
                ends.append((index, len(array)-1))
                break

        # search for stones connected to first row stones, loop till exhaustion
        for stone in stones:
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                col = stone[0] + neighbour[0]
                if row >= 0 and col >= 0:
                    try:
                        if array[row][col] == player and (col, row) not in stones:
                            stones.append((col, row))  # append stone to end of list so it will be looped over
                    except IndexError:
                        continue

        # return true if one of the end stones is connected to first row stones
        for end in ends:
            if end in stones:
                return True


'''
Instructions
Compute the result for a game of Hex / Polygon.

The abstract boardgame known as Hex / Polygon / CON-TAC-TIX is quite simple in rules, though complex in practice. 
Two players place stones on a parallelogram with hexagonal fields. The player to connect his/her stones to the opposite side first wins. 
The four sides of the parallelogram are divided between the two players (i.e. one player gets assigned a side and the side directly 
opposite it and the other player gets assigned the two other sides).

Your goal is to build a program that given a simple representation of a board computes the winner (or lack thereof). 
Note that all games need not be "fair". (For example, players may have mismatched piece counts or the game's board might have a different width and height.)

The boards look like this:

. O . X .
 . X X O .
  O O O X .
   . X O X O
    X O O O X
"Player O" plays from top to bottom, "Player X" plays from left to right. 
In the above example O has made a connection from left to right but nobody has won since O didn't connect top and bottom.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/connect/canonical-data.json
