"""Week 4, Code Along 1 — Intro to the split function, split(). Split function does not change the value of the variable,
instead it tales those value and changes it into a list and returns it into a different variable.
split() is only available to strings"""

my_numbers = "10 20 30 40 50 60"
print(my_numbers)
print(type(my_numbers))
number_list = my_numbers.split()
print("After Splitting \"my_numbers\"")
print(number_list)
print(type(number_list))

# Using a for loop inside a list comprehension to convert each string in my_numbers.split() to an integer.
int_list = [int(x) for x in my_numbers.split()]
print(int_list)
print(type(int_list))
print(type(number_list))
print(len(number_list))

# Emulate a csv file.
my_csv = "Scooby Doo, Harry Potter, Darth Vader, Bugs Bunny, Captain America"
print(my_csv)
print(type(my_csv))
# Delimiter with ","
str_list = my_csv.split(",")
print(str_list)
print(type(str_list))
print(str_list[1])

# Time Example
my_time = "10:05:45, 09:45:32, 07:30:25"
# We have 2 things to split — "," and ":"
time_list = my_time.split(",")
print(time_list)
for item in time_list:
    time = item.split(":")
    print(time)

time = "07:49:34"
hours, minutes, seconds = time.split(":")
print("h:", hours, "m:",minutes, "s:",seconds)
print(type(hours))