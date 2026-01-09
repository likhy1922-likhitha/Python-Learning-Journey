# write a program to find the largest of three numbers 
num1 = int(input ("Enter the number 1 : "))
num2 = int(input ("Enter the number 2 : "))
num3 = int(input ("Enter the number 3 : "))
if(num1>num2 and num1>num3):
    print(f"{num1} is the largest number.")
elif(num2>num1 and num2>num3):
    print(f"{num2} is the largest number.")
elif(num3>num1 and num3>num2):
    print(f"{num3} is the largest number.")
else:
    print("All are Equal.")

