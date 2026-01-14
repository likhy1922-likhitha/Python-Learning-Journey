'''
__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor.
It takes ‘self’ argument and can also take further arguments.
For Example:
class Employee:
def __init__(self, name):
self.name=name
def getSalary(self):
...
harry = Employee("Harry")
'''

class Student:
    course = "it"
    fee = 4000000
    timeLine = 4
    #function one --> method one
    def __init__(self):#which is automatically called  and also called as dundar method  only called when you create a object
        print("I'm creating an object")

    def getInfo(self):
        print(f"the course is {self.course} with the timeLine {self.timeLine}")

    #function 2 method 2
    @staticmethod # when you wont need any parameter as a self
    def greet():
        print("Good Morning")
   
    
#object creation 
harika = Student()
print(harika.fee)
# harika.getInfo()
# harika.greet()
