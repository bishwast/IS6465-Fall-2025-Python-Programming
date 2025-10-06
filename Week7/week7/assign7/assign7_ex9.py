"""Exercise #9: (5 points)
Step 1:
Write a function named collatz() that has one parameter named number.
    If number is even, then collatz() should print number // 2 and return this value.
    If number is odd, then collatz() should print and return 3 * number + 1.

Step 2:
Write a program that lets the user type in an integer
and that keeps calling collatz() on that number until the function returns the value 1.

Amazingly enough, this sequence actually works for any integer—sooner or later,
using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.

Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”

Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
"""

def collatz(number):
    # If Even
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # If Odd
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Checking for an Integer.
while True:
    try:
        n = int(input("Give me a number: "))
        break # if n is a valid integer.
    except ValueError as ve:
        print(f"Error Details: {ve}\n That's not a number.")
# Continuously calling collatz() function until the number becomes 1
while n != 1:
    n = collatz(n)


"""NOTE: For Self Reference 
Collatz Conjecture, also known as the 3n + 1 problem or the Syracuse problem. 
Mathematically, the Collatz conjecture is a sequence defined as follows:

Start with any positive integer n.
    If n is even, divide it by 2:
        n = n/2
    If n is odd, multiply it by 3 and add 1:
        𝑛 = 3𝑛 + 1
Repeat the process indefinitely with the new value of n.

The goal: 
The Collatz Conjecture claims that no matter which positive integer you start with, 
you will eventually reach the number 1, regardless of the starting value.
"""