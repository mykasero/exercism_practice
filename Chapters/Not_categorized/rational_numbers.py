#STATUS 33/43 Passed

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        x,y = self.denom, other.denom
        self.numer *= other.denom
        other.numer *= self.denom
        self.denom = x * y
        other.denom = x * y
        if self.numer + other.numer == 0:
            return Rational(self.numer+other.numer,1)
        else:
            return Rational(self.numer + other.numer, self.denom)

    def __sub__(self, other):
        x, y = self.denom, other.denom
        self.numer *= other.denom
        other.numer *= self.denom
        self.denom = x * y
        other.denom = x * y
        if self.numer - other.numer == 0:
            return Rational(self.numer - other.numer, 1)
        else:
            return Rational(self.numer - other.numer, self.denom)

    def __mul__(self, other):
        x = (self.numer*self.denom)
        y = (other.denom*other.numer)

        if x == y:
            return Rational(1,1)
        elif x == 0 or y == 0:
            return Rational(0,1)
        elif self.denom < other.denom:
            if self.numer < 0 and other.numer < 0 :
                return Rational(abs(x/self.denom), abs(y/self.denom))
            else:
                return Rational(x / self.denom, y / self.denom)
        else:
            if self.numer < 0 and other.numer < 0 :
                return Rational(abs(y/other.denom), abs(x/other.denom))
            else:
                return Rational(y/other.denom, x/other.denom)


    def __truediv__(self, other):
        x = self.numer * other.denom
        y = self.denom * other.numer

        if x < 0 and y < 0:
            return Rational(abs(x),abs(y))
        elif y < 0:
            return Rational(-x ,abs(y))
        else:
            return Rational(x, y)

    def __abs__(self):
        if self.numer > 1 and self.denom % self.numer == 0:
            return Rational(abs(self.numer/self.numer),abs(self.denom/self.numer))
        else:
            return Rational(abs(self.numer),abs(self.denom))

    def __pow__(self, power):
        x = self.numer
        y = self.denom
        # if power > 0:
        for i in range(abs(power)-1):
            if abs(x) == 1:
                y *= self.denom
            else:
                x *= self.numer
                y *= self.denom

        if abs(power) % 2 == 0 and (x < 0 or y < 0):
            x = abs(x)
            y = abs(y)

        if power == 0:
            return Rational(1,1)

        elif power > 0:
            if y < 0:
                x = -x
                y = abs(y)

            return Rational(x,y)

        else:
            if x < 0 :
                x = abs(x)
                y = -y

            return Rational(y,x)

    def __rpow__(self, base):
        pass
