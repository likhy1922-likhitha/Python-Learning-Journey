# write a program to check whether a number is 2 digit or 3 digit 
num = int(input("Enter a number: "))
if(num>=10 and num<=99):
    print(f"{num} is a 2 digit number.")
elif(num>=100 and num<=999):
    print(f"{num} is a 3 digit number.")
else:
    print(f"{num} is not a 2 or 3 digit number.")

    

