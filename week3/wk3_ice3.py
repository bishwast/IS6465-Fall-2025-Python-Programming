"""
In Class Exercise 3
"""

"""
3.1 Adding a Custom Message in a Loop (4.5 points)
a. Create a list of five different car brands. Use a for loop to print each brand’s name in uppercase.
b. Modify your program to print a message for each brand.
Example: I would love to drive a {car}.
"""

car_brands = ["Mazda", "Tesla", "Lexus", "Honda", "Rivian"]
for cb in car_brands:
    print(cb)

# Empty list to store each messages.
message = []
for car in car_brands:
    message_updated = f"I would love to drive a {car}" # Creating message using the current car brand from the loop.
    message.append(message_updated)                    # Appending the variable msgx to the empty list — on each iteration.
    print(message_updated)                           # Printing each element from the new list of msg.

"""
3.2 Find the vowels – for loop (4.5 points)
Using the 'if' statement and the 'or' operator, write a program that uses the input() function and asks the user for a word or sentence.
Print the number of vowels in the string that’s returned from the input() function.
Use the 'or' operator inside the 'if' condition.
Pseudo code:
    Prompt user for a word or phrase.
    total = 0
    enter 'for' loop:
    for each letter, check if the letter is an 'a,e,i,o or u'. 
    If a match, then +1 to total.
    end loop.
    Print total results.
Reminder: Comparisons must be on both sides of the operator. i.e. c == 'e'. Cannot be: or 'a' or 'e'...
"""
user_input = input("Enter a word or phrase: ").lower()
# Initiating total vowel's count as 0
total_vowels = 0
# List to include each vowel from the loop.
your_vowels = []
for vowel in user_input:
    # Condition to check if user_input includes any vowels characters.
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        # If True, adding 1 to the total_vowels for each match.
        total_vowels += 1
        # For each vowel in a loop, appending each vowel found to the vowel list.
        your_vowels.append(vowel)
print(f"Your vowels are: {your_vowels}")
print("Total vowels: ", total_vowels)