# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"

dirs = {0 : NORTH, 1 : EAST, -1: WEST, 2: SOUTH, -2: SOUTH}
key_list = list(dirs.keys())
val_list = list(dirs.values())
class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._dir = direction
        self._x = x_pos
        self._y = y_pos
        self.start_pos = key_list[val_list.index(self._dir)]
    @property
    def coordinates(self):
        return self._x, self._y
    @property
    def direction(self):
        return self._dir

    def move(self,mvmt):
        for steps in mvmt:
            if steps == "R":
                if self._dir == SOUTH:
                    self.start_pos = -1
                else:
                    self.start_pos +=1
            elif steps == "L":
                if self._dir == SOUTH and self.start_pos == -2:
                    self.start_pos = 1
                else:
                    self.start_pos -=1
            elif steps == "A":
                if self._dir == NORTH:
                    self._y += 1
                elif self._dir == EAST:
                    self._x +=1
                elif self._dir == SOUTH:
                    self._y -= 1
                elif self._dir == WEST:
                    self._x -= 1
            self._dir = dirs[self.start_pos]
        return self._dir