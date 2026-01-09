# Print all vowels in the word "education"
word = "education"
for i in range(0,len(word)):
    if((word[i]=="a" )or(word[i]== "e") or (word[i]=="i") or (word[i]=="o") or (word[i]=="u")):
        print(word[i])
print("next one...........")
   
# or youcan us ethis for less code
word1 ="Engineering"
vowels="aeiou"
for i in range(0,len(word1)):
    if word1[i] in vowels:
        print(word1[i])