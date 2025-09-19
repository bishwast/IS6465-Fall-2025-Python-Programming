"""In-class exercise 2 - Function Arguments and Variables"""
"""2.1. Sum of numbers (3 points)
Write a function that takes a list of numbers and returns the sum of the numbers."""
def get_sum_of_numbers(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total += num
    return total
print(get_sum_of_numbers([1,2,3,4,5]))

"""2.2. Number power (3 points)
Write a function that takes two integers 
and raises the first number to the power of the second number
and returns the result."""
def get_num_power(num1, num2):
    return num1 ** num2
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} to the power of {num2} is {get_num_power(num1, num2)}")

"""2.3. Tax function (3 points)
Write a function that takes the price of the item as an argument 
and return the price calculated with a tax value of .07. 
The goal here is to convert the tax calculation into a reusable function. 
(Reflective from HW2, problem 2.7)"""
def get_tax_price(price_before_tax):
    price_after_tax = price_before_tax + (price_before_tax * .07)
    return price_after_tax
item_price = float(input("\nEnter the item price: "))
print(f"\Price including tax for item worth $ {item_price:.2f} is $ {get_tax_price(item_price):.2f}")

"""2.4. Average function (3 points)
Write a function that takes three arguments (numerical) 
and returns the average of the numbers entered."""
def average(input1, input2, input3):
    total = input1 + input2 + input3
    return total / 3
print("\nPlease enter three numbers below to get their average!")
input_1 = float(input("Enter the first number: "))
input_2 = float(input("Enter the second number: "))
input_3 = float(input("Enter the third number: "))
print(f"The average of {input_1}, {input_2} and {input_3} is: {average(input_1, input_2, input_3):.2f}")






