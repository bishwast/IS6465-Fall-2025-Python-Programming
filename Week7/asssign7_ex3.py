"""Exercise #3: (5 points)
Create a new class called Square.
Implement a constructor that takes a "side" parameter
and initialize it to a class member called "side".
Add a function in the class called area().
    The area() function will return the side^2.
Create an instance of the class and invoke the area() function to test it.
Set the instance variable "side" to a different value and invoke area() again.
"""
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        side = self.side**2
        return side
    def __str__(self):
        return str(self.side)   # Helps  sides for each Instance.

print("Exercise #3")
square = Square(5)
sq1 = Square(5)
area1 = sq1.area()
print(f"Area of a quare of {sq1} sides is {area1}")

# Set the instance variable "side" to a different value and invoke area() again.
sq1.side = 9
area2 = sq1.area()
print(f"Area of a square of {sq1} sides is {area2}")


