import random
#computer will select a random number
computer = random.randint(1,100)
print("Select a Random number between 1 to 100")

#this loop will check until the condition will become false
#atleast it will exceute one time also
user =""
while(computer!=user):
    user = int(input("Enter a number: "))
    if (computer>user):
        print("Low number")
    elif(computer<user):
        print("High number")
    else:
        print("Congratualtions Gussed correct one.")
        

            

                 