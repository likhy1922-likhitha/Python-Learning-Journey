import random 
# importing the moduel which is built in python


user = input("Enter your choice: ").lower()
choices = ["r","p","s"]
computer = random.choice(choices)

print(f"you choosed the {user} and computer choosed {computer}")

if(computer == user):
    print("IT'S a  Tie!!!!.........")
else:
    if((computer == "r")and(user == "s")):
        print("You Loss the Game!")
    elif((computer == "s")and(user == "r")):
        print("you Won the Game!")
    elif((computer == "s")and(user == "p")):
        print("you Loss the Game! ")
    elif((computer == "p")and(user == "s")):
        print("you Won the Game!")
    elif((computer == "p") and (user == "r")):
        print("you Loss the Game!")
    elif((computer == "r") and (user == "p")):
        print("you Loss the Game!")
    else:
        print("something went wrong!!: once try again ")



        
        




