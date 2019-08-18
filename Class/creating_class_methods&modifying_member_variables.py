class Car(object):
    condition = "new"   #class variables
    def __init__(self, model, color, mpg):
        self.model = model  #Instance variables
        self.color = color  #Instance variables
        self.mpg   = mpg    #Instance variables
        
    def display_car(self):
        return "This is a "+ self.color+" "+self.model+" with " +str(self.mpg)+" MPG."

    def drive_car(self):
        self.condition="used"
        
my_car = Car("DeLorean", "silver", 88)
print(my_car.display_car())

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)
