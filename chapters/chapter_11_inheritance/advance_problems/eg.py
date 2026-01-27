class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def averageMarks(self):
        total = sum(self.marks.values())
        n = len(self.marks)
        avg = total / n
        print(f"Average Marks: {avg:.2f}")
        if avg >= 50:
            print("Pass")
        else:
            print("Fail")
        return avg

    def printSubjects(self):
        print("All subjects and marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

    def printFailedSubjects(self):
        print("Subjects with marks < 50:")
        for subject, mark in self.marks.items():
            if mark < 50:
                print(f"{subject}: {mark}")

# Input from user
name = input("Enter the Name: ")
age = int(input("Enter the Age: "))
marks = {}
for i in range(3):
    subject = input(f"Enter Subject {i+1}: ")
    mark = int(input(f"Enter Marks for {subject}: "))
    marks[subject] = mark

# Create student object
student = Student(name, age, marks)

# Output
student.printSubjects()
student.printFailedSubjects()
student.averageMarks()
