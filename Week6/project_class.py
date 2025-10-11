import parts_inventory as pv


class Project:
    def run(self):

        inventory_options = { "get": "Get all Inventory",
                              "getby": "Inventory by Id",
                              "update": "Update Inventory",
                              "add": "Add Inventory",
                              "delete": "Delete Inventory",
                              "reset": "Reset Database",
                              "exit": "Exit Program"
                              }
        print("Welcome to my Inventory Program. Please choose a selection")
        user_selection = ""
        while user_selection != "exit":
            print("*** Option list ***")

            for option in inventory_options.items():
                print(option)

            user_selection = input("Select an option: ").lower()

            inventory = pv.Inventory()

            if user_selection == "get":
                results = inventory.fetch_inv()
                for item in results:
                    print(item)

            elif user_selection == "getby":

                inv_id = input("Enter Inventory Id: ")
                results = inventory.fetch_inv(inv_id)
                print(results)
                input("Press return/enter to continue")

            # Update
            elif user_selection == "update":

                results = inventory.fetch_inv()
                for item in results:
                    print(item)

                inv_id = input("Enter Inventory Id: ")
                quantity = input("Enter Quantity Amount: ")
                price = input("Enter Unit Price: ")
                inventory.update_inv(inv_id, quantity, price)
                print(inventory.fetch_inv(inv_id))
                input("Press return/enter to continue")

            # Add
            elif user_selection == "add":
                name = input("Enter part name: ").lower()
                quantity = input("Enter Quantity Amount: ")
                price = input("Enter Unit Price: ")
                inventory.add_inv(name, quantity, price)
                print("Done\n")
                input("Press return/enter to continue")

            # Delete
            elif user_selection == "delete":
                inv_id = input("Enter Inventory Id: ")
                inventory.delete_inv(inv_id)
                print("Done\n")
                input("Press return/enter to continue")
            elif user_selection == "reset":
                confirm = input("This will delete all records in parts and inventory, continue? (Y/N)").lower()
                if confirm == "y":
                    inventory.reset_database()
                    parts = pv.Parts()
                    parts.reset_database()
                    print("Reset Complete")
                    input("Press return/enter to continue")
                else:
                    print("Reset Aborted!")
                    input("Press return/enter to continue")

            else:
                if user_selection != "exit":
                    print("Invalid Selection. Please try again.\n")

project = Project()
project.run()
