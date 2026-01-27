'''
Problem 1 — Student Grades System

Description:

Create a parent class Person with attributes name and age.

Create a child class Student that inherits from Person and adds marks (a dictionary of subjects).

Add a method in Student to calculate the average mark and print "Pass" if average ≥ 50 else "Fail".

Use loops to:

Print each subject and mark

Print only subjects where marks < 50

Use input to let the user enter name, age, and marks for 3 subjects.

'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks = marks
    def averageMarks(self):
        sum = 0
        for i in range(n):
            sum +=i
        avg = sum/n
        if(avg>=50):
            print("pass")
        else:
            print("Failed")
       
name = (input("Enter the Name: "))
age = int(input("Enter the Age: "))
my_dict = {}
n = int(input("enter the howo many subjects: "))
for i in range(3):
    key = input(f"Enter the Subjects {i+1}: ")
    value = int(input(f"Enter the Marks of the subjects {key}: "))
    my_dict[key]= value
print("Entered Subjects along with marks are: ",my_dict)
ob1 = Student()

print("The average of the entered subjects are : ",ob1.averageMarks)



