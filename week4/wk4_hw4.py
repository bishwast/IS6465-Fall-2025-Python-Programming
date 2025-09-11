"""
Course: IS 6465, Fall 2025
Homework 4
"""

"""Exercise #1: (10 points)
Fantasy Game Inventory.
You are creating a fantasy video game. The data structure to model the player’s inventory will 
be a dictionary where the keys are string values describing the item in the inventory and the 
value is an integer value detailing how many of that item the player has. 
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
means the player has 1 rope, 6 torches, 42 gold coins, and so on. 
Write a 'for loop' and print out the players inventory. 
The output should be as below:

Inventory:
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
3 map fragments
Total number of items : 65

Hint: You can use a 'for loop' to loop through all the keys in a dictionary. Use the dictionary below:
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments': 3}"""

stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12,
    'map fragments': 3
}
print(type(stuff))
print("Inventory:")
total = 0
for key, value in stuff.items():
    print(value, key)
    total += value
print(f"Total number of items: {total}")

"""Exercise #2: (10 points)
Comma Code.
Say you have a list value like this:
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
Write Python code that coverts the list into a string with all the items separated by a comma and a space, 
with 'and' inserted before the last item. 
For example, converting the characters list look like this:
    'Thor, Thanos, Black Panther, Iron Man, Hulk, Batman and Captain America.' """

print("\nComma Code:")
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
# Variable to store the final string of characters.
new_characters = ""
# using the length of the characters in the list as a form to estimate the range and iterating through every characters.
for c in range(len(characters)):
    # Starting at index of 0, then adding each character to the new variable.
    if c == 0:
        new_characters += characters[c]
    # Inserting "and" before the last character and a period. `
    elif c == len(characters) - 1:
        new_characters += " and " + characters[c] + "."
    # Adding comma and space before all other characters.
    else:
        new_characters += ", " + characters[c]
print(new_characters)
# Adding quotes at beginning and at the end of the list of character strings to match the requirements.
final_strings_of_characters1 = "'" + new_characters + "'"
print(final_strings_of_characters1)
print(type(final_strings_of_characters1))

"""Exercise #3: (10 points)
Create a dictionary of technical terms and allow the user to lookup the definitions of these terms from the dictionary. 
Use the following list for your dictionary:
'dict', 'list', 'map', or 'set'

You can use the following resource:
dict = “stores a key/value pair”
list = “stores a value at each index”
map = “see dict”
set = “stores unordered unique elements” 

Based on the user's input, print the term and the definition.
Make “exit” a term in the dictionary. Prompt the user to enter a term inside a while loop until the user types the word “exit”."""

tech_terms = {
    "dict": "stores a key/value pair",
    "list": "stores a value at each index",
    "map": "see dict",
    "set": "stores unordered unique elements",
    "exit": "terminates the program"
}
print(f"\nLook up the definitions of technical terms below to know their definitions!")
for k in tech_terms:
    print(f"— {k}")
while True:
    user_input_3 = input("Please enter technical terms you would like to look up (or exit to quit): ").lower()
    if user_input_3 == "exit":
        print(f"\nYou entered {user_input_3} which {tech_terms[user_input_3]}.")
        break
    if user_input_3 == "dict" or user_input_3 == "dictionary":
        print(f"Definition of \"{user_input_3}\" is {tech_terms['dict']}.")
    elif user_input_3 == "list":
        print(f"Definition of \"{user_input_3}\" is {tech_terms[user_input_3]}.")
    elif user_input_3 == "map":
        print(f"Definition of \"{user_input_3}\" is {tech_terms[user_input_3]}.")
    elif user_input_3 == "set":
        print(f"Definition of \"{user_input_3}\" is {tech_terms[user_input_3]}.")
    else:
        print("Please enter a valid input.")
print("Goodbye!")

"""Exercise #4: (2 points)
Write an expression that would turn the string "Mississippi" into a set of unique letters.
For example:
set("Parallel") would return set {"P", "a", "e", "l", "r"}
You should only write one line of code for this. Do not assign a variable name to the set.
Hint: use the set() data type."""
print("\nExercise #4")
print(set("Mississippi"))   # {'M', 'p', 'i', 's'}

"""Exercise #5: (2 points)
Reassign "hello" in this nested list to say "goodbye" instead:
list1 = [1, 2, [3, 4, "hello"]]"""
print("\nExercise #5")
list1 = [1, 2, [3, 4, "hello"]]
# From Second list in list1 to its index[2]—third element, assigning the value to "goodbye"
list1[2][2] = "goodbye"
print(list1)

"""
Exercise #6: (3 points)
Using keys and indexing, grab the "hello" from the following dictionaries:
6a.
d = {'simple_key':"hello"}
6b.
d = {"k1":{"k2":"hello"}}"""
print("\nExercise #6")
# 6a
d = {'simple_key':"hello"}
print(f"6a: ", d['simple_key'])
# 6b
d = {"k1":{"k2":"hello"}}
# From first key [k1] accessing the value of the key [k2]
print(f"6b: ", d['k1']['k2'])
