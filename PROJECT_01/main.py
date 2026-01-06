import random
'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.
''''''
1 is for snake
-1 for water
0 for gun
'''

computer = random.choice([1,-1,0])
youstr = input("Enter you choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

younum = youDict[youstr]

print(f"You choosed {reverseDict[younum]} Computer Choosed {reverseDict[computer]}")
if(computer==younum):
    print("Its a Draw!!")
else:
    if((computer==-1 and younum==1)or(computer==0 and younum==0)or(computer==-1 and younum==-1)):
        print("You Win")
    elif(computer ==-1 and younum ==0):
        print("You Lose!")
    elif(computer==1 and younum == -1):
        print("You Lose!")
    elif(computer ==1 and younum ==0):
        print("You win!")
    elif(computer==0 and younum == -1):
        print("You Win!")
    elif(computer ==0 and younum ==1):
        print("You Lose!")
    
    else:
        print("Something Went wrong")



