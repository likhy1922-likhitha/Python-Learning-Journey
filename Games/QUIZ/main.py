'''
Rules of the Game
1.The game asks for 5 question
2. User enter the answer
3.Each correct answer -->+1 point
4.wrong answer -->0 points
5.Shows the final score at the end
'''

score =0
print("Welcome to the quiz")

answer = input("1.What is the capital of the India: ").lower()
if(answer=="delhi"):
    print("Right Answer")
    score+=1
else:
    print("wrong answer")
    score+=0

answer = input("2.who discovered python: ").lower()
if(answer=="gudio"):
     print("Right Answer")
     score+=1
else:
    print("wrong answer")
    score+=0

answer = input("3.who stores the value in python: ").lower()
if(answer=="variable"):
     print("Right Answer")
     score+=1
else:
    print("wrong answer")
    score+=0

answer = input("4.Is python is case sensitive: ").lower()
if(answer=="yes"):
     print("Right Answer")
     score+=1
else:
    print("wrong answer")
    score+=0

answer = input("5.what is the datatype of '6': ").lower()
if(answer=="int"):
     print("Right Answer")
     score+=1
else:
    print("wrong answer")
    score+=0

print(f"Total Score of your quiz is : {score}/5")

