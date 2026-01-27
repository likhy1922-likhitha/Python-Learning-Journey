'''
Class LivingThing → method breathe()
Class Human inherits LivingThing
Class Student inherits Human

Call breathe() using Student object.
'''

class LivingThing:
    def breathe(self):
        print("This is the breathe section.")
class Human(LivingThing):
    pass
class Student(Human):
    pass
#  object creation
s = Student()
s.breathe()