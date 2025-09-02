"""
Code Along 2
Obj: Working with lists
"""
my_list = ["Christine", "Jack", "Benny", "Rene", "Jerry"]
my_list.append("Jeff")  # Appends to end of my_list — ['Christine', 'Jack', 'Benny', 'Rene', 'Jerry', 'Jeff']
print(my_list)

# Delete
del my_list[1] # Deletes index 1 — "Jack" — ['Christine', 'Benny', 'Rene', 'Jerry', 'Jeff']
print(my_list)

# pop() — deletes element in a list and prints out that item
item = my_list.pop(1)   # List is ['Christine', 'Benny', 'Rene', 'Jerry', 'Jeff']
print(my_list)          # New List — ['Christine', 'Rene', 'Jerry', 'Jeff']
print(item)             # Benny

my_list.reverse()
print(my_list)  # ['Jeff', 'Jerry', 'Rene', 'Christine']

location = my_list.index("Jeff")
print(location) # At index 0

prices = [3.99, 2.98, 1.99, 0.99, 0.99]
biggest_mum = max(prices)
print(biggest_mum)  # 3.99
smallest_num = min(prices)
print(smallest_num) # 0.99
print(smallest_num, "up to", biggest_mum)
prices.insert(1, 6.99)
prices.remove(0.99) # Removes first occurrence from the list.
print(prices)
prices.sort()   # Lowest to Biggest
print(prices)
prices.sort(reverse=True) # Biggest to Smallest
print(prices)