import sqlite3
class DBbase:

    _conn = None
    _cursor = None

    def __init__(self, db_name):
        self._db_name = db_name
        self.connect()

    def connect(self):
        """Connect to the database — filename or path to the database name."""
        self._conn = sqlite3.connect(self._db_name)
        """
        CURD is done through the cursor, which is a portal to the database.
        Must have a connection for the cursor.
        """
        self._cursor = self._conn.cursor()

    # def execute_script(self, sql_string):
    #     """Access the cursor, and execute the script."""
    #     self._cursor.execute(sql_string)
    def execute_script(self, sql_string):
        self._cursor.executescript(sql_string)  # Supports multiple SQL statements

    def reset_database(self):
        """Reset the database."""
        raise NotImplementedError("Must implement from the derived class")

    def close_db(self):
        """Close the connection."""
        self._conn.close()

    """Decorators (@property) – Allows us to access private attributes like _cursor and _conn 
    as if they were public attributes, without needing parentheses."""
    @property
    def get_cursor(self):
        return self._cursor

    @property
    def get_connection(self):
        return self._conn



