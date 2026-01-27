'''
Parent class: Animal
Method: eat()

Child class: Dog
Method: bark()

Call both methods using Dog object.

Goal: Child has parent + its own behavior.
'''
# parent class 
class Animal:
    def eat(self):
        print("Animals eat's the food.")

class Dog(Animal):
    def bark(self):
        print("Dog barks!")
# calling the both methods using the Dog object
d = Dog()
d.eat()
d.bark()