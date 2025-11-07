import sqlite3
# MAIN CLASS
class DBbase:
    """
    This is the parent class for all database-handling classes (e.g., Boat, Customers).
    It manages the connection and cursor, so child classes don't have to.
    This principle is known as Inheritance.
    """

    """Class-level attributes to hold no active connection or cursor. Only runs after Object is created and 
    self.connect() is run"""
    _conn = None
    _cursor = None

    def __init__(self, db_name):
        """
        Constructor: Called automatically when a new instance (e.g., Boat()) is created.
        """
        # Stores the database filename (e.g., "boat_rental.sqlite")
        self._db_name = db_name     # Tells the object which DB file it should be connected to
        # Automatically connect to the DB upon creation
        self.connect()

    def connect(self):
        """Connect to the database — filename or path to the database name."""
        self._conn = sqlite3.connect(self._db_name)
        """
        CURD is done through the cursor, which is a portal to the database. Must have a connection for the cursor.
        """
        # Creates a cursor object to execute SQL commands
        self._cursor = self._conn.cursor()

    def execute_script(self, sql_string):
        """
        Runs a string containing one or more SQL statements. This is useful for 'CREATE TABLE' or 'DROP TABLE' scripts.
        """
        # Establishes the connection to the SQLite file. Supports multiple SQL statements
        self._cursor.executescript(sql_string)

    def reset_database(self):
        """
        This is a "placeholder" or "abstract" method.
        It's meant to be overridden by the child classes (Boat, Customers, Rentals).
        This forces each child class to define its own specific 'reset' logic.
        """
        raise NotImplementedError("Must implement from the derived class")

    def close_db(self):
        """Commit pending changes and close the database connection."""
        # Check if a connection actually exists
        if self._conn is not None:
            try:
                #1 Commit any remaining transactions (like INSERT's or UPDATE's)
                self._conn.commit()
                #2 Close the cursor
                self._cursor.close()
                #3 Close the connection
                self._conn.close()
            except Exception as e:
                # Log any errors that happen during closing
                print(f"Failed to close database connection. {e}")
            finally:
                # Ensure these are set to None so the program knows the connection is gone
                self._conn = None
                self._cursor = None

    """
    Decorators (@property) – Allows us to access private attributes like _cursor and _conn as if they were public 
    attributes, without needing parentheses.
    This lets us write 'db.get_cursor' instead of 'db.get_cursor()'.
    """
    @property
    def get_cursor(self):
        """A 'getter' property to safely access the cursor."""
        return self._cursor

    @property
    def get_connection(self):
        """A 'getter' property to safely access the connection."""
        return self._conn



