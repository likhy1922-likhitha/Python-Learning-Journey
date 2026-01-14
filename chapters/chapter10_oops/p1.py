'''
Create a class “Programmer” for storing information of few programmers
working at Microsoft.
'''
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p1 = Programmer("Shreya",40000,5000054)
print(p1.company,p1.name,p1.salary,p1.pincode)

p2 = Programmer("Geetha",70000,500053)
print(p2.company,p2.name,p2.salary,p2.pincode,sep = ",")