"""
In Class Exercise 2
Obj: List Methods
"""

"""
2.1. Shapes (5 points)
Create a list called shapes and set: shapes = ['rectangle', 'circle'].
Use append and add a triangle and print the list.
Use insert and insert "square" and print the list.
Remove the rectangle item and print.
Use del on element two and print.
"""

shapes = ["rectangle", "circle"]
shapes.append("triangle")
print(shapes)
shapes.insert(2, "square")
print(shapes)
shapes.remove("rectangle")
print(shapes)
del(shapes[2])
print(shapes)

"""
2.2. Sorting (5 points)
Using the sort function, sort this list in numerical order and print it:
    ages = [27, 60, 14, 35, 3, 76]
Sort the following list in alphabetical order:
    names = ['Quinn', 'John', 'Amber', 'Kim']
Sort the following list in numerical order and print:
    stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
"""
ages = [27, 60, 14, 35, 3, 76]
ages.sort()     # ascending
print(f"\nAscending: {ages}")
ages.sort(reverse=True)     # descending
print(f"\nDescending: {ages}")

names = ['Quinn', 'John', 'Amber', 'Kim']
names.sort()    # A to Z order
print(f"\nA to Z order: {names}")
names.sort(reverse=True)
print(f"\nZ to A order: {names}")    # Z to A order

stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
stats.sort()    # ascending
print(f"\nAscending: {stats}")
stats.sort(reverse=True)    # descending
print(f"\nDescending: {stats}")

"""2.3. Min-Max (5 points)
Create a list of numbers from 1 to 20 using range(), then use min(), max(), and sum() functions. 
Print out the results for each function."""
nums = []
for i in range(1,21):
    nums.append(i)
print(f"\nList of numbers from 1 to 20: {nums}")

print(f"Minimum number in list {nums} is ",min(nums))
print(f"Maximum number in list {nums} is ",max(nums))
print(f"Sum of all numbers in list {nums} is ",sum(nums))