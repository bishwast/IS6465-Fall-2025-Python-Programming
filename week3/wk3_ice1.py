"""
In Class Exercise 1
Obj: Basic Lists
"""
"""
1.1. Creating and Modifying a List (2.5 points)
Create a list of four different sports of your choice, modify it by adding and removing elements, and print the updated list.
"""
my_sports = ["badminton", "table tennis", "soccer", "cricket"]
print(my_sports)
my_sports.append("volleyball")
print(my_sports)
my_sports.insert(3,"baseball")
print(my_sports)
my_sports.remove("cricket")
print(my_sports)

"""1.2. Copying and Modifying Lists (2.5 points)
Create a list of five different desserts of your choice. 
Copy the list of desserts to a new list, modify both lists separately, and print both."""
my_desserts = ["apple pie", "lemon pie", "banana pudding", "chocolate cake", "brownie"]
my_desserts.sort(reverse=True)
print("\nMy dessert list: ", my_desserts)
my_new_desserts = my_desserts.copy()
my_new_desserts.sort()
print("My new dessert list: ", my_new_desserts)

my_desserts.insert(3,"cheesecake")
print("\nMy dessert list: ", my_desserts)
my_desserts.remove("apple pie")
print("My dessert list: ", my_desserts)
my_desserts.append("donuts")
print("My dessert list: ", my_desserts)
print("From my_desserts with slice: ", my_desserts[2:4])

item_popped = my_new_desserts.pop(1)
print("\nMy new dessert list: ", my_new_desserts)
print("Deleted item from my new list: ", item_popped)
del my_new_desserts[3]
print("My new dessert list: ", my_new_desserts)
my_new_desserts.append("raspberry pie")
print("My new dessert list: ", my_new_desserts)

