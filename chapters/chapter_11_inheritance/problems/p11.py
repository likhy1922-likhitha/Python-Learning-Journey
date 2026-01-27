'''
Class Father → method money()
Class Mother → method care()
Class Child inherits both

Call both methods.
'''
class Father:
    def money(self):
        print("This is the block of father where money is available")
class Mother:
    def care(self):
        print("This is the mother block where caring is available")
class Child(Father,Mother):
    print("this is the child block where both father and mother are called!")
# object creation
c = Child()
c.money()
c.care()