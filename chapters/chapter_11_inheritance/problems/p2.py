'''
Parent class: Person
Method: walk()

Child class: Student
No methods inside child

Call walk() using Student object.

Think: Why does this work even though Student has no method?
'''
# parent class
class Person:
    def Walk(self):
        print("the person Walked around 10kms.")
# child class
class Student(Person):
    pass

# object creation
c = Student()
c.Walk()
