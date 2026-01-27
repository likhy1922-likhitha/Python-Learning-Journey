# one class use the properteis and methods  of other class
class Parent:
    def Inherit(self):
        print("the parent block")
        # it has only one method that is Inherit
# creting a class
class Child(Parent):
    pass
# child inherits form the parent class


# to use the child class
p = Child()#evenn though the Child has no method it uses the parent method
p.Inherit()