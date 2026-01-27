class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)

o = person("Likhitha","Sanaboina")
o.printname()
# creting a child  class
class student(person):
    pass

x = student("Mike", "Olsen")
x.printname()