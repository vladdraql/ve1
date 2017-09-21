# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.name = 'Dacia'
car1.color = 'Red'
car1.value = 25.000

car2.name = 'Bemveu'
car2.color = 'Hauriu'
# test code
print(car1.description())
print(car2.description())