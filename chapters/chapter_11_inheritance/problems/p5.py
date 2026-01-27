'''
Parent class: Shape
Method: draw() → prints "Drawing shape"

Child class: Circle
Override draw() → prints "Drawing circle"

Call draw() using Circle object.

Question to think:
Which method runs — parent or child?
'''
class Shape:
    def draw(self):
        print("Drawing the shape.")
# child class
class Circle(Shape):
    def draw(self):
        print("drawing the circle.")
# calling the draw
c = Circle()
c.draw()