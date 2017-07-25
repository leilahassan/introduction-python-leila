import math
class Circle():
    def __init__(self,radius):
        self.radius = int(radius)
    
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return 2 * math.pi* self.radius
        
radius = input("What is the radius of your circle?:")
object = Circle(radius)
print("The area of the circle is {} and its perimeter {}".format(object.area(),object.perimeter()))