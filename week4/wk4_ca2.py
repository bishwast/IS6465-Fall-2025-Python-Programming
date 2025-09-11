"""Week 4, Code Along 4 — Dictionary, Sets, and Tuples """

my_dictionary = {
    "name": "Thor",
    "age": 1500,
}
print(my_dictionary)

# Data structures within a data structure
example_dict = {
    "animals": ["Dogs", "Cats", "Fish"],
    "number": 1,
    "name": "Odin",
    "a_boolean": True,
    "another_dict": {
        "you could": "keep going",
        "like this": "forever"
    }
}

for key in example_dict:
    print(key)

for item in example_dict.items():
    print(item)

# Iterator
for  v in example_dict.values():
    print(v)

a_dictionary = {"Color" : "Blue",
                "Fruit" : "Orange",
                "pet": "dog"
}
for key in a_dictionary:
    print(key, "->", a_dictionary[key])

states = {
    "AK": "Alaska",
    "AL": "Alabama",
    "HI": "Hawaii",
    "MS": "Mississippi",
    "UT": "Utah"
}
# Returning items as data structures. — ('AK', 'Alaska')
for item in states.items():
    print(item)

# Returning items as independent values in k and v. — AK Alaska
for k, v in states.items():
    print(k, v)

seasons = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}
print(seasons)
winter_season = {
    "Winter": ["December", "January", "February"]
}
# Merging 2 dictionaries
seasons.update(winter_season)
print(seasons)

# SETS - Un Ordered Collection of Unique Objects.
small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes) # {2, 3, 5}
print(type(small_primes))

small_primes.add(1)
print(small_primes) # {1, 2, 3, 5}

# Boolean logic to Sets
print(3 in small_primes)    # Ture
print(4 in small_primes)    # False
print(4 not in small_primes)    # True

small_primes.add(3)
print(small_primes) # Does not include duplicate number to the set.

# Tuples () — Immutable sequence of 0 or more values.
t = ("a", "b", "c", "e")
print(t)
print(type(t))
# Immutable - Cannot be changed.
# t[1] = "xyz"
# print(t)    # Error

print(t.count("d")) # 0

# Convert List to a Set
list_a = [1,2,3]
list_b = [2,3,4]
print(list(set(list_a) & set(list_b)))  # [2, 3] — Intersection of sets list_a and list_b.



