class Car:
    def __init__(self, color):
        self.color = color
class Oto(Car):
    def display(self):
        print("Color car: "+ self.color)
oto = Oto("red")
oto.display()