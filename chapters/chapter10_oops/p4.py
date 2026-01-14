'''
Add a static method in problem 2, to greet the user with hello.

'''
class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
         print(f"{self.n*self.n}")
    def cube(self):
         print(f"{self.n*self.n*self.n}")
    def squareroot(self):
         print(f"{self.n**1/2}")
    @staticmethod
    def greet():
         print("hello")
    
# a = Calculator(4)

m = int(input("Enter the number: "))
a = Calculator(m)
a.greet()
a.square()
a.cube()
a.squareroot()
