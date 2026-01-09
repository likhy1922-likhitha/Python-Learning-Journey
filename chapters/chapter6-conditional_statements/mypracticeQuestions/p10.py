# write a program to check whether a character is uppercase or lowercase.
ch = input("Enter a character: ")
if(len(ch)==1):
    if(ch==ch.lower()):
        print(f"{ch} is in lower Case.")
    elif(ch==ch.upper()):
        print(f"{ch} is in upperCase.")
    else:
        print(f"{ch} please enter a charcter between a to z.")
else:
    print("Enter only single character.")