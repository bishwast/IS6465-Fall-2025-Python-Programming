

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


person = Person(

    "Jane",

    "Doe",

    datetime.date(1992, 3, 12), # year, month, day

    "No. 12 Short Street, Greenville",

    "555 456 0987",

    "jane.doe@example.com"

)


print(person.name)

print(person.email)

print(person.age())


"""
Explain what the following variables refer to, and their scope:

Person
    Person is the Class for this program defining the blueprint that contains various attributes of a Person such as
    name, surname, birthdate, address, telephone, email — as initialized in the constructor method __init__().
    This class and it's attributes can be used to create many instances of a "person" object.

person
    "person" is the specific instance also called an object of the main class "Person" and defined attributes within the constructor.

surname
    "surname" is an instance attribute of the main class "Person" which is initialized via constructor of the main class Person.
    Possibly it stores the surname of the instance "person".

self
    "self" is the first parameter of a constructor and every method that is mainly used to represent an specific Instances of the Class.

age (the function name)
    age() function or a method is defined strictly within the main class Person, which is a method with a "self" parameter
    to define it's instance. self here is used to access the instance birthdate, defined in the constructor.

age (the variable used inside the function)
    "age" in this program is a local variable that stores the value of "today.year - self.birthdate.year".
    Where, today.year, is date with a year and a month from the "datetime" module
           self.birthdate.year, is the birthdate with a year and a month defined in the constructor.

self.email
    This is the email attribute of the specific instance of the class "Person". It is initialized in the constructor and can
    be used for specific "person" instances.

person.email
    This is the email attribute of the "person" object. This was initialized when the instance "person" was created from
    the main class "Person". Retrieves value of the attribute - email of the specific instance "person".
"""