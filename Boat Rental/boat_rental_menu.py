"""
================================================================================
PROJECT: Boat Rental Management System
COURSE: IS 6495-090 Fall 2025
TEAM: Final Group Project 4
AUTHORS: Sunil Tiwari
================================================================================

PROJECT OVERVIEW:
This project is a command-line application to manage a boat rental business.
It is built using Python 3 and uses an SQLite database for data persistence.

KEY FEATURES:
- Full CRUD Functionality: Create, Read, Update, and Delete records for
  boats, customers, and rentals.
- Object-Oriented Design (OOP): The program is split into three logical
  layers for maintainability:
    1. Presentation Layer (boat_rental_menu.py): Handles all user
       interaction (the UI).
    2. Data/Logic Layer (boat_rental_entities.py): Handles all business
       logic and database queries (the "brain").
    3. Database Base Layer (DBbase.py): A reusable parent class for
       managing all database connections.
- Database Management: Uses SQLite to store all data. The database
  and tables are created automatically on the first run.
- Data Population: Includes a 'DataPopulator' class that reads from an
  external 'boat_rentals.csv' file (File I/O) to populate the
  initial boat inventory.
- Robust Error Handling: Uses 'try/except' blocks to handle both
  invalid user input (e.g., typing letters for a number) and
  database errors (e.g., SQL syntax errors).

CORE USE CASES IMPLEMENTED:
- View boat inventory and availability.
- View all active rentals.
- Book a new rental (finds or creates a customer, links them to an
  available boat, and marks the boat as 'Rented').
- Return a completed rental (calculates duration/cost, marks the
  rental as 'Completed', and sets the boat back to 'Available').
- Add a new boat to the inventory.
- Update Customer's Phone Number.
- Reset the database to its initial state for testing.

================================================================================
"""

import boat_rental_entities as bre
import os
from datetime import datetime
import time

# A flag to control behavior. True = reset DB and False = Maintains the Data on every launch.
DEV_MODE = False

class MainMenu:

#1 Runs the class
    def run(self):
        """Main Menu - Method that runs the boat rental program"""
        # --- DATABASE INITIALIZATION ---
        db_file = os.getcwd() + "/boat_rental.sqlite"

        # If in DEV_MODE or the DB file is missing, create/reset it.
        if DEV_MODE or not os.path.exists(db_file):
            if DEV_MODE:
                print("DEVELOPMENT MODE: Resetting and Populating the Database..")
            else:
                print("Database does not exist. Creating and populating the database...")

            # Call the DataPopulator class from the entities file
            bre.DataPopulator().populate_database()
            print("Database created successfully!")

        # --- MENU LOGIC ---
        # A dictionary to hold the menu options
        main_options = {
            "book": "Book New Rental",
            "return": "Return Completed Rental",
            "view_inv": "View Boat Inventory",
            "view_rent": "View Active Rentals",
            "add_boat": "Add New Boat to Inventory",
            "update_customer": "Update Customer's Phone Number",
            "reset": "Reset Database (DANGER)",
            "exit": "Exit Program"
        }
        print("--- Welcome to the Boat Rental Menu! ---")
        user_selection = ""

        # The main application loop
        while user_selection != "exit":
            print("--- Main Menu ---")
            # Loop through the dictionary to print options
            for key, value in main_options.items():
                print(f"{key}: {value}")

            user_selection = input("\nSelect an option: ").lower()

            # --- MENU ROUTING ---
            # Call the appropriate "private" method based on user's choice
            if user_selection == "book":
                self._book_rental()
            elif user_selection == "return":
                self._complete_rental()
            elif user_selection == "view_inv":
                self._view_inventory()
            elif user_selection == "view_rent":
                self._view_rent()
            elif user_selection == "add_boat":
                self._add_boat()
            elif user_selection == "update_customer":
                self._update_customers_phNum()
            elif user_selection == "reset":
                self._reset_db()
            elif user_selection == "exit":
                continue    # Skip the pause and let the loop end
            else:
                print("\nInvalid Selection. Please try again!")

        print("\nThank you for using the Boat Rental Menu! Goodbye!")

#2 Display results
    def _display_results(self, title, results):
        """
        A private helper method to print a formatted list of results.
        This avoids duplicating this print logic in multiple places.
        """
        print(f"\n--- {title} ({len(results)} records) ---")
        if not results:
            print("No records found.")
            return

        # Enumerate gives us an index (i) and the item (item)
        for i, item in enumerate(results):
            # item[0] is the ID
            # item[1:] is a tuple of all other fields
            print(f"ID: {item[0]} | Details: {item[1:]}")

    def _view_inventory(self):
        """View Inventory"""
        print("\n--- Viewing Full Boat Inventory ---")

        # 1. Create instance of the Boat class
        boats = bre.Boat()
        # 2. Call its 'fetch' method to get all boats
        results = boats.fetch()
        # 3. Close the DB connection
        boats.close_db()
        # 4. Display the results
        self._display_results("Boat Inventory (ID, Type, Make, Model, Cap, Rate, Status)", results)
        input("Press Enter/Return to continue...")

    def _view_rent(self):
        """View Active Rentals"""
        print("\n--- Viewing Active Rentals ---")
        # 1. Create instance
        rentals = bre.Rentals()
        # 2. Fetch only rentals with status "Active"
        results = rentals.fetch_rental(status="Active")
        # 3. Close connection
        rentals.close_db()
        # 4. Display results
        self._display_results("Active Rentals (ID, Boat, Customer, StartTime, EndTime, Hours, Cost, Status, Rate)", results)
        input("Press RETURN/ENTER to continue...")

    def _add_boat(self):
        """Add New Boat"""
        print("\n---Add New Boat to Inventory---")
        boat_type = input("Enter the Boat Type: ").lower()
        make = input("Enter the Boat Make: ").lower()
        model = input("Enter the Boat Model: ").lower()

        try:
            # Use try/except to catch bad user input (e.g., "abc")
            capacity = int(input("Enter the Boat Capacity: "))
            hourly_rate = float(input("Enter the Boat Hourly Rate: "))

        except ValueError:
            # If input is bad, print error and exit the method
            print("Invalid Boat Type. Boat Addition Aborted!")
            input("Press RETURN/ENTER to continue...")
            return

        # If input is good, proceed
        boats = bre.Boat()
        current_date = datetime.now().strftime("%Y-%m-%d")
        # Call the 'add' method from the entities class
        boats.add(current_date, boat_type, make, model, capacity, hourly_rate, "Available")
        boats.close_db()
        print(f"Successfully added new boat {boat_type} {make} {model} to inventory!")
        input("Press RETURN/ENTER to continue...")

    def _book_rental(self):
        """Handles the multistep process of booking a new rental."""
        # This process needs all three entity classes
        rentals = bre.Rentals()
        customers = bre.Customers()
        boats = bre.Boat()

        # --- 1. GET Customer's Info ---
        print("\n--- Customer's Information ---")
        phone = input("Enter the Phone Number (xxx-xxx-xxxx): ")
        # Fetch customer by phone
        customer_record = customers.fetch(phone=phone)
        customer_id = None

        if customer_record:
            # If they exist, grab their ID
            customer_id = customer_record[0]
            print(f"Welcome back, {customer_record[1]} {customer_record[2]}!")
        else:
            # If not, create them
            print("Customer not found. Creating new customer...")
            first_name = input("Enter the First Name: ").lower()
            last_name = input("Enter the Last Name: ").lower()
            # The .add() method returns the new customer's ID
            customer_id = customers.add(first_name, last_name, phone)

            if not customer_id:
                # If adding failed (e.g., database error), abort.
                print("\nCould not find nor create the customer record. Aborting!")
                customers.close_db()
                rentals.close_db()
                boats.close_db()
                return

        # We are done with the customers table for now
        customers.close_db()

        # --- 2. Select Boat ---
        available_boats = boats.fetch()     # Calls Boat.fetch() as rentals inherits from Boat
        # Use a list comprehension to filter for 'Available' boats
        self._display_results("Active Rentals (ID, Type, Make, Model, Capacity, Hourly Rate, Status)",
                              [b for b in available_boats if b[7] == "Available"])

        # If the list of available boats is empty, abort.
        if not [b for b in available_boats if b[7] == "Available"]:
            print("\nNo available boats are currently available.")
            rentals.close_db()
            boats.close_db()
            input("Press RETURN/ENTER to continue...")
            return

        try:
            # Get user's boat choice
            boat_id_str = input("Enter the Boat ID to rent: ")  # As input is a string
            if not(boat_id_str.isdigit()):      # Integer validation
                raise ValueError("Boat ID is not valid. Must be an integer.")
            boat_id = int(boat_id_str)

            # --- 3. Validate the chosen boat ID ---
            # Fetch the specific boat they chose
            boat_to_rent = boats.fetch(boat_id)

            if not boat_to_rent:
                raise ValueError(F"No boat found with ID {boat_id}!")
            # Check its status (index 7)
            if boat_to_rent[7] != "Available":
                raise ValueError(F"Boat ID {boat_id} is not available!")

        except ValueError as e:
            # Catch any validation errors (bad ID, unavailable boat)
            print(f"Booking Aborted: {e}")
            rentals.close_db()
            boats.close_db()
            input("Press RETURN/ENTER to continue...")
            return

        # --- 4. Book the Rental ---
        # If all checks pass, get current time
        start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Call the booking method from the entities layer
        # This one method handles the INSERT to Rentals and UPDATE to Boats
        success = rentals.rental_booking_records(boat_id, customer_id, start_time_str)

        if success:
            print(F"Booking confirmed for Boat ID {boat_id}\nCustomer ID: {customer_id}\nStart Time: {start_time_str}")
        else:
            print(f"Booking failed for Boat ID {boat_id} at Start Time: {start_time_str}")

        # Clean up all connections
        rentals.close_db()
        boats.close_db()
        input("Press RETURN/ENTER to continue...")

    def _complete_rental(self):
        """Handles the multistep process of returning a rental."""
        rentals = bre.Rentals()

        # --- 1. View all ACTIVE rentals ---
        active_rentals = rentals.fetch_rental(status="Active")
        # We only show the first few columns for brevity
        self._display_results("Active Rentals (ID, Boat, Customer, StartTime)", [(r[0], r[2], r[3], r[4]) for r in active_rentals])

        if not active_rentals:
            rentals.close_db()
            input("Press RETURN/ENTER to continue...")
            return

        # --- 2. GET rental ID and Calculate Duration ---
        try:
            rental_id_str = input("Enter the Rental ID: ")
            if not(rental_id_str.isdigit()):
                raise ValueError("Rental ID is not valid. Must be an integer.")
            rental_id = int(rental_id_str)

            # Fetch the full record for the specific rental
            # This uses the complex JOIN query from Rentals.fetch_rental()
            rental_record = rentals.fetch_rental(rental_id)

            # --- 3. Validate the rental ---
            if not rental_record:
                raise ValueError(f"No rental record found with ID {rental_id}!")
            # Check status (index 8 in the fetch_rental query)
            if rental_record[8] != "Active":
                raise ValueError(f"Rental ID {rental_id} is not 'Active'. Status: {rental_record[8]}")

            # --- 4. Calculating rental hours ---
            # Get start time (index 4) and convert from string to datetime object
            start_time = datetime.strptime(rental_record[4], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.now()   # Get current time

            # Subtracting two datetime gives a 'timedelta' object
            duration = end_time - start_time

            # Converting timedelta to hours
            rental_hours = round(duration.total_seconds() / 3600.0, 2)

            # Apply minimum charge rule
            if rental_hours < 0.25:
                rental_hours = 0.25

            print(f"Rental Duration: {rental_hours:.2f} hour(s)")

            # --- 5. Confirm and Process ---
            confirmation = input(F"\nConfirm Rental ID {rental_id} completion? (Y/N): ").lower()

            if confirmation == "y":
                # Convert end_time back to a string for the database
                end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
                # Call the method that updates Rentals and Boats tables
                rentals.complete_rental(rental_id, end_time, rental_hours)
            else:
                print("Rental Completion is Aborted!")

        except ValueError as e:
            print(f"Booking Aborted: {e}")
        except Exception as e:
            # Catch-all for any other unexpected errors
            print(f"Error Occurred: {e}")

        # Clean up connection
        rentals.close_db()
        input("Press RETURN/ENTER to continue...")

    def _update_customers_phNum(self):
        """Updates the customer phone number (phone number) based on the customer ID (Existing Records)."""

        print("---Updating customer phone number---")

        # Instance from the Customers Class
        customer = bre.Customers()

        # 1--Find the Customer's Ph Num
        try:
            # Getting Customer's current Ph number
            old_phone_number = input("Enter Customer's Current Phone Number: ")
            customer_record = customer.fetch(phone=old_phone_number)

            # If entered phone number is not in the database
            if not customer_record:
                print(f"No customer found with Phone Number: {old_phone_number}!")
                customer.close_db()
                input("Press RETURN/ENTER to continue...")
                return

            customer_id = customer_record[0]
            print(f"Found Customer: {customer_record[1]} {customer_record[2]}")

        # 2--Get the new customer
            new_phone_num = input("Enter New Phone Number: ")
            if not new_phone_num:
                print("No new phone number provided! Aborting...")
                input("Press RETURN/ENTER to continue...")
                return

        # 3 -- Checking for valid digits for a phone number
            n_phone_num = new_phone_num.replace("-", "")        # Replcing the "-" with no space ""

            if not n_phone_num.isdigit():
                print("New phone number must be an integer with dash. No other characters are allowed. Aborting...")
                customer.close_db()
                input("Press RETURN/ENTER to continue...")
                return

        # 3---Update Method call
            success = customer.update(customer_id, phone_number=new_phone_num)
            if success:
                print(f"For Customer ID:{customer_id} and Phone Number: {old_phone_number} is updated to {new_phone_num} successfully!")
            else:
                print(f"Error updating customer {customer_id}: {old_phone_number}!")

        except ValueError as e:
            print(f"Booking Aborted: {e}")

        customer.close_db()
        input("Press RETURN/ENTER to continue...")

    def _reset_db(self):
        """Handles full database reset."""
        # Safety check!
        confirm = input("WARNING !!! This will DELETE ALL DATA. Continue? (Y/N)").lower()
        if confirm == "y":
            print("\nResetting database...")
            # Use the DataPopulator which handles resetting all tables and repopulating
            bre.DataPopulator().populate_database()
            print("Database reset and initial data populated.")
        else:
            print("Database reset aborted!")
        input("Press RETURN/ENTER to continue...")

# This line makes the 'run()' method execute ONLY when this file is run directly.
# Test Subject -
    # "Alice", "Smith", "764-471-4445
    # ('Bob', 'Johnson', '800-668-9144'),
    # ('Charlie', 'Brown', '668-991-8453'),"
if __name__ == '__main__':
    project = MainMenu()
    project.run()




