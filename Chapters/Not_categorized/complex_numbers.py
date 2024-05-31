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
