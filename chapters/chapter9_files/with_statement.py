# f = open("file.txt")

# print(f.read())

# f.close()
# when u dont need moe code you can write 
# with the with statement

with open("file.txt" ) as f:
    print(f.read())
    # no need to close the file automatically close
    