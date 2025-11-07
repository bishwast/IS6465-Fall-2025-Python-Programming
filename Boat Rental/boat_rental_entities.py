"""
Boat Rental Project file for database interaction and CRUD operations.
Entities:
    Parts: Such as Boat Inventories
    Customers: Information
    Rentals: Reservation and Booking information that links boat and the customer
"""
import os
import DBbase as db
import csv
from datetime import datetime
import sqlite3

# BOAT CLASS
class Boat(db.DBbase):
    """
    Inherits from db.DBbase main class.
    This class handles all CRUD operations for the 'boat_rental_entities' table.
    """

# 1 Class Constructor
    def __init__(self):
        """
        Constructor. Runs automatically when the class is instantiated.
        It calls the parent's (__init__) constructor using super()
        and passes the "boat_rental.sqlit" database file it needs to manage for db_name.
        """
        super().__init__("boat_rental.sqlite")

# 2 Reset Database or Create if not present.
    def reset_database(self):
        """Creates or resets the database 'boat_rental_entities' table."""
        try:
            # This multi-line SQL string defines the table schema
            """Boat Entities: Date, BoatType, Make, Model, Capacity, HourlyRate, AvailabilityStatus"""
            sql = """
                DROP TABLE IF EXISTS boat_rental_entities;
                
                CREATE TABLE boat_rental_entities (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    Date TEXT NOT NULL,
                    BoatType TEXT NOT NULL,
                    Make TEXT NOT NULL,
                    Model TEXT NOT NULL,
                    Capacity INTEGER NOT NULL,
                    HourlyRate REAL NOT NULL, --Stores Floating Point Number for calculations purpose
                    AvailabilityStatus TEXT NOT NULL DEFAULT 'Available'                    
                );
            """
            # execute_script() is from the DBbase parent class
            super().execute_script(sql)
            # Commits the changes
            super().get_connection.commit()
            print("Table \"boat_rental_entities\" is reset successfully!")

        except Exception as e:
            print(f"Error resetting \"boat_rental_entities\": {e}")

# 3 Add
    def add(self, date, boat_type, make, model, capacity, hourly_rate, availability_status):
        """Adds a new boat to the database.
        7 Entities: Date, BoatType, Make, Model, Capacity, HourlyRate, AvailabilityStatus """
        try:
            sql = """
                INSERT INTO boat_rental_entities (
                    Date, 
                        BoatType, 
                        Make, 
                        Model, 
                        Capacity, 
                        HourlyRate, 
                        AvailabilityStatus)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """
            # Open the portal to Database and execute the SQL
            super().get_cursor.execute(sql, (date, boat_type, make, model, capacity, hourly_rate, availability_status))
            # Establish the connection
            super().get_connection.commit()
            print(f"Added {make} {model} {boat_type} to database successfully.")

        except Exception as e:
            print(f"Error adding the boat: {e}")

# 4 Update - hourly_rate=None, availability_status=None, these parameters will be updated only if provided.
    def update(self, boat_id, hourly_rate=None, availability_status=None):
        """Updates a boat's availability status and/or hourly rate."""
        try:
            # This logic dynamically builds the SQL query so we can update one, the other, or both in the entity table.
            parameters = [] # Stores the actual values that will replace the placeholder "?".
            sql_parts = []  # Goes into the SQL SET Clause

            # If the hourly_rate is provided, include in parameter and add to SET in SQL
            if hourly_rate is not None:
                sql_parts.append('HourlyRate = ?')
                parameters.append(hourly_rate)

            # If the availability_status is provided, include in parameter and add to SET in SQL
            if availability_status is not None:
                sql_parts.append('AvailabilityStatus = ?')
                parameters.append(availability_status)

            # If no new values were provided, don't run the query.
            if not sql_parts:
                print("Update Failed! No parameters provided.")
                return False

            # Join the parts: "SET HourlyRate = ?, AvailabilityStatus = ?" for only the records with the given ID
            sql = f"UPDATE boat_rental_entities SET {', '.join(sql_parts)} WHERE id = ?;"

            # Add the boat_id as the last parameter (for the WHERE clause)
            parameters.append(boat_id)
            # Preventing SQL Injection, runs SQL query will all parameters safely substituted.
            super().get_cursor.execute(sql, tuple(parameters))
            # Connect and save changes to the database.
            super().get_connection.commit()
            print(f"Updated {boat_id} successfully.")
            return True

        except Exception as e:
            print(f"Error Updating boat {boat_id}: {e}")
            return False

# 5 Delete
    def delete(self, boat_id):
        """Deletes a boat from the inventory database, only if availability status is not in a rental condition."""
        try:
            # DELETE SQL statement
            super().get_cursor.execute("DELETE FROM boat_rental_entities WHERE id = ?;", (boat_id,))
            super().get_connection.commit()
            print(f"Deleted Boat ID: {boat_id} successfully.")
            return True

        except Exception as e:
            print(f"Error deleting boat {boat_id}: {e}")
            return False

# 6 Fetch - Retrieve Boats
    def fetch(self, boat_id=None, boat_type=None):
        """
        Fetches boat records.
        - If boat_id is given, fetches one specific boat.
        - If boat_type is given, fetches all boats of that type.
        - If neither is given, fetches all boats.
        """
        try:
            if boat_id is not None:
                # .fetchone() returns a single record or None
                return super().get_cursor.execute("SELECT * FROM boat_rental_entities WHERE id = ?;", (boat_id,)).fetchone()
            elif boat_type is not None:
                # .fetchall() returns a list of all matching records
                return super().get_cursor.execute("SELECT * FROM boat_rental_entities WHERE id = ?;", (boat_type,)).fetchall()
            else:
                # Fetch all
                return super().get_cursor.execute("SELECT * FROM boat_rental_entities;").fetchall()

        except Exception as e:
            print(f"An error has occurred while fetching boat(s).\nError Details: {e}")
            return []   # Do nothing, return empty list on failure

# CUSTOMER CLASS
class Customers(db.DBbase):
    """CURD Operations for Customers table"""

#1 Constructor
    def __init__(self):
        """Constructor - calls the parent and sets the DB file"""
        super().__init__("boat_rental.sqlite")

#2 Create or Reset Database
    def reset_database(self):
        """Creates or resets the Customers table."""
        try:
            sql = """
                DROP TABLE IF EXISTS Customers;
                
                CREATE TABLE Customers (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    FirstName TEXT NOT NULL,
                    LastName TEXT NOT NULL,
                    Phone TEXT UNIQUE
                );
            """
            super().execute_script(sql)
            print("Table \"Customers\" was reset successfully.")
            super().get_connection.commit()

        except Exception as e:
            print(f"Error resetting Customers table: {e}")

#3 Add
    def add(self, first_name, last_name, phone_number):
        """Adds a new customer to the database.
        This function is called during Database setup and when booking the rental to create a new customer"""
        try:
            # First, check if customer already exists (by phone number)
            existing_customer = self.fetch(phone=phone_number)
            if existing_customer:
                print(f"Customer {first_name} {last_name}  with Phone Number {phone_number} already exists.")
                return existing_customer[0]     # Return the ID of the existing customer

            # If not, insert new customer
            sql = """
                INSERT INTO Customers (FirstName, LastName, Phone)
                VALUES (?, ?, ?);
            """
            super().get_cursor.execute(sql, (first_name, last_name, phone_number))
            super().get_connection.commit()

            # Get the New Customer ID. This is auto-generated primary key ID of the newly added record.
            new_customer_id = super().get_cursor.lastrowid
            print(f"Successfully added. New Customer ID: {new_customer_id}\nName: {first_name} {last_name}\nPhone Number: {phone_number}")
            return new_customer_id

        except Exception as e:
            print(f"Error occurred while adding customer {first_name} {last_name} {phone_number}. Error Details: {e}")
            return None

# 4 Fetch Customer
    def fetch(self, customer_id=None, phone=None):
        """
        Fetches customer records.
        - If customer_id is given, fetches one specific customer.
        - If phone is given, fetches one specific customer.
        - If neither is given, fetches all customers.
        """
        try:
            if customer_id is not None:
                return super().get_cursor.execute("SELECT * FROM Customers WHERE id = ?;", (customer_id,)).fetchone()
            elif phone is not None:
                return super().get_cursor.execute("SELECT * FROM Customers WHERE Phone = ?;", (phone,)).fetchone()
            else:
                return super().get_cursor.execute("SELECT * FROM Customers;").fetchall()
        except Exception as e:
            print(f"Error fetching customer(s): {e}")
            return []

# 5 Update Customer's Details
    def update(self, customer_id, first_name = None, last_name = None, phone_number = None):
        """Updates a customer record by ID."""

        try:

            parameters = []     # Stores the actual values that will replace the ? placeholders in the SQL query
            sql_parts = []      # Stores the column updates that will go into the SQL SET clause

            # Dynamic built-up of queries based on what is provided
            if first_name is not None:
                parameters.append(first_name)
                sql_parts.append("FirstName = ?")
            if last_name is not None:
                sql_parts.append("LastName = ?")
                parameters.append(last_name)
            if phone_number is not None:
                sql_parts.append("Phone = ?")
                parameters.append(phone_number)

            # If there is no new data provided to update, stop
            if not sql_parts:
                print("Update Aborted! No new data provided.")
                return False
            # Join of sql_parts with sql_parts and parameters-placeholders for a given customer ID
            sql = f"UPDATE Customers SET {', '.join(sql_parts)} WHERE id = ?;"

            # Update by Customer ID
            parameters.append(customer_id)
            # Runs the SQL query with all the parameters safely substituted
            super().get_cursor.execute(sql, tuple(parameters))
            # Establish DB Connection and Save the changes.
            super().get_connection.commit()
            print(f"Updated Customer ID: {customer_id} successfully.")
            return True

        except Exception as e:
            # Catches exceptions for duplicates. Eg - ph num are uniquely constraint.
            print(f"Error updating customer {customer_id}: {e}")
            return False


# RENTALS CLASS
class Rentals(db.DBbase):
    __tablename__ = 'Rentals'
    """Inherits from the DBBase class performs CRUD operations for Rentals"""

# 1 - Constructor
    def __init__(self):
        super().__init__("boat_rental.sqlite")      # db_name = boat_rental.sqlite

# 2 - Create or Reset Database for Rentals Table
    def reset_database(self):
        """Creates or resets the Rentals table"""
        try:
            """Date, BoatType, Make, Model, Capacity, HourlyRate, AvailabilityStatus"""
            sql = """
                DROP TABLE IF EXISTS Rentals;
                
                CREATE TABLE Rentals (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    boat_id INTEGER NOT NULL,
                    customer_id INTEGER NOT NULL,
                    StartTime TEXT NOT NULL,
                    EndTime TEXT,      
                    TotalRentalHours REAL,
                    TotalCosts REAL,
                    Rental_Status TEXT NOT NULL DEFAULT 'Active',
                    
                    -- These lines link the tables and enforce data integrity
                    FOREIGN KEY (customer_id) REFERENCES Customers(id),
                    FOREIGN KEY (boat_id) REFERENCES boat_rental_entities(id)
                );                
            """
            super().execute_script(sql)
            print("Table \"Rentals\" is Reset Successfully!")
            super().get_connection.commit()

        except Exception as e:
            print(f"An error has occurred while resetting Rental Table.\nError Details: {e}")

# 3: Customers Rental Record (BOOKING)
    def rental_booking_records(self, boat_id, customer_id, start_time):
        """
        Creates a new rental record and updates the boat's status to 'Rented'.
        This is a "transaction" that affects two tables.
        """
        # Boat instance to manage the boat operations
        boat_manager = Boat()

        try:
            # --- Step 1: Check if the boat is available ---
            boat_record = boat_manager.fetch(boat_id)

            if not boat_record:
                raise Exception(f"Boat ID {boat_id} is not found!")

            availability_status_index = 7       # The 8th column (index 7) is 'AvailabilityStatus'

            if boat_record[availability_status_index] != 'Available':
                raise Exception(f"Boat ID {boat_id} is not available for rent!\nStatus: {boat_record[availability_status_index]}")

            # --- Step 2: If available, create the rental record ---
            sql = """
                INSERT INTO Rentals (
                boat_id, customer_id, StartTime)
                VALUES (?, ?, ?)
            """
            super().get_cursor.execute(sql, (boat_id, customer_id, start_time))
            super().get_connection.commit()

            # --- Step 3: Update the boat's status to 'Rented' ---
            boat_manager.update(boat_id, availability_status="Rented")
            return True     # Success

        except Exception as e:
            print(f"An error has occurred during booking.\nError Details: {e}")
            return False    # Failure

        finally:
            # Close the boat_manager's connection, even if an error happened.
            boat_manager.close_db()

# 4: Finalize Rental (RETURN)
    def complete_rental(self, rental_id, end_time, rental_hours):
        """
        Completes a rental. Updates the rental record with costs and updates the boat's status back to 'Available'.
        """

        # Boat Manager — A Boat object to get the rate and update its status
        boat_manager = Boat()

        try:
            # --- Step 1: Get the rental record ---
            rental_record = self.fetch_rental(rental_id)

            if not rental_record:
                raise Exception(f"Rental ID {rental_id} does not exist.")

            # rental_record[8] is 'Rental_Status' from the fetch_rental query
            if rental_record[8] == 'Completed':
                raise Exception(f"Rental ID {rental_id} has already been rented.")

            # --- Step 2: Get boat details to calculate cost ---
            boat_id = rental_record[1]
            boat_record = boat_manager.fetch(boat_id)

            # boat_record[6] is 'HourlyRate' from the Boat table
            if not boat_record:
                raise Exception(f"Rental ID {rental_id} does not exist.")

            # HourlyRate is at (index 6) in the fetch_rental SELECT statement
            hourly_rate = boat_record[6]
            total_costs = rental_hours * hourly_rate

            # --- Step 3: Update the Rentals table ---
            sql = """
                UPDATE Rentals SET 
                    EndTime = ?,
                    TotalRentalHours = ?,
                    TotalCosts = ?,
                    Rental_Status = "Completed"
                WHERE id = ?;
            """
            super().get_cursor.execute(sql, (end_time, rental_hours, total_costs, rental_id))
            super().get_connection.commit()

            # --- Step 4: Update the boat's status back to 'Available' ---
            boat_manager.update(boat_id, availability_status="Available")

            # Display rental information
            print(f"Rental ID {rental_id} is completed. Total Costs: {total_costs:.2f}.")

        except Exception as e:
            print(f"An error has occurred.\nError Details: {e}")

        finally:
            # Close the boat_manager's connection
            boat_manager.close_db()

    # 5: Fetch rental records
    def fetch_rental(self, rental_id=None, status=None):
        """Fetches Rental records with friendly names from other tables."""
        try:
            sql = """
                SELECT 
                    Rnt.id,
                    Bot.id AS boat_id,
                    Bot.Make || ' ' || Bot.Model AS BoatName, 
                    Cust.FirstName || ' ' || Cust.LastName AS CustomerName,
                    Rnt.StartTime, 
                    Rnt.EndTime, 
                    Rnt.TotalRentalHours, 
                    Rnt.TotalCosts, 
                    Rnt.Rental_Status, 
                    Bot.HourlyRate
                FROM Rentals Rnt
                -- Keeping all rows from the left table, no matter what with LEFT JOIN
                -- Join Rentals to Boats
                LEFT JOIN boat_rental_entities Bot ON Bot.id = Rnt.boat_id 
                -- Join Rentals to Customers
                LEFT JOIN Customers Cust ON Cust.id = Rnt.customer_id
            """

            # Add conditions based on function arguments
            if rental_id is not None:
                sql += " WHERE Rnt.id = ?;"
                return super().get_cursor.execute(sql, (rental_id,)).fetchone()

            elif status is not None:
                sql += " WHERE Rnt.Rental_Status = ?;"
                return super().get_cursor.execute(sql, (status,)).fetchall()

            else:
                sql += " ORDER BY Rnt.id DESC;"     # Show newest first
                return super().get_cursor.execute(sql).fetchall()

        except Exception as e:
            print(f"An error has occurred while fetching Rentals.\nError Details: {e}")
            return []

# DATA POPULATOR CLASS (File I/O)
class DataPopulator:
    """
    A helper class just for populating the database. It reads from a CSV file and inserts initial data.
    """

# 1: Constructor
    def __init__(self):
        # super().__init__("boat_rental_DB.sqlite")
        pass    # Doesn't need to do anything

# 2: Populate Database
    def populate_database(self, db_csv_path="boat_rentals.csv"):
        """Rebuilding and initializing the entire database.
            1. Deletes any existing database file (to start fresh).
            2. Recreates all database tables.
            3. Imports boat data from a CSV file.
            4. Adds sample customers.
            5. Creates one initial rental record for testing.
            6. Closes all database connections safely.
        """
        db_file = "boat_rental.sqlite"

        # --- STEP 1: Delete old database file to ensure a fresh start ---
        print("\nResetting all databases...")

        # Checking if file above db_file exists. If Yes, delete it to ensure clean and fresh start
        if os.path.exists(db_file):
            os.remove(db_file)
            print("Old database removed. Creating a fresh one...")

        # --- STEP 2: Create new, empty tables ---
        # Create instances of each entity class
        boat_instance = Boat()
        customer_instance = Customers()
        rental_instance = Rentals()

        # Call their reset_database() methods to build the schemas (tables and columns) - Blank DB Structure
        boat_instance.reset_database()
        customer_instance.reset_database()
        rental_instance.reset_database()
        print("Database reset complete.")

        try:
            # Open a temporary connection to the new database.
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            # New CSV File
            csv_file = "boat_rentals.csv"

            # Insert from CSV after the new table is ready

            if os.path.exists(csv_file):
                # Open the CSV file
                with open(csv_file, "r", newline="", encoding="utf-8") as f:
                    # Using DictReader() to read rows as dictionaries
                    reader = csv.DictReader(f)
                    boats_to_add = []      # List of tuples, ready for insertion
                    # Prepare a list of tuples with all boat data
                    for row in reader:
                        boats_to_add.append((
                            row["Date"],
                            row["BoatType"],
                            row["Make"],
                            row["Model"],
                            int(row["Capacity"]),
                            float(row["HourlyRate"]),
                            row["AvailabilityStatus"]
                        ))
                        # Use .executemany() for a fast, bulk insert
                    cur.executemany("""
                                        INSERT INTO boat_rental_entities
                                        (Date, BoatType, Make, Model, Capacity, HourlyRate, AvailabilityStatus)
                                        VALUES (?, ?, ?, ?, ?, ?, ?)
                                    """, boats_to_add)

                print(f"Loaded {len(boats_to_add)} records from {csv_file} into SQLite.")

            else:
                print("CSV file not found, created empty database.")

            # Commit the boat data and close the temporary connection
            conn.commit()
            conn.close()

        except Exception as e:
            print(f"An error has occurred during CSV Population.\nError Details: {e}")

        # --- STEP 4: Add/Populate with sample Customers ---
        print("\nPopulating sample customer data...")
        customer_data = [
                ('Alice', 'Smith', '764-471-4445'),
                ('Bob', 'Johnson', '800-668-9144'),
                ('Charlie', 'Brown', '668-991-8453'),
                ('Diana', 'Prince', '433-919-4876'),
                ('Emily', 'Davis', '558-485-7260'),
                ('Frank', 'Garcia', '269-420-6326'),
                ('Grace', 'Lee', '263-291-2607'),
                ('Henry', 'Wilson', '661-317-7811'),
                ('Ivy', 'Martinez', '440-907-6986'),
                ('Jack', 'Robinson', '504-522-5939'),
                ('Kate', 'Clark', '244-335-6316'),
                ('Leo', 'Rodriguez', '648-712-2695'),
                ('Mia', 'Lewis', '710-252-3606'),
                ('Noah', 'Walker', '628-457-9056'),
                ('Olivia', 'Hall', '276-246-7674'),
                ('Peter', 'Allen', '646-875-9903'),
                ('Quinn', 'Young', '715-642-7587'),
                ('Ryan', 'King', '558-329-6151'),
                ('Sophia', 'Wright', '233-493-9508'),
                ('Thomas', 'White', '278-384-9677')
                ]
        # Use the customer_instance.add() method to add them one by one
        for firstName, lastName, phoneNum in customer_data:
            customer_instance.add(firstName, lastName, phoneNum)
        print("Customers added successfully.")

        # --- STEP 5: Populate one initial sample Rental ---
        # This makes the "Return Rental" feature testable on first run
        print("\n---Booking Initial Rental Records---")

        try:
            # Find the customer "Alice" we just added above
            customer_record = customer_instance.fetch(phone="764-471-4445")    # Assuming Known - "Alice", "Smith", "555-0101"

            if customer_record:
                customer_id = customer_record[0]
                # Get Boat ID 1
                boat_record = boat_instance.fetch(1)        # Fetches Boat with ID 1 from boat_rental_entities table.

                # Book the rental if customer and boat exist and boat is available
                if customer_id and boat_record and boat_record[7] == "Available":
                    start_time = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

                    # Use the rental_instance.rental_booking_records() method
                    success = rental_instance.rental_booking_records(1, customer_id, start_time)

                    if success:
                        print(f"Initial Rental Booking Record for customer {customer_id} is Successful.")
                    else:
                        print(f"Initial rental booking failed for customer {customer_id}.")
                else:
                    print(f"Could not fetch initial rental booked for customer {customer_id}.")

            else:
                print("Could not find customer \"555-0101\" for initial rental booking.")

        except Exception as e:
            print(f"Error booking initial record.\nError Details: {e}")

        # --- STEP 6: Close all database connections ---
        boat_instance.close_db()
        customer_instance.close_db()
        rental_instance.close_db()
        print("Database populated successfully.")


