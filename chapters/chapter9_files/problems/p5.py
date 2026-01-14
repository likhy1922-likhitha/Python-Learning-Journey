'''
5. Repeat program 4 for a list of such words to be censored.
'''

words = ["donkey", "dog", "cat", "horse", "monkey"]

with open("main2.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("main2.txt", "w") as f:
    f.write(content)
