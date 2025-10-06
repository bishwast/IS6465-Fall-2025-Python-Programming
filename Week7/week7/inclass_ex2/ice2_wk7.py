"""2.1. The simplest class: (5 points)
We will start with the simplest class you could ever write in Python.
Create a class called Simplest() and use the pass statement.

Answer the following questions:
a. Using the code below, what type is this object?
    print(type(Simplest))
b. Create an instance of Simplest to a variable called simp. What type is simp?"""

class Simplest():
    pass
print(f"Type: {type(Simplest)}")
simp = Simplest()
print(f"Type: {type(simp)}")    # simp is an instance of class - Simplest

"""2.2. Person Class: (5 points)
Create a new class called Person. 
Add 3 attributes (or fields) called first_name, middle and last_name.
Add a function called format_name() and return all 3 attributes.
(Hint: Use the same function we wrote in week 6).
Create a new instance of the Person class, 
set the attribute fields and 
then call the format_name() function using print().
"""
class Person():
    # 3 attributes
    first_name = ""
    middle = ""
    last_name = ""

    # Add a function called format_name() and return all 3 attributes.
    def format_name(self):
        return f"Full Name: {self.first_name} {self.middle} {self.last_name}"

# Instance of class - Person
person = Person()
# Setting Attributes
person.first_name = "Sunil"
person.middle = "Tiwari"
person.last_name = "Bishwakarma"
# Calling the function with print
full_name = person.format_name()
print(full_name)







