# write a program to find the youngest of three people .
person1 = int(input("Enter the age of person one: "))
person2 = int(input("Enter the age of person two: "))
person3 = int(input("Enter the age of person three: "))
if(person1<person2 and person1<person3):
    print(f"{person1} is the youngest person.")
elif(person2<person1 and person2<person3):
    print(f"{person3} is the youngest person.")
elif(person3<person2 and person3<person1):
    print(f"{person3} is the youngest person.")
else:
    print(f"All Age's are equal.")
