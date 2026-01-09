# write a program to find out whether a given name is present in a list or not 
list = ["Hasini","Akshaya","Deepika","Geetha","Swarna","Thanuja","Bhagya","Likhitha","Harini","Anjani","Akash","Ruthwik","Vishnu","Shiva","Venkatesh","Badulla","Veeresh","Aravind"]
list.sort()

print(list)
name = input("Enter the name: ")
if(name in list):
    print(f"{name} is in the list")
else:
    print(f"{name} is not in the list")