"""Course IS6495 Fall 2025
In Class Exercise 2: Dictionaries"""

"""1.1 Create Dictionaries (2.5 points)
Use any names and birthdays you want to create a birthday dictionary that has four entries.  
The name is the key and the value is the birth date.  
Print each birth date by using the key to access each entry. """
birthday_dict = {
    "Doomsday": "1992-11-17",
    "The Hulk": "1978-05-21",
    "Superman": "1938-06-01",
    "Batman": "1939-03-30"
}
print(birthday_dict)
for names, birthdays in birthday_dict.items():
    print(names, "->", birthdays)

"""1.2 Update Dictionaries (2.5 points)
Using the dictionary from above, update the last entry and change the birth date to 06/06/1980."""
print("\nNew Birthday Dictionary:")
birthday_dict["Batman"] = "06/06/1980"
for names, birthdays in birthday_dict.items():
    print(names, "->", birthdays)

"""1.3 Dictionary With Lists (2.5 points)
Create a dictionary of the seasons Fall, Spring and Summer 
where the name of the season is the key and the value is a list of the months in that season. 
Print the value of "Fall"."""

seasons = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}
print("\nFall Season's are: ", seasons["Fall"])

"""1.4 Dictionary Merge (2.5 points)
Create the same dictionary as in exercise 3 but also create a second dictionary with only the season of Winter.  
Use the dictionary.update method to merge the winter dictionary into the seasons dictionary.  
Print the seasons dictionary."""

winter_seasons = {
    "Winter": ["December", "January", "February"]
}
seasons.update(winter_seasons)  # I could print this line of code directly, however, line below is more readable format.
print("\nUpdated Dictionary including all Seasons:")
for season, months in seasons.items():
    print(season, "->", months)