class Recentangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getArea(self):
        return self.width * self.height
    def display(self):
        print("Width:", self.width, "Height:", self.height, "Area:", self.getArea())
Recentangle(5, 10).display()