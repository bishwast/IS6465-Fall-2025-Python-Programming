"""Homework 5
Course IS 6495-090 Fall 2025.
Student: Sunil Tiwari — u1275445"""

import random
""" Exercise #1: (5 points)
Write a program that generates the following pattern. Use functions to break up the problem into reusable blocks of code.
Code Example:
def topOrBottom():
    print ("#####")
Output:
#####
#     #
  # #
   #
  # #
#     #
#####

"""
def layer_1():
    print ("#####")
def layer_2():
    print("#   #")
def layer_3():
    print(" # # ")
def layer_4():
    print("  #  ")
layer_1()
layer_2()
layer_3()
layer_4()
layer_3()
layer_2()
layer_1()

"""Exercise #2: (5 points)
Write a function that converts a number from feet to inches (12 inches in a foot) 
and another function that converts feet to meters (0.3048 meters in a foot). 
Each function should accept a single argument and use that argument to calculate the conversion and print the result. 
Next, write a program that generates the following output - make sure to use your functions in your program!
0 ft:
... 0 inches
... 0 meters
1 ft:
... 12 inches
... 0.3048 meters
"""
print("\nUnits Conversion Program!")
# 12 inches = 1 foot
def conversion_ft_to_inches(feet):
    print (f"...{feet * 12} inches")

# 1 foot = 0.3048 meters
def conversion_ft_to_meters(feet):
    print (f"...{feet * 0.3048} meters")
# Range per requirement: 0 to 9
def get_conversions():
    for i in range(10):
        print(f"\n {i} ft:")
        conversion_ft_to_inches(i)
        conversion_ft_to_meters(i)
# Output
get_conversions()

"""Exercise #3: (5 points)
Write a function that rolls two dice. 
Your function should be designed to accept a single argument (an integer) and 
generate two die rolls between 1 and the number supplied. 
Your function should then return the two rolls in ascending order. 
Next, write a program that rolls 5 sets of dice with different sides. Here's a sample running of your program:
6 sided dice roll: 2 & 4
7 sided dice roll: 3 & 4
8 sided dice roll: 1 & 8
9 sided dice roll: 7 & 7
10 sided dice roll: 4 & 6"""
print("\nRoll 5 sets of dice!")
# Number representing two dice roll
def roll_dice(sides):
    roll_1 = random.randint(1, sides) # For first roll
    roll_2 = random.randint(1, sides) # For second roll
    # Logic to sort the rolls in ascending order.
    if roll_1 > roll_2:
        roll_1, roll_2 = roll_2, roll_1 # Small Number to Greater than small number., Swapping values at the sametime.
    return roll_1, roll_2

# Per question's requirement there is upto 10 sided dice.
# To roll exactly 5 sets of dice with different sides (6,7,8,9,10)
rolls = []  # Empty list to store each rolls
for sides in range(6, 11):
    roll_1, roll_2= roll_dice(sides)
    rolls.append((sides, roll_1, roll_2))   # Storing items as a tuple.
# Output
for sides, roll_1, roll_2 in rolls:
    print(f"{sides} sided dice roll: {roll_1} & {roll_2} ")

# # Extra feature for users custom rolls.
# # Note: Self Added feature if i have to ask user's input
# def get_users_input_sides():
#     while True:
#         sides = input("Enter number of sides for a dice roll (1-10): ")
#         if sides.isdigit():
#             sides = int(sides)
#             if 1 <= sides <= 10:
#                 return sides
#             else:
#                 print("Invalid sides entered. Please choose a number between 1 and 10.")
#         else:
#             print("Invalid sides entered. Try again.")
# users_roll_sides = get_users_input_sides()
# roll_1, roll_2 = roll_dice(users_roll_sides)
# print(f"{users_roll_sides} sided dice roll: {roll_1} & {roll_2} ")

"""Exercise #4: (5 points)
Guess the number
Prompt the user to guess a number. Check in input from the user against the secret number that was randomly generated. 
Limit the guesses to 6 chances. If the user correctly guesses, then print 
    "Good job! You guessed my number in x guesses!" 
Else, if they failed to guess correctly, print 
    "Nope. The number I was thinking of was x".

Use the following code to get you started:

# This is a guess the number game.
import random
# use the random.randint() function to generate a random number between 1 and 20.
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

guess = 0
guesses = 0
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
...

Sample output:

I am thinking of a number between 1 and 20.
Take a guess.
4
Your guess is too low.
Take a guess.
18
Your guess is too high.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Good job! You guessed my number in 4 guesses!"""
print("\nNumber Guessing Game!")
def get_guessed_number():
    secretNumber = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    guess = 0
    guesses = 0
    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        user_input = input("Take a guess: ")
        if user_input.isdigit():
            guess = int(user_input)
            if guess < secretNumber:
                print("Your guess is too low.")
            elif guess > secretNumber:
                print("Your guess is too high.")
            else:
                print(f"Good job! You guessed my number in {guessesTaken} guesses!")
                break
        else:
            print(f"Please try again.")
    else:
        print(f"Nope. The number I was thinking of was {secretNumber}.")
get_guessed_number()





