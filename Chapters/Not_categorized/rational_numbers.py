import math

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        is_eq = self.numer == other.numer and self.denom == other.denom
        if is_eq == True:
            return True
        else:
            if self.numer == 0 or other.numer == 0:
                return True
            else:
                x = math.gcd(self.denom,other.denom)

                if (self.numer < 0 or self.denom < 0) and (other.numer < 0 or other.denom < 0):
                    self.numer = abs(self.numer)
                    self.denom = abs(self.denom)
                    other.numer = abs(other.numer)
                    other.denom = abs(other.denom)

                elif self.denom < 0:
                    self.numer = -self.numer
                    self.denom = abs(self.denom)

                elif other.denom < 0:
                    other.numer = -other.numer
                    other.denom = abs(other.denom)
                if x > 1:
                    if self.denom != x:
                        if other.numer == 1:
                            self.numer /= x
                            self.denom /= x
                        else:
                            self.numer /= other.numer
                            self.denom /= other.numer
                    elif other.denom != x:
                        if self.numer == 1:
                            other.numer /= x
                            other.denom /= x
                        else:
                            other.numer /= self.numer
                            other.denom /= self.numer
                else:
                    if self.numer > other.numer:
                        self.numer /= self.denom
                        self.denom /= self.denom

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
        return round(math.exp(math.log(pow(base,self.numer))/self.denom), 8)

'''
Instructions
A rational number is defined as the quotient of two integers a and b, called the numerator and denominator, respectively, where b != 0.

Note
Note that mathematically, the denominator can't be zero. However in many implementations of rational numbers, you will find that the denominator is allowed 
to be zero with behaviour similar to positive or negative infinity in floating point numbers. In those cases, the denominator and numerator generally still 
can't both be zero at once.

The absolute value |r| of the rational number r = a/b is equal to |a|/|b|.

The sum of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ + r₂ = a₁/b₁ + a₂/b₂ = (a₁ * b₂ + a₂ * b₁) / (b₁ * b₂).

The difference of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ - r₂ = a₁/b₁ - a₂/b₂ = (a₁ * b₂ - a₂ * b₁) / (b₁ * b₂).

The product (multiplication) of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ * r₂ = (a₁ * a₂) / (b₁ * b₂).

Dividing a rational number r₁ = a₁/b₁ by another r₂ = a₂/b₂ is r₁ / r₂ = (a₁ * b₂) / (a₂ * b₁) if a₂ is not zero.

Exponentiation of a rational number r = a/b to a non-negative integer power n is r^n = (a^n)/(b^n).

Exponentiation of a rational number r = a/b to a negative integer power n is r^n = (b^m)/(a^m), where m = |n|.

Exponentiation of a rational number r = a/b to a real (floating-point) number x is the quotient (a^x)/(b^x), which is a real number.

Exponentiation of a real number x to a rational number r = a/b is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.

Implement the following operations:

addition, subtraction, multiplication and division of two rational numbers,
absolute value, exponentiation of a given rational number to an integer power, exponentiation of a given rational number to a real (floating-point) power, 
exponentiation of a real number to a rational number.
Your implementation of rational numbers should always be reduced to lowest terms. 
For example, 4/4 should reduce to 1/1, 30/60 should reduce to 1/2, 12/8 should reduce to 3/2, etc. 
To reduce a rational number r = a/b, divide a and b by the greatest common divisor (gcd) of a and b. So, for example, 
gcd(12, 8) = 4, so r = 12/8 can be reduced to (12/4)/(8/4) = 3/2. The reduced form of a rational number should be in "standard form" 
(the denominator should always be a positive integer). If a denominator with a negative integer is present, multiply both numerator and denominator by -1 to 
ensure standard form is reached. For example, 3/-4 should be reduced to -3/4
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/rational-numbers/canonical-data.json
