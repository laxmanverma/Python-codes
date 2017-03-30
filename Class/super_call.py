#You can directly access the attributes or methods of a superclass
#with Python's built-in super call.
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours=hours
        return hours*12.00
    def full_time_wage(self,hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)
    #here in derived PartTimeEmployee class we have overwritten the calculate_wage
    #method but we want to use the method of base(or super or parent) class we can
    #do this by using a super call whose syntax is
    """
        super(Derived class name, self).method_name(arguments)
                                                              """
milton=PartTimeEmployee("Laxman")
print(milton)
b=milton.calculate_wage(20)
print(b)
a=milton.full_time_wage(10)
print(a)
