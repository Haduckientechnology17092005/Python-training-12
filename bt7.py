class String:
    def __init__(self, string):
        self.string = string
    def getString(self):
        return self.string
    def printString(self):
        print(self.string)

s = String("Hello, World!")
s.printString()