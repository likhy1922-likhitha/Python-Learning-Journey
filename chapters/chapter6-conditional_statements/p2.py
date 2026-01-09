# write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each 
# subject to pass .Assume 3 subjects and takes marks as an input from the Use
sub1 = int(input("Enter the marks of sub1: "))
sub2 = int(input("Enter the marks of sub2: "))
sub3 = int(input("Enter the marks of sub3: "))
total_precentage = (100*(sub1+sub2+sub3))/300

if(total_precentage>= 40 and sub1>=33 and sub2>=33 and sub3>=33):
    print(f"Pass:{total_precentage}")

else:
    print("Fail")




