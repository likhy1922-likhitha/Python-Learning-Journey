import random
computer = random.choice([1,-1,0])
youstr=input("Enter Your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

younum = youDict[youstr]

print(f"You choosed {reverseDict[younum]} Computer Choosed {reverseDict[computer]}")
if(computer==younum):
    print("Its a Draw!!")
else:
    if((computer-younum==-2)or(computer-younum==1)):
        #here if computer choosed a number and you choosed a number there subtarction is 
        #1,2,-1 then you Lose the game or -2 1 then you won the game
        print("You Win!")
    else:
        print("You Lose!")
    # just observe the pattern  you choose the any pattern 
    # if you want decrease the lines of code
    # then try with the patterns
    
    



