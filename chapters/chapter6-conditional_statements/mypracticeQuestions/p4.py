# write a program to compare two numbers and print the larger one.
n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))
if(n1>n2):
    print(f"{n1} is a large number.")
elif(n2>n1):
    print(f"{n2} is a large number.")
else:
    print(f"{n1},{n2} both are equal")
