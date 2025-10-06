"""2.3. Cylinder: (5 points)
Create a Cylinder class using the class skeleton below.
Fill in the code needed for each function.

class Cylinder:

    def set_height_radius(self, height, radious):
        pass

    def volume(self):
        pass

    def surface_area(self):
        pass

Sample output should look like this:

mycyl = Cylinder()
mycyl.set_height_radius(2,3)
print(mycyl.volume())
56.52
print(mycyl.surface_area())
94.2
Volume formula:

height * pi(radius)^2

Surface area formula: top = pi * radius^2

2*top + (2*pi*radius*height)"""

import math
class Cylinder:
    # Volume of a cylinder: pi*r^2*height
    def set_height_radius(self, height, radius):
        # Setting height and radius
        self.height = height
        self.radius = radius

    def volume(self):
        volume = math.pi * (self.radius ** 2) * self.height
        return volume
    # Surface Area = (2*3.14*r^2) + (2*3.14*r*h)
    def surface_area(self):
        s_area = (2*math.pi * self.radius ** 2) + (2*math.pi * self.radius * self.height)
        return s_area

# Instance of class - Cylinder
mycyl = Cylinder()
# Calling methods
mycyl.set_height_radius(2,3)
# Printing results
print(f"Volume of a Cylinder: {mycyl.volume():.2f}")
# 56.52
print(f"Surface Area of a Cylinder: {mycyl.surface_area():.2f}")
# 94.2