'''
solve the code
class Father:
    def skills(self):
        print("Father knows driving")

class Mother:
    def skills(self):
        print("Mother knows cooking")


'''
class Father:
    def skills(self):
        print("Father knows driving")

class Mother:
    def skills(self):
        print("Mother knows cooking")

class Child(Father, Mother):
    def skills(self):
        # Call Father method using super()
        super().skills()  # This calls Father because of MRO
        # Call Mother method directly
        Mother.skills(self)
        # Child's own skill
        print("Child knows coding")

# Object creation
c = Child()
c.skills()   # <-- call the method with ()

