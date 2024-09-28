from student import Student
import random, string
def randomWord(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def createStudent():
    name = randomWord(6)
    age = random.randint(15, 20)
    math = random.randint(0, 10)
    literature = random.randint(0, 10)
    english = random.randint(0, 10)
    return Student(name, age, math, literature, english)
def showListStudents(listStudents):
    for student in listStudents:
        print("Name: "+ student.getName())
def main():
    student = Student("Kien", 19, 10, 9, 9)
    listStudents = []
    listStudents.append(student)
    print("List of students: ")
    showListStudents(listStudents)
    for i in range(10):
        listStudents.append(createStudent())
    print("List of students: ")
    showListStudents(listStudents)
    

if __name__ == "__main__":
    main()