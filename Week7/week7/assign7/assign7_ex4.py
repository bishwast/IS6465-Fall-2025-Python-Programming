"""Create an instance of the Person class.
Use the dir function on the instance.
    Then use the dir function on the class.

1. What happens if you call the __str__ method on the instance?
    Verify that you get the same result if you call the str function with the instance as a parameter.
2. What is the type of the instance?
3. What is the type of the class?
4. Write a function which prints out the names and values of all the custom attributes of any object that is passed in as a parameter.
    (see vars() hint.)
Dir() Hint:
    person = Person()
    print(dir(person))

vars() Mega
    hint: (this is the solution)
    print(vars(person))"""
import datetime
class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):

        self.name = name

        self.surname = surname

        self.birthdate = birthdate

        self.address = address

        self.telephone = telephone

        self.email = email


    def age(self):

        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):

            age -= 1

        return age

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Birthdate: {self.birthdate}\n"
                f"Address: {self.address}\n"
                f"Telephone: {self.telephone}\n"
                f"Email: {self.email}")


person = Person(

    "Jane",

    "Doe",

    datetime.date(1992, 3, 12), # year, month, day

    "No. 12 Short Street, Greenville",

    "555 456 0987",

    "jane.doe@example.com"

)

print("1. What happens if you call the __str__ method on the instance?\n"
      "This will internally call the __str()__ method and prints the attributes returned in the method as below.\n")
print(person)

print("Verify that you get the same result if you call the str function with the instance as a parameter.\n")
print(f"{person.__str__()}")

print("2. What is the type of the instance?\n")
print(f"Type: {type(person)}\n"
      f"Type: {type(person.__str__())}\n")

print("3. What is the type of the class?")
print(f"Type: {type(Person)}\n")

print("Write a function which prints out the names and values of all the custom attributes of any object that is passed "
      "in as a parameter. (see vars() hint.)\n")

def get_attributes(person):
    all_attributes = vars(person)   # var() here accesses any person object attributes
    for attribute, value in all_attributes.items():
        print(f"{attribute}: {value}")
get_attributes(person)

print("")
# Use the dir function on the instance — Calls all the Attributes and Methods that are part of the "person" Instance.
print("With dir() function on the Instance.")
print(dir(person))

print("")
# Use the dir function on the class — Calls all the Attributes and Methods that are part of the "Person" Class.
print("With dir() function on the Class.")
print(dir(Person))