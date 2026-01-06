s = {1,4,2,2,6,8,"Likhitha","Shreya","Shreya"}
print(s,type(s))
s.add(98)
print(s)
print(len(s))
s.remove(2)
# s.clear()
s.copy()

print(s)
s1 ={1,2,0,9,8,4,6}
s2={4,1,2,7,0,9,8,4,3,2}
s3 =s1.difference(s2)
print(s3)
s4=s1.difference_update(s2)
print(s4)
s5 =s1.union(s2)#all elements
print(s5)
s6 = s2.intersection(s1)
print(s6)
print(s.pop())# removes random element from the set
print(s)

set1 ={1,2,4,6}
set2={2,9,8,7,5}
print(set1.intersection(set2))
#subset
print({1,2}.issubset(set1))
print(set1.issuperset({1,2}))
