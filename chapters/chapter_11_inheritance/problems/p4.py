'''
Parent class: Employee
Method: work()

Child class: Developer
Method: code()

Call both methods.
'''
class Employee:
    def work(self):
        print("This the work place.")
# child class
class Developer(Employee):
    def code(self):
        print("this is the code area.")
d = Developer()
d.work()
d.code()