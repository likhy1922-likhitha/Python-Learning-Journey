# write a program to check whether a character is vowel or consonant.
ch = input("Enter the character: ")
if(len(ch)==1):
    if((ch=="a")or(ch=="e") or(ch=="i") or (ch =="o") or(ch =="u")):
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Enter the single alphabet.")

