#A basic class consists only of the class keyword, the name of the class, and the class from which 
#the new class inherits in parentheses.
#here it will inherit from the object class
# Class definition
class animal(object):
    # For initializing our instance objects
    """__init__(). This function is required for classes, and it's used
    to initialize the objects it creates. __init__() always takes
    at least one argument, self, that refers to the object being created."""
    def __init__(self, name, age,is_hungry):
        self.name = name
        self.age = age
        self.is_hungry=is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = animal("Jeffrey", 2, True)
giraffe = animal("Bruce", 1, False)
panda = animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
