"""In Class Ex 1: Basic Functions"""
"""1.1. Hello World (again) (3 points)
Write a function that asks for the user’s name and prints “Hello, “ followed by their name."""
def get_user_name():
    input1 = input("Please enter your name: ").lower()
    username = input1.title()
    print(f"Hello, {username}!")
get_user_name()

"""1.2. Dog Years (3 points)
Write a function that asks for the age of the user’s dog. 
Print a string that states the dog’s age in dog years with a conversion rate of 1 human year to 7 dog years."""
def human_dog_years():
    input1 = int(input("\nPlease enter your dog's human age: "))
    # 1 human year to 7 dog years
    dogs_years = input1 * 7
    # 7 dog years = 1 human year
    print(f"Your dog is {input1} human years old which is {dogs_years} dog years, as 1 human year = 7 dog years.")
human_dog_years()

"""1.3. Purchase (3 points)
Write a function that asks for the user to enter a number of items they wish to purchase."""
def get_num_items_count():
    num_items = int(input("\nEnter number of items you wish to purchase: "))
    print("Total number of items you wish to purchase: ", num_items)
get_num_items_count()