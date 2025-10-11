import DBbase as db

class Parts(db.DBbase):

    def __init__(self):
        super().__init__("inventoryDB.sqlite")

    def update(self, part_id, name):    # Primary Key and Name parameters.
        try:
            super().get_cursor.execute("update Parts set name = ? where id = ?;", (name, part_id))
            super().get_connection.commit()
        except Exception as ex:
            print("An error occurred.", ex)
            print(f"Updated record to {name} successfully.")

    def add(self, name):
        try:
            super().get_cursor.execute("insert or ignore into Parts (name) values(?);", (name,))    # Expects a Tuple
            super().get_connection.commit()
            print(f"Added {name} successfully.")

        except Exception as ex:
            print("An error occurred.", ex)

    def delete(self, part_id):
        try:
            super().get_cursor.execute("delete from Parts where id = ?;", (part_id,))
            super().get_connection.commit()
            print(f"Deleted Part ID: {part_id} successfully.")
            return True
        except Exception as ex:
            print("An error occurred.", ex)
            return False

    def fetch(self, id = None,  part_name = None):
        # Check first if id is not None
        try:
            if id is not None:
                return super().get_cursor.execute("select * from Parts WHERE id = ?;", (id,)).fetchone()
            elif part_name is not None:
                return super().get_cursor.execute("select * from Parts WHERE name = ?;", (part_name,)).fetchone()
            else:
                return super().get_cursor.execute("select * from Parts;").fetchall()
        except Exception as ex:
            print("An error occurred.", ex)

    def reset_database(self):
        try:
            sql = """
                    DROP TABLE IF EXISTS Parts;
                    
                    CREATE TABLE Parts (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT UNIQUE);
            """
            super().execute_script(sql)
        except Exception as ex:
            print("An error occurred.", ex)
        finally:
            super().close_db()

# parts = Parts()
# #parts.reset_database()
# #parts.add("Dr. Pepper")
# #parts.update(2, "Coca Cola Classic")
# #parts.delete(2)
# # parts.add("Sprite Zero")
# # parts.add("Headphones")
# # parts.add("Macbook Pro")
# print(parts.fetch(part_name="Headphones"))
# print(parts.fetch())

class Inventory(Parts):

    def add_inv(self, name, quantity, price):
        try:
            # Add the part item first
            super().add(name)
        except Exception as ex:
            print("An error occurred in the Parts class.", ex)
        else:
            try:
                part_id = super().fetch(part_name=name)
                if part_id is not None:
                    super().get_cursor.execute("""INSERT INTO Inventory (part_id, quantity, price)
                     VALUES (?, ?, ?); """, (part_id[0], quantity, price))
                    super().get_connection.commit()
                    print(f"Inventory {name} added successfully.")
                else:
                    raise Exception("The id of the Part name was not found.")
            except Exception as ex:
                print("An error occurred in the Inventory class.", ex)

    def update_inv(self, id, quantity, price):
        try:
            super().get_cursor.execute("""UPDATE Inventory SET quantity = ?, price = ? WHERE id = ?;""",
                                       (quantity, price, id))
            super().get_connection.commit()
            print(f"Inventory {id} updated successfully.")
            return True
        except Exception as ex:
            print("An error occurred.", ex)
            return False

    def delete_inv(self, inventory_id):
        try:
            record = self.fetch_inv(inventory_id)

            if record is None:
                raise Exception(f"No inventory record found with id: {inventory_id}")

            part_id = record[1]  # index 1 is part_id from the SELECT query

            if part_id is not None:
                return_status = super().delete(part_id)
                super().get_connection.commit()

                if return_status is False:
                    raise Exception("Delete method in parts failed, Delete aborted.")

        except Exception as ex:
            print("An error occurred.", ex)
        else:
            try:
                super().get_cursor.execute("""DELETE FROM Inventory WHERE id = ?;""", (inventory_id,))
                super().get_connection.commit()
            except Exception as ex:
                print("An error occurred in Inventory Delete.", ex)

    def fetch_inv(self, id=None):
        try:
            if id is not None:
                return_value = super().get_cursor.execute("""SELECT Inventory.id, part_id, p.name, quantity, price
                    FROM Inventory
                    JOIN Parts p ON Inventory.part_id = p.id
                    WHERE Inventory.id = ?;
                """, (id,)).fetchone()
                return return_value
            else:
                return super().get_cursor.execute("""SELECT Inventory.id, part_id, p.name, quantity, price
                    FROM Inventory
                    JOIN Parts p ON Inventory.part_id = p.id;""").fetchall()

        except Exception as ex:
            print("An error occurred.", ex)

    def reset_database(self):
        try:
            sql = """
                DROP TABLE IF EXISTS Inventory;
                
                CREATE TABLE Inventory (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        part_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        price VARCHAR(20)
                );
            """
            super().execute_script(sql)
            print("Inventory table successfully created.")
        except Exception as ex:
            print("An error occurred.", ex)
        finally:
            super().close_db()
