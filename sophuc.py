class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

if __name__ == "__main__":
    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(7, 11)
    print("Complex Number 1:", num1.getData())
    print("Complex Number 2:", num2.getData())
    num2 = ComplexNumber(5)
    num2.attr = 10
    num1.attr = 6
    print("Complex Number 2:", num2.imag, num2.real, num2.attr)
    print("Complex Number 1:", num1.imag, num1.real, num1.attr)