# 1.write a program to create a dictionary of telugu words with the value as their in english translation .provide user with an option to look it up
# words={
#     "bagunara":"Are you good!",
#     "illu":"house",
#     "mancham":"bed",
#     "kooni":"Few"
# }
# word=input("Enter the word you want to know the meaning: ")
# print(words[word])

# 2. write a program to input eight numbers from the user and display all the unique numbers (once) (using set)
# set = set()

# n1 = int(input("Enter the number1:"))
# set.add(n1)
# n2 = int(input("Enter the number2:"))
# set.add(n2)
# n3 = int(input("Enter the number3:"))
# set.add(n3)
# n4 = int(input("Enter the number4:"))
# set.add(n4)
# n5 = int(input("Enter the number5:"))
# set.add(n5)
# n6 = int(input("Enter the number6:"))
# set.add(n6)
# n7 = int(input("Enter the number7:"))
# set.add(n7)
# n8 = int(input("Enter the number8:"))
# set.add(n8)
# print(set)


# 3.can we have the set with 18(int) and "18"(str)  as a value in it?
# set1={18,"18"}
# print(set1)

# 4.create a empty dictionary.Allow 4 friends to enter their favorite language as value and use key as their names.Assume that the names are unique
# dic={}
# name = input("Enter your name: ")
# lang = input("Enter the language:")
# dic.update({name:lang})

# name = input("Enter your name: ")
# lang = input("Enter the language:")
# dic.update({name:lang})

# name = input("Enter your name: ")
# lang = input("Enter the language:")
# dic.update({name:lang})

# name = input("Enter your name: ")
# lang = input("Enter the language:")
# dic.update({name:lang})
# print(dic)

# 5.if the names of 2 friends are same what will  happen to the program in problem4

# 6.if the language of 2 friends are same what will happen to the program in problem4

# 7.can you change the value inside a list which contained in set s={8,7,12,"Harika",[1,2]}
s={8,7,12,"Harika",[1,2]}# we cannot write the list inside the set because python 
# requires all their elements to be immuatble and hassable.lists are mutable and not hasable so they cannot added in a set


print(s)
