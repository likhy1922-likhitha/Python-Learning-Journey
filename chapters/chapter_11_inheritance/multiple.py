# creating the class - parent - 1
class Employee:
    company = "ITC"
    name = "Likhitha"
    salary = 450000

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# creating the class - parent - 2
class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages, your language is: {self.language}")

# creating the child class using both parents
class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The company is {self.company} and she is good at {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()
