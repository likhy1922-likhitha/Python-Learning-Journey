# write a program to check whether  a character is an aplhabet ,digit or special character.
value = input("Enter the value: ")
if(value.isalpha()):
    print(f"{value} is a alphabet.")
elif(value.isdigit()):
    print(f"{value} is a digit.")
else:
    print(f"{value} is a special character.")