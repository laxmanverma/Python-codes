"""
Static methods are methods within a class that have no access to anything else in the class (no self keyword or cls keyword). They cannot change or look at any object attributes or call other methods within the class.
They can be thought of as a special kind of function that sits inside of the class.
When we create a static method we must use something called a decorator.
The decorator for a static method is "@staticmethod".
"""
class MyStaticMethodClass:
    def __init__(self):
        self.x = x

    @staticmethod
    def static_method():
        return "i am a static method"

# Notice staticMethod does not require the self parameter


"""
Class methods are methods within a class that only have access to class variables and other class methods.
They are passed the name of the class and therefore can access anything within the class. 
Like static methods they cannot access any instance attributes. 
You can create a class method by using the "@classmethod" decorator.
"""
class MyClass:
    count = 0

    def __init__(self):
        self.x = x

    @classmethod
    def classMethod(cls):
        cls.count += 1
# The classMethod can access and modify class variables. It takes the class name as a required parameter