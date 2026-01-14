#until the object is instantiated the memory will not allocate to that object
# instance-->copy
class Dog:          # Class with content (method)
    def bark(self):
        print("Woof! Woof!")

# Creating objects
dog1 = Dog()
dog2 = Dog()

# Using the method
dog1.bark()  # Output: Woof! Woof!
dog2.bark()  # Output: Woof! Woof!
