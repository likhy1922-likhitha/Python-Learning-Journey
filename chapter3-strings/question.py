Name = "Likhitha"
Date = "10\\11\\2025"
letter = '''
Dear <|Name|>,
    You are selected!
    <|Date>

'''
print(letter.replace("<|Name|>",Name).replace("<|Date>",Date))
# it is called chaining
#finding the double space if -1 then the  no double space
name = "likhy is a good   girl"
print(name.find("  "))
print(name)
print(name.replace("  "," "))
# letter formating
Letter = "Dear Likhitha ,\n\tThis python course is nice.\n\t\tThanks!"
print(Letter)