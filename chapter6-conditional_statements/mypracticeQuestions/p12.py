# write a program to check whether a temperature is cold warm or hot .
temp = int(input("Enter the temperature: "))
if(temp<20):
    print("cold")
elif(temp<=30):
    print("Warm")
else:
    print("Hot")