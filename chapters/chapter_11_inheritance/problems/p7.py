'''
Parent class: Person
Constructor takes name

Child class: Student
Constructor takes roll_no

Create object and try printing both.

Goal: Notice what breaks and why.
'''
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
# child class
class Student(person):
    def __init__(self, fname, lname,rollno):
        super().__init__(fname, lname)# if it is not used then the error through that no attributes of fname,lname is printed overides the parent init function
        self.rollno = rollno 
# creating both 
s = Student("likhitha","Sanaboina",11)
print(s.fname)
print(s.lname)
print(s.rollno)