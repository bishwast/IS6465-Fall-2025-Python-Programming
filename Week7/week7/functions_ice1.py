"""Week 7: In-class exercise 1 - Import Functions"""
"""1.1. Import functions: (5 points)
Write a new function in your functions file (as noted above). 
Create 2 functions; 
    one to convert a value from Fahrenheit to celsius and 
    the second function to convert from celsius to Fahrenheit
        Note: remember to return the values in the function statement.

Create a new python file called ICE1.py. Using Import, import your new functions script in the ICE.py script.
Using the print() function, test and invoke the celsius and Fahrenheit functions."""

# Functions 1: Convert a value from Fahrenheit to Celsius. C = (5/9)*(F-32)
def convert_fahrenheit_to_celsius(val_fahrenheit):
    val_celsius = float((5/9)*(val_fahrenheit-32))
    return val_celsius

# Function 2: Convert from Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(val_celsius):
    val_fahrenheit = float(((9/5) * val_celsius)+32)
    return val_fahrenheit

"""
Function 3: NullToBooleanConverter(). 
If null (None), return false, otherwise return true. 
(Hint: this can be done with one line of code using comparison operators)"""
def NullToBooleanConverter(val):
    return val != None  # True, IF NOT None, returns False

"""Function 4: getAnswer(), that takes one numerical argument called answerNumber"""
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
