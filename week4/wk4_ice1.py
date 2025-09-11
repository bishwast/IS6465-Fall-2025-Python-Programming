"""Course: IS 6465 Fall 2025
In-Class Exercise 1:List Manipulation
"""

""" #4.1. Split Number List (2.5 points)
Use the string.split method create a list of numbers from the following string and then print the list to the screen.
    '10 67 123 46 20 18 36 250'
Do the same thing for this string:
    '10,67,123,46,20,18,36,250' """
num_list1 = "10 67 123 46 20 18 36 250"
num_list1 = num_list1.split()
print(num_list1)
print(type(num_list1))
num_list2 = "10,67,123,46,20,18,36,250"
num_list2 = num_list2.split(",")
print(num_list2)
print(type(num_list2))

"""4.2 Split Data into List (2.5 points)
Use the string.split method create a list of numbers from the following string and then sum up the numbers.  
Print the sum to the screen.
    '90,67,87,102,77,80' """
list_4_2 = "90,67,87,102,77,80"
int_list_4_2 = [int(i) for i in list_4_2.split(",")]
print(int_list_4_2)
total = 0
for i in int_list_4_2:
    total += i
print(f"\nSum of numbers in the list of {int_list_4_2} is: ", total)

"""4.3 Slice Lists (2.5 points)
Use the slicing syntax of lists to get the first 4 numbers in the following list and print out the results.
    [1,2,3,4,5,6,7,8,9] """
list_4_3 = [1,2,3,4,5,6,7,8,9]
print(f"\nFirst 4 numbers in the list {list_4_3} are:", list_4_3[:4])

"""4.4 Slice Lists with Increment (2.5 points)
Use the slicing syntax of lists to get every other entry in the following list starting at the beginning and print the results.
['a','b','c','d','e','f','g']
Sample output:
['a', 'c', 'e', 'g']"""
list_4_4 = ['a','b','c','d','e','f','g']
print(f"\nEvery other entry in the list of {list_4_4} are: ", list_4_4[::2])


