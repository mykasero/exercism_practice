class BowlingGame:
    def __init__(self):
        self.throws = 0
        self.points = []
        self.frame = []
        self.counter = 0

    def roll(self, pins):
        self.counter += 1
        if pins == 10:
            self.points([10])
        else:
            if len(self.frame) < 2:
                self.frame.append(pins)
                if len(self.frame) == 2:
                    self.points.append(self.frame)
                    self.frame = []

        STOP = "TEST"


    def score(self):
        pass

