import random
'''
The game() function in a program lets a user play 
a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’
which is either blank or
contains the previous Hi-score. 
You need to write a program to update the Hiscore 
whenever the game() function breaks the Hi-score
the given code we have to do :
1.create a game function
2.player should play the game computer return the score as an integer
3.we should update the score whenever makes the high score
'''
def game():
    print("your are playing the game")
    score= random.randint(1,62)
    #fetching the  hiscore
    with open("Hi-score.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore= 0
    print(f"Your score: {score}")
    if(score>hiscore or hiscore==""):
        # write this hiscore in file
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
        return score
game()
    
    
