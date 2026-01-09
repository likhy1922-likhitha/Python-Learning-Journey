# write a program to check whether a number is a multiple of both 3 and 7 .
num = int(input("Enter the number : "))
if(num%3==0 and num%7==0):
    print(f"{num} is divisible by both 3 and 7 .")
else:
    print(f"{num} is not divisible by 3 and 7.")
