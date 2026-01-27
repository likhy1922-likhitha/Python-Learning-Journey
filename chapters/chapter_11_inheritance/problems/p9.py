'''
Parent class: Device
Constructor takes brand

Child class: Laptop
Constructor takes brand and ram

Use super() properly.
'''
class Device():
    def __init__(self,brand):
        self.brand = brand
# child class
class Laptop(Device):
    def __init__(self,brand,ram):
        super().__init__(brand)
        self.ram = ram
# object creation
l = Laptop("Hp",256)
print(l.brand)
print(l.ram)

