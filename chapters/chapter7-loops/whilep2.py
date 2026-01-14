# write a program to print the 
# content of a list using the while Loop
list = ["Akash","Akshaya",1,2,3,7,True,"Akshitha"]
i = 0
while(i<len(list)):
    print(list[i])
    i+=1
list.pop(True)# true is 1 and false is 0 so deletes the 1 index in python not true word
list.pop(6)
print(list)