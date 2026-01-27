'''
Create a parent class Vehicle with a method start()
Create a child class Bike and call start() using a Bike object.
'''
class Vehicle:
    def start(self):
        print("starting the vehicle")
# child class
class Bike(Vehicle):
    pass
# calling the start using the Bike object
b = Bike()
b.start()