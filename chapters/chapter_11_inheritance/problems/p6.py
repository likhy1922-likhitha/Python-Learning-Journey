'''
Parent class: Bank
Method: interest() → prints "General interest"

Child class: SavingsBank
Override interest() → prints "Savings bank interest"

Call method using child object.
'''
class Bank:
    def interset(self):
        print("General interest!")
# child
class SavingBank(Bank):
    def interset(self):
        print("Saving Bank interest!")
# calling method using the child class
c = SavingBank()
c.interset()