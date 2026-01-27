# the child init function is overrides the parent init function
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
    def __init__(self, fname, lname):
        # as using the init in child class overrides the parent init so we explicitly called the parent init function 
        person.__init__(self,fname,lname)

x = student("Mike", "Olsen")
x.printname()