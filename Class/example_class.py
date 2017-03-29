#
class Car(object):
    condition="new"
    def __init__(self,model,color,mpg):
        self.model=model
        self.color=color
        self.mpg=mpg

my_car=Car("DeLorean", "silver", 88)
print(my_car.condition)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)

"""
Each class object we create has its own set of member variables.
Since we've created an object my_car that is an instance of the Car class,
my_car should already have a member variable named condition.
This attribute gets assigned a value as soon as my_car is created.


There is a special function named __init__() that gets called whenever
we create a new instance of a class. It exists by default, even though
we don't see it. However, we can define our own __init__() function
inside the class, overwriting the default version. We might want to do
this in order to provide more input variables, just like we would with
any other function.

The first argument passed to __init__() must always be the keyword
self - this is how the object keeps track of itself internally - but we
can pass additional variables after that
"""
