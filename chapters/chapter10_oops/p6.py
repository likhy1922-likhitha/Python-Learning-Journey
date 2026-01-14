'''
Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.
'''
class Demo:
    def studentdetails(slf,name,rollno):
        slf.name = name
        slf.rollno = rollno
    def coursedetails(likhitha,course,fee):
        likhitha.course = course
        likhitha.fee = fee
 

s1 = Demo()
s1.studentdetails("likhitha",11)
s1.coursedetails("cse",4000000)
print(s1.name)
print(s1.course)
