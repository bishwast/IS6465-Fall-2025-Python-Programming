"""Exercise #2: (5 points)
Rewrite the Person class so that
a person’s age is calculated for the first time when a new person instance is created,
and recalculated (when it is requested) if the day has changed since the last time that it was calculated.

Here is some code you can use to recalculate the age:
Note: you will want 2 age variables, one local to the function and one as a class variable.

def recalculate_age(self):
    today = datetime.date.today()

    # todo: set local variable "age", subtract today's year from birthdate year. age = ...
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

    # todo: set the age class variable to the new age value calculated from above.

    # todo: set a new class variable _age_last_recalculated to equal today.


def age(self):
    # replace the code in the age function

    if (datetime.date.today() > self._age_last_recalculated):
        self.recalculate_age()

    return self.age
Hints:

Add a class variable called age.

Invoke the new recalculate_age() function in both the constructor and age() function."""

import datetime

class Person:

    # Constructor — Initializing attributes
    def __init__(self, name, surname, birthdate, address, telephone, email):

        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

        # Instance variables to track the age and recalculation date
        self.age = None
        self._age_last_recalculated = None
        # A person’s age is calculated for the first time when a new person instance is created.
        self.recalculate_age()

    def recalculate_age(self):
        """recalculated person's age (when it is requested)
        if the day has changed since the last time that it was calculated. """

        today = datetime.date.today()

        # todo: set local variable "age", subtract today's year from birthdate year. age = ...
        age_local = today.year - self.birthdate.year
        # If the birthdate hasn't occurred yet this year.
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age_local -= 1

        # todo: set the age class variable to the new age value calculated from above.
        self.age = age_local

        # todo: set a new class variable _age_last_recalculated to equal today.
        _age_last_recalculated = today

    def get_age(self):
        # recalculated person's age (when it is requested)
        # if the day has changed since the last time that it was calculated.
        today = datetime.date.today()
        # If the date has changed since last recalculation.
        if self._age_last_recalculated is None or today > self._age_last_recalculated:
            self.recalculate_age()
        # Calculated age
        return self.age


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"

)
print(f"Name: {person.name}")
print(f"Email: {person.email}")
print(f"Age: {person.get_age()}")
