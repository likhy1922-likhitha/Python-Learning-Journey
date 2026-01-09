# write a program to check whether a person is eligible to vote (age>=18).
age = int(input("Enter the age: "))
if(age>=18 and age<=100):
    print("Eligible for vote")
elif(age>100):
    print("Enter the correct age.")
elif(age<0):
    print("Invalid input .Enter the correct age.not in negative")

else:
    print("not eligible to vote")
