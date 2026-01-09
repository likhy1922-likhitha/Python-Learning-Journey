# A spam comment is defined  as a text contaning the following keywords :
# "Make a lot of money ","Buy now ","Subscribe this","click this ".Write a program to detect this spam.

comment= input("Write a comment here: ")
# if(comment =="Make a lot of money "or "Buy now " or"Subscribe this" or"click this"):
#     print("spam is detected")
# else:
#     print("Spam is not detected")

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "click this"
if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("Spam is detected")
else:
    print("Spam is not detected")
    print(comment)