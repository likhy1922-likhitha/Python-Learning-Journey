'''
1
23
456
78910
'''
num=0
for i in range(1,5):
    for j in range(1,i+1):
        num =num+1
        print(num,end="")
    print()
