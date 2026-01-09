# write a program to Scholarship eligibilty based on the marks +income
marks = int(input("Enter your marks: "))
income = int(input("Enter your income: "))
if(marks>75 and income<300000):
   print("Eligible for the schlarship")
else:
    print("Not Eligible .")