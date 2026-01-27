class Employee:
    company = "ITc"
    def show(self):
        self.name = "Likhitha"
        language = "Python"
        print("this is from the Employee using the show fucnction")
        print(f"The name of Employee is {self.name}.")
    

class Programmer(Employee):
    company = "Itc Infotech"
    language = "Python"

    def ProgrammerLanguage(self):
        print("this is from the Employee using the show fucnction")
        print(f"The language is {self.language}")

Ob1 = Employee()
ob2 = Programmer()

print(Ob1.company,ob2.company)
print(Ob1.show(),ob2.ProgrammerLanguage())
