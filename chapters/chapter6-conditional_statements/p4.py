# write a program to find whether a  given username contains less than 10 characters or not 
username = input("Enter a Username: ")
length = len(username)
if(length<10):
    print(" Invaild USername.should be greater than 10 characters")
else:
    print("Valid username")