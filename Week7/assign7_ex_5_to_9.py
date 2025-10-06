"""Exercise 5 TO 8"""

"""Exercise #5: (5 points)
Write a Python class to reverse a string word by word."""

print("Exercise #5")
class String_Reverse:

    def __init__(self, user_input):
        self.user_input = user_input

    def get_reversed_word_by_word(self):
        words = self.user_input.split()
        reversed_words = words[::-1]
        return reversed_words
user_input = input("Enter a sentence and see it's reverse: ")
ui = String_Reverse(user_input)
print(f"Reversed List:{ui.get_reversed_word_by_word()}")
# Proper format eliminating "," with spaces using .join() method.
print(f"Reversed String: {" ".join(ui.get_reversed_word_by_word())}")

"""Exercise #6: (5 points)
Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle.
    Area Formula: radius squared * pi (r2 * 3.14)
    Perimeter Formula: 2*radius*pi"""

print("\nExercise #6")
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        area = math.pi * (self.radius**2)
        return area

    def get_perimeter_circle(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter
user_input1 = float(input("Enter a radius of a Circle: "))
c1 = Circle(user_input1)
print(f"\tArea of a Circle of radius {user_input1}: {c1.get_area_circle():.2f}")
print(f"\tPerimeter of a Circle of radius {user_input1}: {c1.get_perimeter_circle():.2f}")


"""Exercise #7: (5 points)
Write a Python class named Rectangle constructed by a length and width 
and a method which will compute the area of a rectangle.
Formula: Length * Width"""

print("\nExercise #7")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def __str__(self):
        # String formatted with values related to the specifically defined Instance.
        return (f"Area of a Rectangle with length: {self.length} and Width: {self.width} is {self.get_area()}!.")

r = Rectangle(5, 5)     # Instance
print(r)    # Invoking __str__() method to display the strings.

"""Exercise #8: (5 points)
Create a Line class using the class skeleton below. Fill in the code needed for each function.
(Hint: coor1, coor2 are tuples)

class Line:

    def __init__(self, coor1, coor2):
        pass

    def distance(self):
        pass

    def slope(self):
        pass

Sample output:

    coordinate1 = (3,2)
    coordinate2 = (8,10)

    li = Line(coordinate1, coordinate2)
    print(li.distance())
    9.433981132056603

    print(li.slope())
    1.6
"""
print("\nExercise #8")
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1  # First Coordinate
        self.coor2 = coor2  # Second Coordinate

    def distance(self):
        """Pythagorean theorem — Distance between two points is square root of (( x2 - x1)^2 - (y2 - y1)^2)"""
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   # From module math.sqrt()
        return dist

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        if x2-x1 == 0:
            return "Slope is undefined for vertical lines."
        else:
            slope = (y2-y1)/(x2-x1)
            return slope

coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(f"Distance between {coordinate1} and {coordinate2} is {li.distance():.2f}.")
print(f"Slope between {coordinate1} and {coordinate2} is {li.slope():.2f}.")

"""Exercise #9: (5 points)
Step 1:
Write a function named collatz() that has one parameter named number.
    If number is even, then collatz() should print number // 2 and return this value.
    If number is odd, then collatz() should print and return 3 * number + 1.

Step 2:
Write a program that lets the user type in an integer
and that keeps calling collatz() on that number until the function returns the value 1.

Amazingly enough, this sequence actually works for any integer—sooner or later,
using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.

Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
"""

print("\nExercise #9")
def collatz(number):
    # If Even
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # If Odd
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Checking for an Integer.
while True:
    try:
        n = int(input("Give me a number: "))
        break # if n is a valid integer.
    except ValueError as ve:
        print(f"Error Details: {ve}\n That's not a number.")
# Continuously calling collatz() function until the number becomes 1
while n != 1:
    n = collatz(n)