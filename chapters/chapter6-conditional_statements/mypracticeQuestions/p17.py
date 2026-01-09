# write a program to check whether a triangle is valid (sum angles = 180)
side1 = int(input("Enter the side1: "))
side2 = int(input("Enter the side2: "))
side3 = int(input("Enter the side3: "))
sum = side1+side2+side3
if(sum==180):
    print(f"{side1},{side2},{side3} sum is {sum} so it is a triangle.")
else:
    print("It is not a Triangle.")