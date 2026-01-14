class student():
    course = "IT"
    fee=4000000
    timeLine="4years"

    def getInfo(self):
        print(f"The fee is : {self.fee}.The time line is {self.timeLine},Enrolled course is {self.course} ")

shreya = student()
shreya.course="CSE"
print

shreya.getInfo()
# it means so make it self
#student.getInfo(shreya)
# instead o self anuthing canbe wriiten but self will be more descripitive right
