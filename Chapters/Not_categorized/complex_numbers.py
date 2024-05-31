import math
class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __radd__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __rmul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        return ComplexNumber(self.real-other.real, self.imaginary-other.imaginary)

    def __rsub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        return ComplexNumber((self.real-other.real) * -1, (self.imaginary-other.imaginary) * -1)

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real = ((self.real*other.real)+(self.imaginary*other.imaginary)) / (pow(other.real,2)+pow(other.imaginary,2))

        imaginary = (((self.imaginary*other.real)-(self.real*other.imaginary))
                     /(pow(other.real,2)+pow(other.imaginary,2)))

        return ComplexNumber(real,imaginary)

    def __rtruediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        return other/self

    def __abs__(self):
        return math.sqrt(pow(self.real,2)+pow(self.imaginary,2))

    def conjugate(self):
        return ComplexNumber(self.real,self.imaginary * -1)

    def exp(self):
        real_part = math.cos(self.imaginary) * math.exp(self.real)
        imaginary_part = math.sin(self.imaginary) * math.exp(self.real)

        return ComplexNumber(real_part, imaginary_part)

'''
nstructions
A complex number is a number in the form a + b * i where a and b are real and i satisfies i^2 = -1.

a is called the real part and b is called the imaginary part of z. 
The conjugate of the number a + b * i is the number a - b * i. 
The absolute value of a complex number z = a + b * i is a real number |z| = sqrt(a^2 + b^2). 
The square of the absolute value |z|^2 is the result of multiplication of z by its complex conjugate.

The sum/difference of two complex numbers involves adding/subtracting their real and imaginary parts separately:
(a + i * b) + (c + i * d) = (a + c) + (b + d) * i, (a + i * b) - (c + i * d) = (a - c) + (b - d) * i.

Multiplication result is by definition (a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i.

The reciprocal of a non-zero complex number is 1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i.

Dividing a complex number a + i * b by another c + i * d gives: (a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i.

Raising e to a complex exponent can be expressed as e^(a + i * b) = e^a * e^(i * b), the last term of which is given by Euler's formula e^(i * b) = cos(b) + i * sin(b).

Implement the following operations:

addition, subtraction, multiplication and division of two complex numbers,
conjugate, absolute value, exponent of a given complex number.
Assume the programming language you are using does not have an implementation of complex numbers.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/complex-numbers/canonical-data.json
