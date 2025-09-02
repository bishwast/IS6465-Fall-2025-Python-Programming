""" Homework 3 """

"""Exercise 1: (3 points)
Given the list below, write a program that 
counts the # of A’s (scores between 90 and 100). 
Extension: Count the # of B’s, C’s, D’s and F’s.
Hint: use an if-elif-else condition inside a for loop.
grades = [90,100,70,45,76,84,93,21,36,99,100]"""
print("Program to count number of grade A, B, C, D, and F")
grades = [90,100,70,45,76,84,93,21,36,99,100]
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0
for g in grades:
    if g >= 90 and g <=100: a_count +=1
    elif g >= 80 and g < 90: b_count +=1
    elif g >= 70 and g < 80: c_count +=1
    elif g >= 60 and g < 70: d_count +=1
    else: f_count +=1
print(f"The number of grade A: {a_count}")
print(f"The number of grade B: {b_count}")
print(f"The number of grade C: {c_count}")
print(f"The number of grade D: {d_count}")
print(f"The number of grade F: {f_count}")

"""Exercise 2: (3 points)
Given the following list of student test scores, apply a class "curve" to each score. 
The class curve is as follows:
90 or above: no curve
80 to 90: +2 points
70 to 80: +5 points
Lower than 70: +8 points
Use the below test scores list:
    grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
    Pseudo code: for each score in list,
    If grade is greater than or equal to 90, move on to next score.
    Else if score is greater or equal to 80 but less than 90, add 2 points.
    Else if score is greater or equal to 70 but less than 80, add 5 points.
    Else, add 8 points
    Print out the new grades."""
print("\nProgram that applies class curve to each score.")
test_scores = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
point_curve = []
for s in test_scores:
    if s >= 90: point_curve.append(s)   # Score is as original score.
    elif s >= 80 and s < 90: point_curve.append(s + 2)
    elif s >= 70 and s < 80: point_curve.append(s + 5)
    else: point_curve.append(s + 8)
print(f"Original test scores is: {test_scores}")
print(f"Test scores after applying score curve is: {point_curve}")

"""Exercise 3: (3 points)
Write a program that asks the user for daily sales figures for a full week (Sunday – Saturday). 
Store these values in a list and print them out at the end of your program. 
Here's a sample running of your program:
Enter sales for Day #1: 100
Enter sales for Day #2: 200
Enter sales for Day #3: 300
Enter sales for Day #4: 400
Enter sales for Day #5: 500
Enter sales for Day #6: 600
Enter sales for Day #7: 700
Sales for the week: [100,200,300,400,500,600,700]"""
print("\nProgram to sales figures for the week.")
# Empty list to add user input per days in a week.
weekly_sales = []
# Days in a Week = 1 to 7, range(1,8).
for d in range(1,8):
    # 1. Accepting user's input as a string.
    user_input = input(f"Enter sales for Day #{d} of the week: ")
    # 2. Validating: Keep asking user if they do not enter a number or type enter key like I did.
    while user_input.strip() == "" or user_input.isdigit() == False:
        user_input = input(f"Enter sales for Day #{d} of the week: ")
    # Appending the user's input to the sales list as integers.
    weekly_sales.append(int(user_input))
print(f"Sales for the week: {weekly_sales}")

"""Exercise #4: (3 points)
Given the following list, write a program that does the following:
Extract the first 3 elements of the list into a new list
Extract the characters b, c, and d into a new list
Extract the last 4 characters into a new list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']"""

my_list_n4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Extract the first 3 elements of the list into a new list
new_list1 = my_list_n4[:3]
print("\nNew list 1: ", new_list1)
# Extract the characters b, c, and d into a new list
new_list2 = my_list_n4[1:4]
print("New list 2: ", new_list2)
# Extract the last 4 characters into a new list, -ve indexing -4 always gives last 4 elements from the list.
new_list3 = my_list_n4[-4:]
print("New list 3: ", new_list3)

"""Exercise #5: (3 points)
Given the following lists, write a program that lets the user type in the name of a product. 
If the product name exists in our inventory, you should print out that it is in our inventory. 
Otherwise you should print out that the product is not found. 
Ensure that your program is case insensitive (i.e. searches for "Apple" or "apple" or "APPLE" should all succeed).
products = ["apple", "pear", "peach", "banana"]"""
print("Program to validate if product is in Inventory.")
products = ["apple", "pear", "peach", "banana"]
for _ in products:  # As any variable after "for" will not be used in this program, therefore i have used "_" for intentionally unused variable.
    user_input = input("Enter product name or q to quit: ").lower()
    if user_input == "q":
        print("Thank you for using the program!")
        break
    elif user_input in products:
        print(f"{user_input} is in our inventory")
    else:
        print(f"{user_input} is not in our inventory")

"""Exercise #6: (3 points)
Given these two lists, write a program that finds all elements that exist in both lists 
(i.e. the integer 2 exists in both lists). 
Store your results in a list and print it out to the user. 
The expected answer is:
[1, 2, 3]
Two lists:
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]"""
print("\nProgram to find all elements that exists in both lists:")
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]
common_elements = []
for element in a:
    if element in b:
        common_elements.append(element)
print(f"Common elements in list a: {a} and b: {b} is ", common_elements)

"""Exercise #7: (3 points)
Write a program that continually prompts a user to enter in a series of first names. 
The user can elect to stop entering names when they supply the string "end." 
Store these first names in a list and print them out at the end of your program. 
Extension: Prevent the user from entering duplicate names (hint: use the in operator)."""

print("\nProgram to continually prompt user to enter first names:")
users_entries = []
while True:
    user_input7 = input("Enter your first names (Or enter \"End\") to quit): ")
    user_input7 = user_input7.strip()  # Remove any spaces.

    if user_input7.strip().lower() == "end":
        print("Thank you for using the program!")
        break
    # Check 1: For lowercase version of user entries — case sensitive
    first_name_lowercase = []
    # Validating is user's entries exists in the main list — user_entries[]
    for user_entries in users_entries:
        # Append lowercase versions of each user entries to the lowercase first names list.
        first_name_lowercase.append(user_entries.lower())
    # Check 2: For case in-sensitive entries. Removing any spaces in front of names
    if user_input7.strip().lower() in first_name_lowercase:
            print(f"First name \"{user_input7}\"already exists, please enter another name.")
    else:
        users_entries.append(user_input7)   # Appends user entries in the list as users original entries.
        print(f"First name :\"{user_input7}\" has been entered.")
print("First names in a list:", users_entries)

"""Exercise #8: (3 points)
Continually ask the user for a product name. 
Next, see if that product name is included in the inventory list below. 
If it is, remove the product from the list and then print the current list of products to the user. 
If the product is not on the list you should alert the user that we do not currently carry the product in question. 
You can end the program when the list of products is exhausted or when the user types the string "end".
products = ["apple", "pear", "peach", "banana"]"""

print("\nProgram to validate if the product is in the inventory.")
# Inventory in current list of products.
products = ["apple", "pear", "peach", "banana"]
# Ask user until they enter "end" to stop the program.
while True:
    product_entries = input("Please enter a product name: ")
    product_entries = product_entries.strip()   # Removed any spacing from the input.
    # If user types end — end the program with break and a thank you note.
    if product_entries.lower() == "end":
        print("Thank you for using this program!")
        break

    # User can enter product name in any case — Lowercase entries of product list
    lowercase_plist = []
    # Check for case-sensitive letters against the current products list.
    # Checking each entry, converting to lowercase and appending to the lowercase list.
    for p in products:
        lowercase_plist.append(p.lower())
    # Check is user's entry is not a match to current inventory. If true, prompt user.
    if product_entries.lower() not in lowercase_plist:
        print(f"Sorry, we do not currently carry \"{product_entries}\".")
    # Check if entry is matched — remove product fom the list, print the current list and prompt.
    else:
        # Checking each entry against the current products list.
        for p in products:
            # In the current products list, if lower case converted product is a match to the lower case entry — remove the product and prompt.
            if p.lower() == product_entries.lower():
                    products.remove(p)
                    print(f"Product {p} is sold.")
                    print(f"Current list of products:{products}")
                    break
    # If no product is in the list or sold out.
    if not products:
        print("Sorry, all products are sold out.")
        break

"""Exercise #9: (3 points)
The lists below are organized in such a way that the item at position 0 in the first list matches with the item at position 0 in the second list. 
With this in mind, write a product price lookup program that works as follows:
Enter a product:  peanut butter
This product costs 3.99
products = ['peanut butter', 'jelly', 'bread']
prices = [3.99, 2.99, 1.99]"""
print("\nProgram for product price lookup.")
products = ['peanut butter', 'jelly', 'bread']
prices = [3.99, 2.99, 1.99]
# users input
user_input_9 = input("Enter a product: ").strip()
user_input_9 = user_input_9.lower()
if user_input_9 in products:
    product_index = products.index(user_input_9)
    product_price = prices[product_index]
    print(f"\nThe price for \"{user_input_9}\" is ", product_price)
else:
    print("Sorry, the product is not in the inventory.")

"""Exercise #10: (3 points)
Write a program that asks a teacher for the number of students in his or her class. 
Next, ask the teacher how many assignments are given in this class. 
With this information prompt the user to enter in scores for each student and compute their average grade in the class.

Hint: use a nested for loop for the assignments inside the student for loop. (For each student, iterate for each assignment)

Sample:
(Input sample)
How many students in the class? 2
How many assignments in the class? 2
(Output sample)
Student #1
Assignment #1: 100
Assignment #2: 90
Student #1 earned a 95
Student #2
Assignment #1: 90
Assignment #2: 80
Student #2 earned a 85"""

print("\nTeacher's Dashboard Program.")
num_of_students = int(input("Enter number of students in this class: "))
num_of_assignments = int(input("Enter number of assignments in this class: "))
# range() function will give students and assignments a range per the teachers inputs/
# For each students in the range of numer of students.
for student in range(num_of_students):
    # range(num_of_students) generates values starting from 0 up to (but not including) the number given,
    # so we add 1 when printing for readability.
    print(f"Student #{student+1}")
    # Calculating scores.
    total_score = 0
    avg_grade = 0
    # range(num_of_assignments) generates values starting from 0 up to (but not including) the number given,
    # so we add 1 when printing for readability.
    for assignment in range(num_of_assignments):
        # For each assignment in the given range recording the corresponding scores.
        scores_for_each_assignments = float(input(f"Score for Assignment #{assignment + 1}: "))
        print(f"Assignment #{assignment + 1}: ", scores_for_each_assignments)

        total_score += scores_for_each_assignments
        avg_grade = total_score / num_of_assignments
    print(f"Student #{student+1} earned a average score of {avg_grade:.2f}")













