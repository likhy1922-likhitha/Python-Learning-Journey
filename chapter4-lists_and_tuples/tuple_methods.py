a = (1,3,7,7,2)
print(a)
print(type(a))
s = a.count(7)# counts the specified value occurences
print(s)
d = a.index(7)# return the index of the specified value
print(d)
b = ("likhitha","Seetha","venkatesh","siddu",12,14,4)
concatination= a+b# concating
print(concatination)
repitation=a*2#repeating
print(repitation)
slicing = a[1:4]#slicing
print(slicing)
# unpacking tuple into separte variables
u,y,t,r,e = a
print(u,y,t,r,e)
print(len(a))#length of a tuple
print(2 in a)# checking whether the sepcified value exists or not 
# this method is called membership: returns the boolean value
