'''
Write a program to find out whether a file is identical & matches the content of
another file.
'''
with open("file.txt") as f:
    content = f.read()
with open("poems.txt","r")as f:
     conetnt2= f.read()
if(content==conetnt2):
     print("All the content matches with the file")
else:
     print("all content is not identical")