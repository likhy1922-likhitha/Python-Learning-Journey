class Student:
    course = "it"
    fee = 4000000
    timeLine = 4
    
    def __init__(self,name,course,fee,timeLine):
        print("I'm creating an object")
        self.name = name
        self.course = course
        self.fee = fee
        self.timeLine = timeLine

    def getInfo(self):
        print(f"the course is {self.course} with the timeLine {self.timeLine}")

    
    @staticmethod 
    def greet():
        print("Good Morning")
   
    
#object creation 
harika = Student("Harika","cse",5000000,5) #when you want to directly access through the instance attribute use the init 
print(harika.name,harika.course,harika.fee,harika.timeLine,sep=",")


