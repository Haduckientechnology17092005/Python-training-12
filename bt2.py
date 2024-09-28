class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, width):
        super().__init__(width, width)

    def display(self):
        print("Width:", self.width, "Height:", self.height, "Area:", self.getArea())

s = Square(4)
s.display()