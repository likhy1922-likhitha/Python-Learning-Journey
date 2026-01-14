'''
Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?

'''
class Demo:
    a = 4
main = Demo()
print(main.a)
main.a = 10
print(main.a)
#but it doesnt change the class attribute
print(Demo.a)
