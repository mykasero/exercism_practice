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
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary

        return ComplexNumber(real,imaginary)


    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        if (self.imaginary * other.imaginary) != 0 :
            real = ((self.real * other.real) - (self.imaginary * other.imaginary))

            imaginary = ((self.imaginary*other.real) + (self.real*other.imaginary))

            return ComplexNumber(real,imaginary)
        else:
            return ComplexNumber(self.real*other.real, self.imaginary*other.imaginary)

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        return ComplexNumber(self.real-other.real, self.imaginary-other.imaginary)

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            other = ComplexNumber(other)

        real = (((self.real*other.real)+(self.imaginary*other.imaginary)) /
                ((other.real*other.real)+(other.imaginary*other.imaginary)))

        imaginary = (((self.imaginary*other.real)-(self.real*other.imaginary)) /
                     ((other.real*other.real)+(other.imaginary*other.imaginary)))


        return ComplexNumber(real,imaginary)

    def __abs__(self):
        pass

    def conjugate(self):
        self.imaginary *= -1

        return ComplexNumber(self.real,self.imaginary)

    def exp(self):
        pass
