"""
Code Along 3
Obj: For Loop
"""
apples = "apples"
for i in apples:
    print(i)

fruit = "oranges"
for letter in fruit:
    print(letter)
print("Loop is done")
print(fruit)

# Range Function — range()
total = 0
for i in range(1000):
    total += i
print("Sum of all numbers from 0 to 1000: ", total)

# List of strings
characters = ["Batman", "Superman", "Aquaman", "Green Lantern", "Wonder Women"]
for item in characters:
    print(item)

characters.append("Flash")
print(characters)
