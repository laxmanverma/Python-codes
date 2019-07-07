class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")

    def add_speed(self, speed):
        self.speed = speed

    def display(self):
        print(self.speed)


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # This will call the Animal classes constructor method

    def speak(self):
        print("I am a Dog")


lxn = Dog("tiger", 5)
lxn.speak()  # This will print "I am a Dog"

animal = Animal("lion", 7)
animal.speak()
animal.add_speed(50)
animal.display()
#lxn.display()  gives error 'Dog' object has no attribute 'speed'
lxn.add_speed(70)
lxn.display()
