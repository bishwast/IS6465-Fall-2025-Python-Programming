"""Exercise 3 - Classes & Constructors"""

"""3.1. NumberSet Class (5 points)
Create a class called NumberSet that accepts 2 integers as input, 
and defines two instance variables: num1 and num2, which hold each of the input integers. 
Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. 
Save this instance to a variable t."""

class NumberSet:
    """Constructor with Parameters — Initialing the instance variables num1 and num2. """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Creating an Instance (or an Object "t") — The arguments num1=6 and num2=10 are passed to match the constructor parameters.
t = NumberSet(6, 10)
# Printing
print("Exercise 3.1")
print(f"Instances\n num1: {t.num1}\n num2: {t.num2} ")

"""3.2. Animal Class (5 points)
Create a class called Animal that accepts two numbers as inputs 
and assigns them respectively to two instance variables: arms and legs. 
Create an instance method called limbs that, when called, returns the total number of limbs the animal has. 
To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. 
Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
"""

class Animal:

    def __init__(self, arms, legs):
        """Initialize an animal with arms and legs. """
        self. arms = arms
        self.legs = legs

    # Instance method called get_arms_legs (arms + legs) that, when called, returns the total number of limbs the animal has.
    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

    def limbs(self):
        total_limbs = self.get_legs() + self.get_arms()
        return total_limbs

# To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs — in order as in the constructor.
spider = Animal(4, 4)
# Call the limbs method on the spider instance and save the result to the variable name spidlimbs
spidlimbs = spider.limbs()
print("\nExercise 3.2")
print(f"Spider has {spidlimbs} limbs")

"""3.3. Cereal Class (5 points)
Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, 
and assigns them to 3 instance variables in the constructor: name, brand, and fiber. 
When an instance of Cereal is printed, the user should see the following: 
“[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!”

To the variable name c1, assign an instance of Cereal 
    whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2.

To the variable name c2, assign an instance of Cereal 
    whose name is "Honey Nut Cheerios", brand is "General Mills", and fiber is 3.

Practice printing both!"""

class Cereal:
    pass
    """Accepts three inputs: 2 strings and 1 integer. """
    def __init__(self, name, brand, fiber):
        """Constructor — Initializing the instance variables name, brand, and fiber. """
        self.name = name
        self.brand = brand
        self.fiber = fiber

    # Second Approach to this problem — Using __str__() method to control printing of the instances at once — Override
    def __str__(self):
        """Returning a string representation of the object attributes. """
        return(f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!")

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

# Implementing __str__() override.
print("\nMy Second Approach for Exercise 3.3")
print(c1)
print(c2)

# Manual formatting.
print("\nMy First Approach for Exercise 3.3")
print(f"{c1.name} cereal is produced by {c1.brand} and has {c1.fiber} grams of fiber in every serving!")
print(f"{c2.name} cereal is produced by {c2.brand} and has {c2.fiber} grams of fiber in every serving!")


