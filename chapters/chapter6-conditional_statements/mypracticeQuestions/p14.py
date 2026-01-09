# write a program to check whether a number is divisible by 2, 3 both
num = int(input("Enter a number: "))
if(num%2==0 and num%3==0):
    print(f"{num} is divisible by both numbers 2 and 3 .")
else:
    print(f"{num} is not divisible by 2 and 3 .")