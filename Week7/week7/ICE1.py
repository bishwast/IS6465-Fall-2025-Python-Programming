"""Using Import,
Import your new functions script in the ICE1.py script.
Using the print() function, test and invoke the Celsius and Fahrenheit functions."""

import functions_ice1 as func_i1
import random

from week7.functions_ice1 import getAnswer
print("Import Functions")
val_celsius = 100
val_fahrenheit = 75
# Fahrenheit to Celsius
vc = func_i1.convert_fahrenheit_to_celsius(val_fahrenheit)
print(f"{val_fahrenheit} Fahrenheit is {vc:.2f} Celsius.")
# Celsius to Fahrenheit
vf = func_i1.convert_celsius_to_fahrenheit(val_celsius)
print(f"{val_celsius} Celsius is {vf:.2f} Fahrenheit.")


"""1.2. NullToBooleanConverter: (5 points)
Create a new function in your functions.py script called NullToBooleanConverter(). 
If null (None), return false, otherwise return true. (Hint: this can be done with one line of code using comparison operators)
In the ICE1.py file and using the print() function, test and invoke the function using a non-null variable and a variable that is null."""
print("\nNullToBooleanConverter")
val_null = None # No Value
print("Null: ", func_i1.NullToBooleanConverter(val_null))

"""1.3. Magic 8-Ball: (5 points)
Create a new function in your functions.py script called getAnswer() that takes one numerical argument called answerNumber.
use the following code inside the new getAnswer() function:

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
In the ICE1.py script, use the random generator and generate a number between 1 and 9. Pass the number into the getAnswer() function and print out the users fortune."""

print("\nMagic 8-Ball")
for n in range(1,10):
    answerNumber = random.randint(1,9)
    print(f"Fortune for {answerNumber}: {func_i1.getAnswer(answerNumber)}")
