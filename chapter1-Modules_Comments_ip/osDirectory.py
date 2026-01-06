import os
# specify the directory you wnat to list
# here in quote specify the file name ex:'/Users/sanab/oneDrive/Desktop/python_learning'
directory_path ='/'
# list all the files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)

