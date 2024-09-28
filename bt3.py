class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def getData(self):
        print(self.real, "+", self.imag, "i")
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)
    def __mul__(self, other):
        r = self.real * other.real
        i = self.imag * other.imag
        return ComplexNumber(r, i)
    def __truediv__(self, other):
        r = self.real / other.real
        i = self.imag / other.imag
        return ComplexNumber(r, i)

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(7, 11)
print((num1 + num2).getData())
print((num1 - num2).getData())
print((num1 * num2).getData())
print((num1 / num2).getData())