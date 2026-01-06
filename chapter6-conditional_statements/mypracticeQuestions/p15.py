#  # write a program to write a simple calulator
num1 = int(input("Enter a operand 1 : "))
num2 = int(input("Entera operand 2: "))
op = input("Enter a opertor: ")
if(op =="+"):
    sum = num1+num2
    print(f" sum of {num1},{num2} is {sum}.")
elif(op =="-"):
    sub = num1-num2
    print(f" subtraction of {num1},{num2} is {sub}.")
elif(op =="*"):
    mul = num1*num2
    print(f" mul of {num1},{num2} is {mul}.")
elif(op =="/"):
    div = num1/num2
    print(f" div of {num1},{num2} is {div}.")
elif(op =="%"):
    modul = num1%num2
    print(f" modul of {num1},{num2} is {modul}.")
else:
    print("Enter a valid values.")

