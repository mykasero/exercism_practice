WHITE = "W"
BLACK = "B"
NONE = " "
UNKNOWN = "?"


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = 0 if self.rows == 0 else len(board[0])

    def onboard(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows

    def neighbors(self, x, y):
        nbr = []
        for mov_x in (-1, 1):
            if self.onboard(x + mov_x, y):
                nbr.append((x + mov_x, y))
        for mov_y in (-1, 1):
            if self.onboard(x, y + mov_y):
                nbr.append((x, y + mov_y))

        return nbr

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self.onboard(x, y):
            raise ValueError("Invalid coordinate")

        if self.board[y][x] != NONE:
            return NONE, set()

        owner = UNKNOWN
        visited = set()
        enclosed = set()
        stack = [(x, y)]

        while len(stack) != 0:
            c, r = stack.pop()
            visited.add((c, r))
            stone = self.board[r][c]
            if stone == NONE:
                enclosed.add((c, r))
                for n in self.neighbors(c, r):
                    if n not in visited:
                        stack.append(n)
            elif stone != owner:
                owner = stone if owner == UNKNOWN else NONE

        if owner == UNKNOWN:
            owner = NONE

        return owner, enclosed

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        t = {WHITE: set(), BLACK: set(), NONE: set()}

        vacant = set()

        for c in range(self.cols):
            for r in range(self.rows):
                if self.board[r][c] == NONE:
                    vacant.add((c,r))

        while len(vacant) != 0:
            v = vacant.pop()
            who, where = self.territory(v[0], v[1])
            vacant -= where
            t[who] |= where

        return t
