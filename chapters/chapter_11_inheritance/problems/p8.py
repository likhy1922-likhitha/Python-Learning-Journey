'''
Fix Problem 7 using super() so both name and roll_no work.
'''
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
        super().__init__(fname, lname)
        self.rollno = rollno 
# creating both 
s = Student("likhitha","Sanaboina",11)
print(s.fname)
print(s.lname)
print(s.rollno)