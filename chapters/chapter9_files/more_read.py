# f = open("file.txt","r")
# # lines = f.readlines()# it return the one list

# # print(lines,type(lines))

# line1 = f.readline()#prints  first line in the file.txt
# print(line1,type(line1))

# line2 = f.readline()#prints second line  in the file.txt
# print(line2,type(line2))

# line3 = f.readline()# prints line three in the file.txt
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))# if line is not present  it will 
# #wont count it so that output is nothing for line 4 

# f.close()

f = open("file.txt", "r")

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()

