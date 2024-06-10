# STATUS 17/31 passed

class BowlingGame:
    def __init__(self):
        self.throws = 0
        self.points = []
        self.frame = []
        self.counter = 0
        self.total = 0
        self.spare = False
        self.strike = False
        self.strike_ctr = 0

    def roll(self, pins):
        self.counter += 1

        if not 0 <= pins <= 10 and self.counter < 18:
            raise ValueError("invalid fill balls")

        else:
            self.frame.append(pins)

        if self.strike == True:
            if pins != 10:
                self.points.append(pins)
                self.strike_ctr += 1
                if self.strike_ctr == 2:
                    self.strike = False
            elif len(self.frame) == 2 and self.frame[0] + self.frame[1] == 20:
                self.points.append(20)


            # if len(self.frame) == 1:
            #     if self.frame[0] != 10:
            #         self.points.append(2*self.points[-1])
            #         self.points.append(10)
            #         self.points.append(pins)
            #         self.strike_ctr +=1
            # else:
            #     if self.frame[0] != 10 and self.frame[1] != 10:
            #         self.points.append(pins)
            #         self.strike_ctr += 1
            #         # if self.strike_ctr == 2:
            #         #     self.strike = False
            #
            #     elif self.frame[0] == 10 and self.frame[1] != 10:
            #         self.points.append(10)
            #         self.strike_ctr += 1
            #         # if self.strike_ctr == 2:
            #         #     self.strike = False
            #
            #     elif len(self.frame) == 2 and self.frame[0] + self.frame[1] == 20:
            #         self.points.append(20)

            if self.strike_ctr == 2:
                self.strike = False

        if self.spare == True:
            self.points[-1] += pins
            self.spare = False

        if len(self.frame) == 2 and self.frame[0] + self.frame[1] > 10:
            total = self.frame[0] + self.frame[1]
            if self.counter < 20:
                raise ValueError("invalid fill balls")
            elif self.counter >= 20 and (total >= 21 or total < 20) or self.counter >= 20 and len(self.frame) == 1:
                raise IndexError("cannot throw bonus with an open tenth frame")


        elif pins > 10 and self.counter >= 18:
            raise IndexError("cannot throw bonus with an open tenth frame")

        elif len(self.frame) == 1 and self.frame[0] == 10 and self.strike == False:
            # self.points.append(10)
            #self.frame = []
            self.strike = True
        elif len(self.frame) == 2 and self.frame[0] + self.frame[1] == 20 and self.strike == True:
            self.points[-1] += 10
            self.frame = []
            self.strike = False
        elif len(self.frame) == 2 and self.frame[0] + self.frame[1] == 10:
            self.points.append(10)
            self.frame = []
            self.spare = True
        elif len(self.frame) == 2 and self.frame[0] + self.frame[1] != 10:
            self.points.append(self.frame[0])
            self.points.append(self.frame[1])
            self.frame = []


        STOP = "TEST"
        if sum(self.points) == 0 and self.counter > 20:
            raise ValueError("invalid fill balls")

    def score(self):
        if self.points == []:
            raise ValueError("invalid fill balls")
        else:
            for item in self.points:
                self.total += item

        if self.total == 0:
            raise ValueError("invalid fill balls")

        return self.total

