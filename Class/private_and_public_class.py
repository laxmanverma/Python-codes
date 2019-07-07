"""
Private and Public
In other programming languages there is the notion of private and public classes and methods.
A private class is something that can only be accessed from within a certain file or directory and a private method is something that can only be called from within the class.
A public class or method is something that can be accessed anywhere.

However, In python this does not exist. Every class and method in python is public and there is no way to change that. We can only simulate creating private classes and methods by using certain notation and conventions.

To declare something as private we use one underscore before the name.
"""

class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)  # Even though we decalre something private we can still call and us it

    def _dispaly(self):  # Private
        print("Hello")

    def display(self):  # Public
        print("Hi")