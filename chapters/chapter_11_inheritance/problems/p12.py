'''
Answer these in your own words:

Why can a child object access parent methods?
Ans:Because the child class inherits from the parent class, it automatically gets all the parent’s methods and attributes. So a child object can use them as if they were its own.

When do we override a method?
Ans:We override a method when we want the child class to have a different behavior than the parent’s method, even if the method name is the same.

Why does Python need super()?
Ans:Python uses super() to call the parent’s method (often __init__) from the child, so we can keep the parent’s behavior while adding or changing things in the child.

What happens if parent and child have same method name?
Ans: The child’s method overrides the parent’s method. Python will run the child’s version when called from a child object.

When should we avoid inheritance?
Ans:Avoid inheritance when the classes are not logically related, or when you just want to reuse code. In those cases, use composition instead (having objects inside other objects instead of inheriting).
'''