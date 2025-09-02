"""
Code Along 1
Obj: Intro to data structures — Basic Lists
"""
empty_list = list()

my_list = [95, 3.2, "Marvel", 17, -4]
print(my_list)
print(my_list[2])

second_list = [100, 101]
print("Second List: ", second_list)
second_list = second_list * 2   # instead of product, the *2 multiplies the list — [100, 101, 100, 101]
print(second_list)

big_list = my_list + second_list    # concatenation of line 15 and line 9
print(big_list)

characters = ["Iron Man", "Ant Man", "Thor", "Loki", "Black Panther", "Black Widow"]
print(characters)
print(len(characters))
print(characters[2])   # Thor
print(characters[1:3]) # Ant Man, Thor
print(characters[1:5]) # "Ant Man", "Thor", "Loki", "Black Panther"
print(characters[-3:]) # "Iron Man", "Ant Man", "Thor", "Loki"
print(characters[::3]) # Start at 0, skip 2, then take 3 — "Iron Man", "Loki"
# Slicing inside an element.
print(characters[2][-1]) # From element 2 — Thor, take the end, that is r
# print(characters[::-1]) # Reversed version of the list — ['Black Widow', 'Black Panther', 'Loki', 'Thor', 'Ant Man', 'Iron Man']
