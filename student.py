class Student:
    def __init__(self, name, age, math, literature, english):
        self.name = name
        self.age = age
        self.math = math
        self.literature = literature
        self.english = english
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def Average(self):
        return (self.math + self.literature + self.english) / 3
    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Math: " + str(self.math))
        print("Literature: " + str(self.literature))
        print("English: " + str(self.english))
        print("Average: " + str(self.Average()))
def __main__():
    student = Student("Kien", 19, 10, 9, 9)
    student.display()

if __name__ == "__main__":
    __main__()
    