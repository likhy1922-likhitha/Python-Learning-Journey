'''
static method
Sometimes we need a function that does not use the self-parameter. We can define a
static method like this:
@staticmethod # decorator to mark greet as a static method
def greet():
    print("Hello")
'''
# class creation
class Student:
    course = "it"
    fee = 4000000
    timeLine = 4
    #function one --> method one
    def getInfo(self):
        print(f"the course is {self.course} with the timeLine {self.timeLine}")
    #function 2 method 2
    @staticmethod # when you wont need any parameter as a self
    def greet():
        print("Good Morning")
#object creation 
harika = Student()
print(harika.fee)
harika.getInfo()
harika.greet()
