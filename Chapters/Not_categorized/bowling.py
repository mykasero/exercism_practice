# STATUS 10/31 passed

class BowlingGame:
    def __init__(self):
        self.throws = 0
        self.points = []
        self.frame = []
        self.counter = 0
        self.total = 0
        self.spare = False

    def roll(self, pins):
        self.counter += 1
        self.frame.append(pins)

        if self.spare == True:
            self.points[-1] += pins
            self.spare = False

        if len(self.frame) == 1 and self.frame[0] == 10:
            self.points.append(10)
            self.frame = []
        elif len(self.frame) == 2 and self.frame[0] + self.frame[1] == 10:
            self.points.append(10)
            self.frame = []
            self.spare = True
        elif len(self.frame) == 2 and self.frame[0] + self.frame[1] != 10:
            self.points.append(self.frame[0]+self.frame[1])
            self.frame = []


        STOP = "TEST"


    def score(self):
        for item in self.points:
            self.total += item

        return self.total

