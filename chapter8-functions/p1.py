# write a program using functions to find the 
# geratest of three numbers
def great(a,b,c):
    if (a>b and a>c):
        print(f"{a} is the greatest number.")
    elif(b>a and b>c):
        print(f"{b} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")
great(10,12,13)
great(1,2,113)
great(0,2,19)
great(102,287,13)

