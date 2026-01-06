import random
#imporitng the random  built  in Module
print("Roll the Dice!!")
user = input("Hit Enter to roll the dice")
#computer selects the number between the 1 to 6
Dice = random.randint(1,6)
print(f"{Dice} is the number rolled")
#conditions to win the Game
if(Dice==6):
    print("You Win")
else:
    print("Try Again")